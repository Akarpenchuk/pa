# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from dat.base_methods.base import BaseClass
from selenium.webdriver.common.by import By
from dat.base_methods.config import *


class TestCase(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

    def testPlay(self):
        # self.assertTrue (self.login(), 'login false')
        self.open_url(BASE_URL, LIST_CAMPAIGN)
        campaigns_count = self.store_elements_count(LIST_CAMPAIGN)
        if campaigns_count < 50:
            raise Exception, "Not enought campaigns"
        # self.assertTrue (self.logout(), 'logout is false')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()