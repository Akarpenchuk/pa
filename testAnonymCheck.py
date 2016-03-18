# !/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from dat.base_methods.base import BaseClass
from dat.main_page.main_page import MainPage
from dat.anonym_check.anonym import Anonym
from dat.base_methods.wait import Wait

from dat.main_page.main_page_elements import *
from dat.base_methods.config import *



class TestSuite(unittest.TestCase, BaseClass, MainPage, Anonym, Wait):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)


    def testAnonymChecking(self):
        '''check common functional by anonym'''

        self.assertTrue(self.open_base_url())

        self.assertTrue(self.check_main_page_elements())

        self.assertTrue(self.check_validation_reg())
        self.assertTrue(self.check_validation_auth())

        self.assertTrue(self.check_validation_recovery())

        self.assertTrue(self.check_help_menu_items())
        self.assertTrue(self.check_main_menu_items())

        self.assertTrue(self.anonym_buy_modnakarta())

        self.assertTrue(self.anonym_buy_product())

        # self.assertTrue(self.check_soon_end_campaigns())
        # self.assertTrue(self.check_coming_soon_campaigns())

        # self.assertTrue(self.check_fast_access_buttons())

    # def tearDown(self):

    #     self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()


