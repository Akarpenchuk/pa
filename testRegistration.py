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

from dat.main_page.main_page_elements import *
from dat.mail.mail_elements import *
from dat.base_methods.config import *

class TestSuite(unittest.TestCase, BaseClass, MainPage, Wait, Mail):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testRegistrations(self):

        # self.open_base_url()
        # self.send_registration_email()
        self.check_ragistration_email()
        # Registration(driver).fill_personal_info_popup()
        # PersonalInfo(driver).verify_user_email()


    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()
