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
import time

#from webdriver_manager import driver

@pytest.fixture
def setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    #request.cls.driver = web_driver
    driver.maximize_window()
    driver.get(cndemo.url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, cl.your_logo_xpath )))
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