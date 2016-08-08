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

import cabinet.cabinet_elements as myinfo
import base_methods.config as conf

class TestSuite(unittest.TestCase, BaseClass, MainPage, Wait, Mail, Cabinet):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testRecovery(self):
        self.clear_mailbox(myinfo.TEST_EMAIL)
        self.open_main_page()
        self.send_recovery_email(myinfo.TEST_EMAIL)
        self.check_recovery_email(myinfo.TEST_EMAIL)
        self.fill_password_reset_popup(myinfo.USER_PASS)
        self.fill_password_reset_login_popup(myinfo.TEST_EMAIL, myinfo.USER_PASS)
        self.logout()

        # query = "select is_active from auth_user where email='testemail@mailinator.com';"
        # result = self.db_select(query)
        # print 'result ', result
        # assert 'True' in result

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()