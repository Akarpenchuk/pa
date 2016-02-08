# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from dat.base_methods.base import BaseClass
from dat.base_methods.config import *


class TestCase(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def testPlay(self):
        # self.assertTrue (self.open_url(BASE_URL, LIST_CAMPAIGN), 'campaign is not find')
        self.assertTrue (self.login(), 'login false')
        self.assertTrue (self.elements_count(LIST_CAMPAIGN), 'campaigns is < 50')
        self.assertTrue (self.logout(), 'logout false')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()