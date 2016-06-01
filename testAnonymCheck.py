# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
import unittest

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

import dat.main_page.main_page_elements as mpe
import dat.base_methods.config as conf



class TestSuite(unittest.TestCase, BaseClass, MainPage, Anonym, Wait):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)


    def testAnonymChecking(self):

        self.open_url(conf.BASE_URL)

        # self.check_main_page_elements()

        # self.check_validation_reg()
        # self.check_validation_auth()

        # self.check_validation_recovery()

        # self.wait
        # self.check_help_menu_items()
        # self.check_main_menu_items()

        # self.anonym_buy_modnakarta()

        self.anonym_buy_product()

        self.check_soon_end_campaigns()
        self.check_coming_soon_campaigns()

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()


