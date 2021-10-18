import pytest
import sys
sys.path.append(".")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
from pages.wrapper import BasePage
from resources.credentials import Constantinope as cndemo
from selenium.webdriver.chrome.options import Options
from resources.locators import common_locators as cl
from resources.locators import Locators_Homepage as LH

import time

#from webdriver_manager import driver

@pytest.fixture
def setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options) 
    driver.maximize_window()
    wrap = BasePage(driver)

    driver.get(cndemo.Commurl)
    wrap.wait_until_element_clickable(20, cl.cookiee_button_xpath).click()
    time.sleep(3)
    wrap.wait_until_visibility_of_element_located(10, cl.signin_username_xpath)
    wrap.wd_Send_keys_siimple( cl.signin_username_xpath , cndemo.username)
    wrap.wd_Send_keys_siimple(cl.signin_password_xpath , cndemo.password)
    wrap.wait_until_element_clickable(10, cl.radio_button_remeber_me_xpath).click()
    wrap.wait_until_element_clickable(10, cl.signin_submit_xpath).click()
    elem = wrap.wait_until_visibility_of_element_located(15, cl.community_name_header_xpath)
    print(elem.text)
    return driver

@pytest.fixture
def teardown():
    driver.close()
    driver.quit()
    return teardown

'''
setup()
teardown()
'''