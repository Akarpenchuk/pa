# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from selenium import webdriver
import unittest
from wait import Wait


class BaseClass(unittest.TestCase):

    def open_url(self, url, element):
        self.driver.get(url)
        self.wait_for_element_is_displayed(element)
        return True


    # def login(self, url, login, pass):
    #     open_url(url)

    #     wait
    #     verify element is displayed
    #     click
    #     wait
    #     send keys
    #     click
    #     send keys
    #     click
    #     wait element is displayed
    #     return

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
