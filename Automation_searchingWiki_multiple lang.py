from selenium import webdriver
from selenium.webdriver.common.by import By

# Import statements for explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

chromedriver = "/Users/shuvo/PycharmProjects/SQA_practice/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.wikipedia.org/")

# Define the wait variable for explicit wait.
wait_time = 5
wait = WebDriverWait(driver, wait_time)
driver.maximize_window()

# Define a list of locators for the language links.
language_locators = ["js-link-box-en", "js-link-box-ru", "js-link-box-de"]
search_locator = "searchInput"
search_text = "Software"

#looping through the languages
for i in range(len(language_locators)):
    language_link = wait.until(expected_conditions.presence_of_element_located((By.ID, language_locators[i])))
    language_link.click()

    input_box_element = wait.until(expected_conditions.presence_of_element_located((By.ID, search_locator)))
    input_box_element.send_keys(search_text)

    input_box_element.submit()

    # Pause the script for a few seconds.
    time.sleep(4)
    driver.back()
    driver.back()
# driver.quit()