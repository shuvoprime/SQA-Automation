from pages.visiting_url import HomePage
import pytest
import sys
sys.path.append(".")

from selenium import webdriver
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from resources.credentials import Constantinope as cndemo

import time
import os

def test_page_notification(setup):
    global drv
    drv = setup
    commobj = HomePage(drv)
    elem = commobj.call_us_now()
    elem == True

def test_cart_visibility():
    commobj = HomePage(drv)
    elem = commobj.cart_visibility()
    elem == True

def test_vissibility_of_component():
    commobj = HomePage(drv)
    elem = commobj.visibility_of_compoment()
    elem[0] == True
    elem[1] == True
    elem[2] == True

def test_tear_down(teardown):
    pass