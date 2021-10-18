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
    
    def wd_click_simple(self, locator):
        self.drv.find_element_by_xpath(locator).click()

    def wd_implicitly_wait(self, time):
        self.drv.implicitly_wait(time) 
                
    def wait_until_element_clickable(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))   
        return webel
    
    def wait_until_visibility_of_element_located(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel  

    def wd_Send_keys_siimple (self, locator, text):
        self.drv.find_element_by_xpath(locator).send_keys(text)    
    
    def handle_webelement_exception(self, waitTime, locator,message ):   
        wait = WebDriverWait(self.drv, waitTime)
        try: 
            webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except  NoSuchElementException:  
            print(message)
            
    def wait_untill_visibility_CSS(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))   
        return webel 
      
    def simpleXpath_with_click(self,locator):
        webel = self.drv.find_element_by_xpath(locator).click()
        return webel

    def handling_window(self):
        parentWindow = self.drv.current_window_handle
        childWindow = self.drv.current_window_handle
        allWindows = self.drv.window_handles
        for n in allWindows:
            if(parentWindow != n):
                self.drv.switch_to.window(n)
                break

            print(message)

    def wait_until_visibility_of_element_located_CLASS_NAME(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))   
        return webel 

    def scroll_to_specific_xpath(self, locator):
        #wait = WebDriverWait(self.drv, waitTime)
        webel = self.drv.find_element_by_xpath(locator)
        webel.location_once_scrolled_into_view
    
    def wait_until_element_CSS_clickable(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator)))   
        return webel
