# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from dat.base_methods.base import BaseClass
from dat.main_page.main_page import MainPage
from dat.anonym_check.anonym import Anonym
from dat.base_methods.config import *

class TestSuite(unittest.TestCase, BaseClass, MainPage, Anonym):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def test_verify_main_page(self):
        self.open_url(BASE_URL, LIST_CAMPAIGN)

        self.assertTrue(self.check_main_page_elements(
            LOGO,
            AUTH_LINK,
            FEMALE_CATEGORY_MENU,
            LIST_CAMPAIGN))

        self.assertTrue(self.check_validation_reg(
            REG_LINK,
            REG_FORM,
            REG_EMAIL_INPUT,
            REG_PASS_INPUT,
            REG_BTN,
            REG_EMAIL_INPUT_ERROR,
            REG_PASS_INPUT_ERROR))


        self.assertTrue(self.check_validation_auth(
            AUTH_FORM,
            AUTH_EMAIL_INPUT,
            AUTH_PASS_INPUT,
            AUTH_BTN,
            AUTH_EMAIL_INPUT_ERROR, 
            AUTH_PASS_INPUT_ERROR))


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


    # def tearDown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()


