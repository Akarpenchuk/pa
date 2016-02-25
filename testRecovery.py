# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from dat.base_methods.base import BaseClass
from dat.main_page.main_page import MainPage
from dat.mail.mail import Mail
from dat.base_methods.wait import Wait
from dat.cabinet.cabinet import PersonalInfo

from dat.main_page.main_page_elements import *
from dat.mail.mail_elements import *
import base_methods.config as conf

class TestSuite(unittest.TestCase, BaseClass, MainPage, Wait, Mail, PersonalInfo):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testRecovery(self):

        self.assertTrue(self.open_base_url())
        self.assertTrue(self.send_recovery_email())
        self.assertTrue(self.check_recovery_email())
        
        # self.assertTrue(self.create_new_password_and_login())

        # self.assertTrue(self.logout())
        # self.assertTrue(self.login(conf.USER_EMAIL))

    # def tearDown(self):

    #     self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()
