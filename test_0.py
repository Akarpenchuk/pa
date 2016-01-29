# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from dat.base_methods.base import KastaClass
from dat.base_methods.base import GoogleClass




class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testOpen(self):
        urlKasta = "https://modnakasta.ua"
        urlGoogle = "https://google.com"
        # KastaClass(webdriver).openKasta(urlKasta)
        # GoogleClass(webdriver).openGoogle(urlGoogle)

        KastaClass(self.driver).openKasta(urlKasta)
        GoogleClass(self.driver).openGoogle(urlGoogle)



if __name__ == "__main__":
    print 'running'
    unittest.main()

    
