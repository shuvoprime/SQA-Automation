from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait

def fb_login():
driver.get ("https://www.facebook.com")

driver.find_element_by_id("email")
driver.find_element_by_id.send_keys("fakeemail@crossbrowsertesting.com')
sleep(2)

driver.find_element_by_id("pass").send_keys("fakepassword1")
sleep(2)

driver.find_element_by_id("loginbutton").click()

WebDriverWait(driver, 10).until(EC.title_contains("home"))