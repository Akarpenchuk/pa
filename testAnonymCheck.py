# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from dat.base_methods.base import BaseClass
from dat.main_page.main_page import MainPage
from dat.base_methods.base import clickandfill
from dat.base_methods.config import *

class TestSuite(unittest.TestCase, BaseClass, MainPage):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def test_verify_main_page(self):
        self.open_url(BASE_URL, LIST_CAMPAIGN)
        print self.check_main_page_elements(LOGO, AUTH_LINK, FEMALE_CATEGORY_MENU, LIST_CAMPAIGN)
        # self.check_header_elements(FEMALE_CATEGORY_MENU)
        self.check_validation_reg()
        Anonym(driver).anonym_verify_auth()
        Anonym(driver).anonym_verify_recovery()

        Menu(driver).verify_help_menu()
        
        Menu(driver).verify_main_menu()
        
        Anonym(driver).anonym_buy_modnakarta()
        
        self.elements_count(CURRENT_CAMPAIGNS)
        self.element_displayed_by_xpath(BANNER_MOB_SHOPPING)
        self.element_displayed_by_xpath(BANNER_HOW_IT_WORKS)


        self.elements_count(SOON_END_CAMPAIGNS)
        self.elements_count(COMING_SOON)

        self.verify_fast_access_buttons()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()


