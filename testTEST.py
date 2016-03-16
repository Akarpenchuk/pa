#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os, sys
sys.path.append('/home/ace/Documents/git/autotests/dat')

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from dat.base_methods.base import BaseClass
import dat.main_page.main_page_elements as mpe

class Test(unittest.TestCase, BaseClass):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

    def test_case(self):

        self.open_url_css("http://staging.modnakasta.ua", "css=header-top_logo:contains('img/logo.svg')")
            # :contains('http://m.cdnmk.net/site_media/frontend/assets/staging/blocks/b-header/img/logo.svg')")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()