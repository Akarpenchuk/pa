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
        # self.assertTrue (self.open_url(BASE_URL, LIST_CAMPAIGN), 'campaign is not find')
        self.assertTrue (self.login(), 'login false')
        self.assertTrue (self.logout(), 'logout is false')

        #Traceback (most recent call last):
#   File "/home/ace/Documents/git/autotests/test_0.py", line 23, in testPlay
#     self.assertTrue (self.logout(), 'logout is false')
#   File "/home/ace/Documents/git/autotests/dat/base_methods/base.py", line 44, in logout
#     if self.wait_element_displayed_by_xpath(AUTH_LINK):
#   File "/home/ace/Documents/git/autotests/dat/base_methods/wait.py", line 16, in wait_element_displayed_by_xpath
#     if self.wait.until(lambda self: self.find_element_by_xpath(element)):
#   File "/usr/local/lib/python2.7/dist-packages/selenium/webdriver/support/wait.py", line 75, in until
#     raise TimeoutException(message, screen, stacktrace)
# TimeoutException: Message: 

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()