# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from dat.base_methods.base import BaseClass
# from dat.base_methods.base import Wait
from dat.base_methods.config import *


class TestCase(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        BASE_URL = "https://modnakasta.ua"

    def testPlay(self):
        self.login()
        self.open_main_page(BASE_URL, LIST_CAMPAIGN)
        self.open_campaign()
        self.logout()


    # def tearDown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()