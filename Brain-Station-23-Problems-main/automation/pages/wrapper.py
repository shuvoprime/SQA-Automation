from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import sys

from webdriver_manager import driver
sys.path.append(".")

class BasePage(object):
    
    def __init__(self, drv):
        self.drv = drv
    
    def wait_until_element_clickable(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))   
        return webel
    
    def wait_until_visibility_of_element_located(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel  

    def wait_until_visibility_of_element_located_name(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.NAME, locator)))   
        return webel

    def wd_Send_keys (self, locator, text):
        self.drv.find_element_by_xpath(locator).clear()
        self.drv.find_element_by_xpath(locator).send_keys(text) 
    
    def scroll_to_specific_xpath(self, locator):
        #wait = WebDriverWait(self.drv, waitTime)
        webel = self.drv.find_element_by_xpath(locator)
        webel.location_once_scrolled_into_view
