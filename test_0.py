# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from dat.base_methods.base import BaseClass
from dat.base_methods.base import Wait
from dat.base_methods.config import *


class TestCase(BaseClass, Wait):

    def setUp(self):
        self.driver = webdriver.Chrome()
        BASE_URL = "https://modnakasta.ua"

    def testPlay(self):
        result = self.open_url(BASE_URL, LIST_CAMPAIGN)
        self.assertTrue(result, 'campaign is not displayed')

    def tearDown(self):
        self.driver.quit()



        
#EXAMPLE
# class Some(BaseClass):

#     def setUp(self):
#         self.shape = "123"
#         super(Some, self).setUp()


if __name__ == "__main__":
    print 'running'
    unittest.main()

    
