# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from selenium import webdriver
import unittest
from wait import Wait
from clickandfill import Clicking
from clickandfill import Filling


class BaseClass(Wait, Clicking, Filling):

    def open_url(self, url, element):
        self.driver.get(url)
        if self.wait_element_displayed_by_xpath(element) != True:
            return False
        return True


    def login(self):
        self.open_url(BASE_URL, LIST_CAMPAIGN)
        self.click_by_xpath(AUTH_LINK)
        self.wait_element_displayed_by_xpath(AUTH_FORM)
        self.click_by_xpath(AUTH_EMAIL_INPUT)
        self.filling_field_by_xpath(AUTH_EMAIL_INPUT, USER_EMAIL)
        self.click_by_xpath(REG_EMAIL_INPUT)
        self.filling_field_by_xpath(REG_EMAIL_INPUT, USER_PASS)
        self.click_by_xpath(LOGIN_BTN)
        result = self.wait_element_displayed_by_xpath(LIST_CAMPAIGN)
        if result != True:
            return False
        return True

    # def logout(pass):
    #     verify element is displayed
    #     hover
    #     click
    #     wait element is displayed
    #     return

    # def refresh(self):
    #     pass

    def store_elements_count(self, element):
        elem_count = count(self.driver.find_elements_by_xpath(element))
        return int(elem_count)
