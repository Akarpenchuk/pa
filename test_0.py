# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from dat.base_methods.base import KastaClass
from dat.base_methods.base import GoogleClass, BaseClass


urlKasta = "https://modnakasta.ua"
urlGoogle = "https://google.com"

class TestCase(BaseClass):

    def testOpen(self):

        # KastaClass(webdriver).openKasta(urlKasta)
        # GoogleClass(webdriver).openGoogle(urlGoogle)

        self.url_open(urlKasta)
        self.url_open(urlGoogle)
        #KastaClass(self.driver).openKasta(urlKasta)
        #GoogleClass(self.driver).openGoogle(urlGoogle)


class Some(BaseClass):

    def setUp(self):
        self.shape = "123"
        super(Some, self).setUp()


if __name__ == "__main__":
    print 'running'
    unittest.main()

    
