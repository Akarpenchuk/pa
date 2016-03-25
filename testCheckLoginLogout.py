# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from dat.base_methods.base import BaseClass
from dat.main_page.main_page import MainPage
from dat.base_methods.wait import Wait

from dat.main_page.main_page_elements import *
from dat.base_methods.config import *


class TestSuite(unittest.TestCase, BaseClass, Wait, MainPage):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)
        
    def testLoginLogout(self):
        '''check login and logout'''

        self.assertTrue(self.open_base_url())
        self.login_old_user()
        self.check_main_page_elements()
        self.logout()
        self.check_main_page_elements()

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()