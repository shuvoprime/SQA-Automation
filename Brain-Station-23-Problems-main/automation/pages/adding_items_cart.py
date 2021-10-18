from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium.common.exceptions import NoSuchElementException , TimeoutException
sys.path.append(".")
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from tests.conftest import  setup
from resources.credentials import Constantinope as cndemo
from resources.locators import common_locators as cl

class cart(BasePage):
    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)
    
    def cart_add(self):
        wrap = self.Wrap
        wrap.wait_until_element_clickable(10, cl.signin_xpath).click()
        wrap.wait_until_element_clickable(10, cl.registered_email_xpath).click()
        wrap.wd_Send_keys(cl.registered_email_xpath,cndemo.email1)
        wrap.wait_until_element_clickable(10, cl.account_password_xpath).click()
        wrap.wd_Send_keys(cl.account_password_xpath,cndemo.password)
        wrap.wait_until_element_clickable(10, cl.registered_signin_button_xpath).click()

        wrap.wait_until_element_clickable(10, cl.cart_dress_xpath).click()
        wrap.scroll_to_specific_xpath(cl.cart_dress_casual_xpath)
        wrap.wait_until_element_clickable(10, cl.cart_dress_casual_xpath).click()

        wrap.scroll_to_specific_xpath(cl.cart_printed_dress_xpath)
        wrap.wait_until_visibility_of_element_located(10, cl.cart_printed_dress_xpath)
        wrap.wait_until_element_clickable(10, cl.cart_printed_dress_xpath).click()

        wrap.wait_until_element_clickable(10, cl.add_to_cart_xpath).click()
        wrap.wait_until_element_clickable(10, cl.proceed_to_checkout).click()
        
        wrap.wait_until_element_clickable(10, cl.summary_proceed_to_click).click()
        wrap.wait_until_element_clickable(10, cl.summary_proceed_to_checkout).click()
        wrap.wait_until_element_clickable(10, "//label[contains(text(),'I agree to the terms of service and will adhere to')]").click()
        wrap.wait_until_element_clickable(10, cl.summery_shipping_proceed_to_checkout).click()
        wrap.wait_until_element_clickable(10, "//a[@title='Pay by check.']").click()
        wrap.wait_until_element_clickable(10, "//span[normalize-space()='I confirm my order']").click()
        
        elem = wrap.wait_until_visibility_of_element_located(10, "//h1[normalize-space()='Order confirmation']")
        return bool(elem)
    