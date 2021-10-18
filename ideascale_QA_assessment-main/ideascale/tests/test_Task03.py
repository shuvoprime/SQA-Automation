import pytest
import sys
sys.path.append(".")
from pages.Task03 import Task3
from selenium import webdriver
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from pages.information import international_guidelines
from resources.credentials import Constantinope as cndemo

import time
import os

def test_submit_idea_in_any_campaign(setup):
    global drv
    drv = setup
    commobj = Task3(drv)
    elem = commobj.Idea_submission()
    assert elem == "test_s4"

def test_upvote():
    commobj = Task3(drv)
    elem = commobj.upvote()
    assert elem[0] == "1"
    assert elem[1] == "test_s4"

def test_tear_down(teardown):
    pass