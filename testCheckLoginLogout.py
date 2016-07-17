# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

import unittest
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from base_methods.base import BaseClass
from main_page.main_page import MainPage
from base_methods.wait import Wait


import main_page.main_page_elements as mpe
import cabinet.cabinet_elements as myinfo


class TestSuite(unittest.TestCase, BaseClass, Wait, MainPage):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)
        
    def testLoginLogout(self):
        self.open_main_page()
        self.login(myinfo.USER_EMAIL, myinfo.USER_PASS)
        self.check_main_page_elements()
        self.logout()
        self.check_main_page_elements()

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()