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
from mail.mail import Mail
from base_methods.wait import Wait
from cabinet.cabinet import Cabinet

import base_methods.config as conf

class TestSuite(unittest.TestCase, BaseClass, MainPage, Wait, Mail, Cabinet):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testRecovery(self):

        self.assertTrue(self.open_base_url())
        self.assertTrue(self.send_recovery_email())
        self.assertTrue(self.check_recovery_email())
        
        self.recovery_set_pass_and_login()
        self.assertTrue(self.logout())

    # def tearDown(self):

        # self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()
