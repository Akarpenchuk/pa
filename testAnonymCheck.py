# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from dat.base_methods.base import BaseClass
from dat.main_page.main_page import MainPage
from dat.anonym_check.anonym import Anonym
from dat.base_methods.wait import Wait
from dat.main_page.main_page_elements import *
from dat.base_methods.config import *
from time import sleep


class TestSuite(unittest.TestCase, BaseClass, MainPage, Anonym, Wait):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)


    def test_verify_main_page(self):
        self.open_base_url()

        # self.assertTrue(self.check_main_page_elements())

        # self.assertTrue(self.check_validation_reg())

        # self.assertTrue(self.check_validation_auth())

        # self.assertTrue(self.check_validation_recovery())

        # self.assertTrue(self.check_help_menu_items())
        
        # self.assertTrue(self.check_main_menu_items())

        self.assertTrue(self.anonym_buy_modnakarta())
        
        """verify campaign length"""
        # self.elements_count(CURRENT_CAMPAIGNS)


        # self.elements_count(SOON_END_CAMPAIGNS)
        # self.elements_count(COMING_SOON)

        # self.verify_fast_access_buttons()


    # def tearDown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()


