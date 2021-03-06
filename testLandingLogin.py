# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from base_methods.wait import Wait
from base_methods.base import BaseClass
from landing_page.landing import Landing

import base_methods.config as conf
import landing_page.landing_elements as le


class Test(unittest.TestCase, Wait, BaseClass, Landing):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testLandingLogin(self):
        self.open_url(conf.LANDING_URL, le.AUTH_FORM)
        self.landing_login()
        self.logout()

    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    print "running"
    unittest.main()
