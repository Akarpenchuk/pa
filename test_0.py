# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from dat.base_methods.isDisplayed import isDisplayed
from dat.base_methods.base import BaseClass
# from dat.base_methods.base import Wait
from dat.base_methods.config import *


class TestCase(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)
        BASE_URL = "https://modnakasta.ua"

    def testPlay(self):
        if self.open_url(BASE_URL, LIST_CAMPAIGN) == True:
            print 'OK'
        else:
            print 'NOK'
        # self.open_campaign()
        # self.logout()


    # def tearDown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()