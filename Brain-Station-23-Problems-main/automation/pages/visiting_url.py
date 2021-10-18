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
#from pages.home import HomePage
from resources.locators import common_locators as cl


class HomePage(BasePage):
    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)
    
    def call_us_now(self):
        wrap = self.Wrap
        elem = wrap.wait_until_visibility_of_element_located(10, cl.call_us_now_xpath)
        return bool(elem)
    
    def cart_visibility(self):
        wrap = self.Wrap
        elem = wrap.wait_until_visibility_of_element_located(10, cl.cart_xpath)
        return bool(elem)
    
    def visibility_of_compoment(self):
        wrap = self.Wrap
        elem = wrap.wait_until_visibility_of_element_located(10, cl.women_xpath)
        elem1 = wrap.wait_until_visibility_of_element_located(10, cl.dress_xpath)
        elem2 = wrap.wait_until_visibility_of_element_located(10, cl.tshirt_xpath)
        return bool(elem), bool(elem1), bool(elem2)
    