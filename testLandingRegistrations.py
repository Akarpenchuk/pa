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
from dat.mail.mail import Mail
from dat.cabinet.cabinet import Cabinet

import dat.base_methods.config as conf
import dat.landing_page.landing_elements as le
import dat.mail.mail_elements as me


class Test(unittest.TestCase, BaseClass, Landing, Mail, Cabinet):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)


    def testLandingRegistration(self):

        self.assertTrue(self.open_url("https://modnakasta.ua/landing/nike", le.AUTH_FORM))
        self.landing_registration()
        self.assertTrue(self.check_registration_email())
        self.assertTrue(self.registration_set_pass_and_login())
        self.assertTrue(self.logout())


    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()