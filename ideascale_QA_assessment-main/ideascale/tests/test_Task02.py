import pytest
import sys
sys.path.append(".")
from pages.Task02 import Task2
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
    commobj = Task2(drv)
    elem = commobj.Idea_submission_under_Any_Campaign()
    assert elem == "test_s4"

def test_tear_down(teardown):
    pass