from pages.adding_user import adding_users
import pytest
import sys
sys.path.append(".")

from selenium import webdriver
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from resources.credentials import Constantinope as cndemo

import time
import os

def test_addinguser1(setup):
    global drv
    drv = setup
    commobj = adding_users(drv)
    elem = commobj.adding_user_1()
    elem[0] == True
    elem[1] == True

def test_adding_user_2(setup):
    drv = setup
    commobj = adding_users(drv)
    elem = commobj.adding_user_2()
    elem[0] == True
    elem[1] == True


def test_tear_down(teardown):
    pass