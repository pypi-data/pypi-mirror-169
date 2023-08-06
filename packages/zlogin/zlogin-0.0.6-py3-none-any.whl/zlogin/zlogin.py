"""
ZLOGIN Module is for auto-login for Zerodha and storage of the access token to dynamoDB. 
This works in conjunction with store_access module which creates a Lambda container handling re-direct url from zerodha
"""
import os
import sys
from time import sleep
from urllib.parse import quote_plus
from datetime import datetime
from logging import getLogger, INFO, StreamHandler

import boto3
from undetected_chromedriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from pyotp import TOTP

from kiteconnect import KiteConnect, KiteTicker

logger = getLogger("Zlogin")
logger.addHandler(StreamHandler(sys.stdout))
logger.setLevel(INFO)


def add_env_vars_from_file():
    path = os.path.expanduser('~/.zerodha')
    with open(path, 'r') as f:
        env_vars = dict(tuple(line.replace('\n', '').split('=')) for line
                        in f.readlines() if not line.startswith('#'))
    os.environ.update(env_vars)


def get_env_vars():
    add_env_vars_from_file()
    return dict(
        api_key=os.getenv('ZAPI'),
        api_secret=os.getenv('ZSECRET'),
        api_auth=os.getenv('ZAPI_AUTH'),
        user_id=os.getenv('ZUSER'),
        pw=os.getenv('ZPASS'),
        totp_key=os.getenv('ZTOTP'),
    )


def get_driver():
    options = ChromeOptions()
    options.headless = True
    logger.info("Driver Options Created")
    driver = Chrome(options=options)
    logger.info("Chrome Created")
    return driver


def generate_request_token(api_key, user_id, pw, totp_key, api_auth, **kwargs):
    logger.info("Generate Function Started")
    driver = get_driver()
    logger.info("Driver Acquired")
    driver.get(
        f'https://kite.trade/connect/login?v=3&api_key={api_key}&redirect_params={quote_plus(f"api_auth={api_auth}")}')
    login_id = WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.XPATH, '//input[@type="text"]'))
    login_id.send_keys(user_id)
    logger.info("USER ID Sent")
    pwd = WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.XPATH, '//input[@type="password"]'))
    pwd.send_keys(pw)
    logger.info("Pw Sent")
    sleep(1)
    submit = WebDriverWait(driver, 10).until(lambda x: x.find_element(
        By.XPATH, '//button[@type="submit"]'))
    submit.click()
    sleep(1)
    logger.info("Login Btn Clicked")
    totp = WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.XPATH, '//form//input'))
    totp.send_keys(TOTP(totp_key).now())
    logger.info("TFA Sent")
    sleep(1)
    continue_btn = WebDriverWait(driver, 10).until(lambda x: x.find_element(
        By.XPATH, '//button[@type="submit"]'))
    continue_btn.click()
    logger.info("Request Token Generated!")


def fetch_access_token():
    """
    This function fetches access token either from Dynamodb - if the token exists for today - or generates request_token
    and passes to the Lambda function to get access_token and save to DynamoDB
    Args: 
        None
    Requirements: 
        A '.zerodha' file in the home directory with values for ZAPI, ZSECRET, ZAPI_AUTH, ZUSER, ZPASS, ZTOTP
        Sample in the repo
    """
    dynamodb = boto3.resource('dynamodb')
    access_store = dynamodb.Table('access_store')
    today = datetime.utcnow().date().strftime('%Y-%m-%d')
    date_rows = access_store.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key(
            'date').eq(today),
        ScanIndexForward=False
    )['Items']
    if not date_rows:
        logger.info("Access token for today does not exist - Generating new..")
        generate_request_token(**get_env_vars())
        wait_seconds = 0
        while not date_rows:
            date_rows = access_store.query(
                KeyConditionExpression=boto3.dynamodb.conditions.Key(
                    'date').eq(today),
                ScanIndexForward=False
            )['Items']
            sleep(1)
            wait_seconds += 1
            logger.info(f'Seconds Waited: {wait_seconds}')
            if wait_seconds > 10:
                logger.info(
                    f'Exiting without success in reading newly generated access token - Seconds Waited: {wait_seconds}')
                break
    try:
        logger.info("Access Token Returned!")
        return date_rows[0]['access_token']
    except Exception as e:
        logger.error(
            'Access token not generated - Neither does one exist for today')
        raise e


def fetch_kiteconnect_instance():
    access_token = fetch_access_token()
    return KiteConnect(get_env_vars()['api_key'], access_token)


def fetch_kiteticker_instance():
    """
    Returns a KiteTicker Object (WebSocket) - that can be used by defining:
        kws.on_ticks = on_ticks
        kws.on_connect = on_connect
        kws.on_close = on_close
    """
    access_token = fetch_access_token()
    return KiteTicker(get_env_vars()['api_key'], access_token)


if __name__ == "__main__":
    print(fetch_access_token())
    print(fetch_kiteconnect_instance())
    print(fetch_kiteticker_instance())
