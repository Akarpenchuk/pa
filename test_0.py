# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from dat.base_methods.base import BaseClass
from dat.base_methods.wait import Wait
from dat.config import *


class TestCase(BaseClass, Wait):

    BASE_URL = "https://modnakasta.ua"

    def testOpen(self):
        self.open_url(BASE_URL, LIST_CAMPAIGN_BANNER)


        
#EXAMPLE
# class Some(BaseClass):

#     def setUp(self):
#         self.shape = "123"
#         super(Some, self).setUp()


if __name__ == "__main__":
    print 'running'
    unittest.main()

    
