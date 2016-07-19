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
from mail.mail import Mail
from cabinet.cabinet import Cabinet

import base_methods.config as conf
import landing_page.landing_elements as le
import mail.mail_elements as me
import cabinet.cabinet_elements as myinfo


class Test(unittest.TestCase, Wait, BaseClass, Landing, Mail, Cabinet):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testLandingRegistration(self):
        self.open_url(conf.LANDING_URL, le.AUTH_FORM)
        rand_email = self.landing_registration()
        self.check_registration_email(rand_email)
        self.fill_password_reset_popup(myinfo.USER_PASS)
        self.login(myinfo.USER_EMAIL, myinfo.USER_PASS)
        self.check_personal_data(myinfo.USER_EMAIL)
        self.logout()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()