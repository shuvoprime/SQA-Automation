import pytest
import sys
sys.path.append(".")
from pages.Task_01 import Task1
from selenium import webdriver
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from pages.information import international_guidelines
from resources.credentials import Constantinope as cndemo

import time
import os


def test_community_settings_checklist_page_open(setup):
    global drv
    drv = setup
    commobj = Task1(drv)
    elem = commobj.campaign_settings_page_redirected()
    assert elem == "Checklist"

def test_campaign_create():
    commobj = Task1(drv)
    elem = commobj.campaign_create()
    assert elem == "IS-QA\nIdeas"

def test_submit_idea():
    commobj = Task1(drv)
    elem = commobj.submit_idea()
    assert elem == "test_s4"
    

def test_tear_down(teardown):
    pass