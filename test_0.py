# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from dat.base_methods.base import BaseClass
from dat.config import *

main_page = "https://modnakasta.ua"


class TestCase(BaseClass):

    def testOpen(self):
        self.open_url(main_page)

        
#EXAMPLE
# class Some(BaseClass):

#     def setUp(self):
#         self.shape = "123"
#         super(Some, self).setUp()


if __name__ == "__main__":
    print 'running'
    unittest.main()

    
