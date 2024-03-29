from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
sys.path.append(".")
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from tests.conftest import  setup
from resources.locators import common_locators as cl
from resources.locators import navbar as nav
from resources.credentials import Constantinope as cndemo

class Task2(BasePage):
    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)
    
    def Idea_submission_under_Any_Campaign(self):
        wrap = self.Wrap
        wrap.wait_until_visibility_of_element_located(10, cl.community_name_header_xpath)
        wrap.wait_until_element_clickable(10, cl.campaign_submit_idea_xpath).click()
        wrap.wait_until_element_clickable(10, cl.idea_submit_campaign_field_xpath).click()
        time.sleep(5)
        wrap.wait_until_element_clickable(10 , cl.idea_submit_test_s4_xpath).click()
        time.sleep(5)
        
        #wrap.wait_until_element_clickable(10, '//*[@id="select2-idea-campaign-value-results"]/li[4]/ul/li[9]').click()
        wrap.wd_Send_keys_siimple(cl.idea_submit_title_xpath, cndemo.demo_text)
        wrap.wd_Send_keys_siimple(cl.idea_submit_description_xpath, cndemo.demo_text)
        wrap.scroll_to_specific_xpath(cl.idea_submit_submit_button_xpath)
        wrap.wait_until_element_clickable(10, cl.idea_submit_submit_button_xpath).click()
        elem = wrap.wait_until_visibility_of_element_located(10, cl.idea_submit_header_xpath)
        
        return elem.text