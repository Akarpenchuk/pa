# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from selenium import webdriver
import unittest
from wait import Wait


class BaseClass(unittest.TestCase, Wait):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def open_url(self, url, element):
        self.driver.get(url)
        self.element_is_displayed(element)
        # self.element_is_displayed(LIST_CAMPAIGN) if element_is_displayed(LIST_CAMPAIGN) == True else False

    
    def verify(self):
    	self.element_is_displayed(LIST_CAMPAIGN) if element_is_displayed(LIST_CAMPAIGN) == True else False