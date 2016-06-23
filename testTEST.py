# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
import unittest
import logging
logging.basicConfig(filename = '/home/ace/log_webdriver', level = logging.DEBUG)

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from base_methods.base import BaseClass
from main_page.main_page import MainPage
from base_methods.wait import Wait
from campaign.campaign import Campaign

import campaign.campaign_elements as ce
import main_page.main_page_elements as mpe


class Test(unittest.TestCase, BaseClass, MainPage, Wait, Campaign):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        chromeOptions.add_argument("--keep-alive-for-test")
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

    def testCampName(self):
        self.text = 'IKEA'
        return self.text

    def testBasket(self, text):
        self.open_main_page()
        self.find_text(mpe.CAMPAIGN_NAME, text)

    # def tearDown(self):
        # self.driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()