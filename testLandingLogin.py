# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from base_methods.base import BaseClass
from dat.landing_page.landing import Landing

import dat.base_methods.config as conf
import dat.landing_page.landing_elements as le


class Test(unittest.TestCase, BaseClass, Landing):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)


    def testLandingLogin(self):

        self.assertTrue(self.open_url("https://modnakasta.ua/landing/nike", le.AUTH_FORM))
        self.assertTrue(self.landing_login())
        self.assertTrue(self.logout())


    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    print "running"
    unittest.main()
