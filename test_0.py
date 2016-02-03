# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from dat.base_methods.base import BaseClass
from dat.base_methods.base import Wait
from dat.base_methods.config import *


class TestCase(unittest.TestCase, BaseClass, Wait):

    def setUp(self):
        self.driver = webdriver.Chrome()
        BASE_URL = "https://modnakasta.ua"

    def testPlay(self):
        # result = self.open_url(BASE_URL, LIST_CAMPAIGN)
        # self.assertTrue(result, 'campaign is not displayed')
        # self.assertTrue(self.login(), 'login is failed')
        '''login() need to serios wait after login'''
        if self.login() != True:
            print False
        else:
            print True


    # def tearDown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()