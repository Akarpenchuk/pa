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

from base_methods.wait import Wait
from base_methods.base import BaseClass
from main_page.main_page import MainPage
from campaign.campaign import Campaign

class Test(unittest.TestCase, BaseClass, MainPage, Campaign, Wait):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testCatalogueDetails(self):
        self.open_main_page()
        self.open_rand_campaign()
        self.affiliation_apply()

    def tearDown(self):
        self.driver.quit()
     


if __name__ == "__main__":
    print 'running'
    unittest.main()
