# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import logging
logging.basicConfig(filename = '/home/ace/log_webdriver', level = logging.DEBUG)

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from dat.base_methods.base import BaseClass
from dat.main_page.main_page import MainPage
from dat.mail.mail import Mail
from dat.base_methods.wait import Wait
from dat.cabinet.cabinet import Cabinet

class TestSuite(unittest.TestCase, BaseClass, MainPage, Wait, Mail, Cabinet):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def testRegistration(self):

        self.assertTrue(self.open_base_url())
        self.assertTrue(self.send_registration_email())
        self.assertTrue(self.check_registration_email())
        self.assertTrue(self.fill_personal_data_popup())    
        self.assertTrue(self.open_personal_cabinet())
        self.assertTrue(self.check_personal_data())
        self.assertTrue(self.logout())
        self.assertTrue(self.login(conf.RAND_EMAIL))

    # def tearDown(self):

    #     self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()
