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
from mail.mail import Mail
from base_methods.wait import Wait
from cabinet.cabinet import Cabinet
import cabinet.cabinet_elements as myinfo
import base_methods.config as conf

class TestSuite(unittest.TestCase, BaseClass, MainPage, Wait, Mail, Cabinet):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testRegistration(self):
        self.open_main_page()
        rand_email = self.send_registration_email()
        self.check_registration_email(rand_email)
        self.fill_personal_data_popup()
        self.open_cabinet()
        self.check_personal_data()
        self.logout_cabinet()
        self.login(rand_email, myinfo.USER_PASS)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()
