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

class Test(unittest.TestCase):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    # @decorator

    def testCategory(self):
        self.open_main_page()
        self.open_campaign_iter()
        self.check_first_category()
        self.check_last_category()
        self.uncheck_first_category()
    def testBrand(self):
        pass
    def testSize(self):
        pass
    def testPrice(self):
        pass
    def testColor(self):
        pass

    def tearDown(self):
        self.driver.quit()
     


if __name__ == "__main__":
    print 'running'
    unittest.main()
