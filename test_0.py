# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from dat.base_methods.base import BaseMethods
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest

class TestCase(unittest.TestCase, BaseMethods):

    global driver
    driver = webdriver.Chrome()

    
    def test_case(self):

        url = "https://modnakasta.ua"
        openUrl(url)
    
    #it works, but its not function(
    # driver.get(url)




if __name__ == "__main__":
    print 'running'
    unittest.main()

    
