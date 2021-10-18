from pages.adding_items_cart import cart
import pytest
import sys
sys.path.append(".")

from selenium import webdriver
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from resources.credentials import Constantinope as cndemo

import time
import os

def test_addtocart(setup):
    global drv
    drv = setup
    commobj = cart(drv)
    elem = commobj.cart_add()
    elem == True

def test_tear_down(teardown):
    pass
