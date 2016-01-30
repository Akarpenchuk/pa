# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from dat.base_methods.base import BaseClass


BASE_URL = "https://modnakasta.ua"
# element = "https://media.modnakasta.ua/site_media/frontend/assets/15w53r17/blocks/b-logo/img/logo.png"

class TestCase(BaseClass):

    def testOpen(self):
        # try:
        assert self.open_url(BASE_URL) == True

        # except Exception, e:
        #     print e 


        
#EXAMPLE
# class Some(BaseClass):

#     def setUp(self):
#         self.shape = "123"
#         super(Some, self).setUp()


if __name__ == "__main__":
    print 'running'
    unittest.main()

    
