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

class adding_users(BasePage):
    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)
    
    def adding_user_1(self):
        wrap = self.Wrap
        wrap.wait_until_element_clickable(10, cl.signin_xpath).click()
        wrap.wait_until_element_clickable(10, cl.email_xpath).click()
        try: 
            wrap.wd_Send_keys(cl.email_xpath, cndemo.email1)
        except  TimeoutException:  
            print("THIS USE HAS BEEN ADDED")
        wrap.wait_until_element_clickable(10, cl.account_create).click()
        elem = wrap.wait_until_visibility_of_element_located(10, cl.account_create_header)

        wrap.wait_until_element_clickable(10, cl.account_title_radio_MR_xpath).click()
        wrap.wait_until_element_clickable(10, cl.account_first_name_xpath).click()
        wrap.wd_Send_keys(cl.account_first_name_xpath,cndemo.user1_first_name)
        
        wrap.wait_until_element_clickable(10, cl.account_last_name_xpath).click()
        wrap.wd_Send_keys(cl.account_last_name_xpath,cndemo.user1_last_name)

        wrap.wait_until_element_clickable(10, cl.account_password_xpath).click()
        wrap.wd_Send_keys(cl.account_password_xpath,cndemo.password)

        wrap.scroll_to_specific_xpath(cl.account_DOB_date_xpath)
        wrap.wait_until_element_clickable(10, cl.account_DOB_days_01_xpath).click()
        wrap.wait_until_element_clickable(10, cl.account_DOB_month_january_xpath).click()
        wrap.wait_until_element_clickable(10, cl.account_DOB_year_2021_xpath).click()

        #address
        wrap.wait_until_element_clickable(10, cl.address_first_name_xpath).click()
        wrap.wd_Send_keys(cl.address_first_name_xpath, cndemo.address_first_name)
        wrap.wait_until_element_clickable(10, cl.address_last_name_xpath).click()
        wrap.wd_Send_keys(cl.address_last_name_xpath,cndemo.address_last_name)
        wrap.wait_until_element_clickable(10, cl.address_company_name_xpath).click()
        wrap.wd_Send_keys(cl.address_company_name_xpath, cndemo.address_company_name)
        wrap.wait_until_element_clickable(10, cl.address_xpath).click()
        wrap.wd_Send_keys(cl.address_xpath,cndemo.address)
        wrap.wait_until_element_clickable(10, cl.address_city_xpath).click()
        wrap.wd_Send_keys(cl.address_city_xpath,cndemo.address_city_xpath)
        wrap.wait_until_element_clickable(10, cl.address_state_xpath).click()
        wrap.scroll_to_specific_xpath(cl.address_postcode_xpath)
        wrap.wait_until_element_clickable(10, cl.address_postcode_xpath).click()
        wrap.wd_Send_keys(cl.address_postcode_xpath,cndemo.address_postcode)
        wrap.wait_until_element_clickable(10, cl.address_additional_info_xpath).click()
        wrap.wd_Send_keys(cl.address_additional_info_xpath,cndemo.address_additional_info)
        wrap.wait_until_element_clickable(10, cl.address_mobile_xpath).click()
        wrap.wd_Send_keys(cl.address_mobile_xpath,cndemo.address_mobile)
        
        #register
        wrap.wait_until_element_clickable(10, cl.register_button_xpath).click()
        elem1 = wrap.wait_until_visibility_of_element_located(10, cl.my_account_xpath)
        return bool(elem), bool(elem1)

    def adding_user_2(self):
        wrap = self.Wrap
        wrap.wait_until_element_clickable(10, cl.signin_xpath).click()
        wrap.wait_until_element_clickable(10, cl.email_xpath).click()
        try: 
            wrap.wd_Send_keys(cl.email_xpath, cndemo.email2)
        except  TimeoutException:  
            print("THIS USE HAS BEEN ADDED")
        wrap.wait_until_element_clickable(10, cl.account_create).click()
        elem = wrap.wait_until_visibility_of_element_located(10, cl.account_create_header)

        wrap.wait_until_element_clickable(10, cl.account_title_radio_MR_xpath).click()
        wrap.wait_until_element_clickable(10, cl.account_first_name_xpath).click()
        wrap.wd_Send_keys(cl.account_first_name_xpath,cndemo.user2_first_name)
        
        wrap.wait_until_element_clickable(10, cl.account_last_name_xpath).click()
        wrap.wd_Send_keys(cl.account_last_name_xpath,cndemo.user2_last_name)

        wrap.wait_until_element_clickable(10, cl.account_password_xpath).click()
        wrap.wd_Send_keys(cl.account_password_xpath,cndemo.password)

        wrap.scroll_to_specific_xpath(cl.account_DOB_date_xpath)
        wrap.wait_until_element_clickable(10, cl.account_DOB_days_01_xpath).click()
        wrap.wait_until_element_clickable(10, cl.account_DOB_month_january_xpath).click()
        wrap.wait_until_element_clickable(10, cl.account_DOB_year_2021_xpath).click()

        #address
        wrap.wait_until_element_clickable(10, cl.address_first_name_xpath).click()
        wrap.wd_Send_keys(cl.address_first_name_xpath, cndemo.address_first_name)
        wrap.wait_until_element_clickable(10, cl.address_last_name_xpath).click()
        wrap.wd_Send_keys(cl.address_last_name_xpath,cndemo.address_last_name)
        wrap.wait_until_element_clickable(10, cl.address_company_name_xpath).click()
        wrap.wd_Send_keys(cl.address_company_name_xpath, cndemo.address_company_name)
        wrap.wait_until_element_clickable(10, cl.address_xpath).click()
        wrap.wd_Send_keys(cl.address_xpath,cndemo.address)
        wrap.wait_until_element_clickable(10, cl.address_city_xpath).click()
        wrap.wd_Send_keys(cl.address_city_xpath,cndemo.address_city_xpath)
        wrap.wait_until_element_clickable(10, cl.address_state_xpath).click()
        wrap.scroll_to_specific_xpath(cl.address_postcode_xpath)
        wrap.wait_until_element_clickable(10, cl.address_postcode_xpath).click()
        wrap.wd_Send_keys(cl.address_postcode_xpath,cndemo.address_postcode)
        wrap.wait_until_element_clickable(10, cl.address_additional_info_xpath).click()
        wrap.wd_Send_keys(cl.address_additional_info_xpath,cndemo.address_additional_info)
        wrap.wait_until_element_clickable(10, cl.address_mobile_xpath).click()
        wrap.wd_Send_keys(cl.address_mobile_xpath,cndemo.address_mobile)
        
        #register
        wrap.wait_until_element_clickable(10, cl.register_button_xpath).click()
        elem1 = wrap.wait_until_visibility_of_element_located(10, cl.my_account_xpath)
        return bool(elem), bool(elem1)

        
        