import pytest
import sys
sys.path.append(".")
from pages.Task04 import Task4
from selenium import webdriver
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from resources.credentials import Constantinope as cndemo

import time
import os

def test_submit_idea_in_any_campaign(setup):
    global drv
    drv = setup
    commobj = Task4(drv)
    elem = commobj.idea_submission_and_comment()
    assert elem == "test_s4"

def test_idea_comment():
    commobj = Task4(drv)
    elem = commobj.idea_comment()
    assert elem == True

def test_tear_down(teardown):
    pass    