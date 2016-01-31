# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support import wait

class Wait:

    def __init__(self, driver):
        self.driver = driver

    def element_is_displayed(self, element):
        try:
            self.driver.find_elements_by_xpath(element)
            print element
        except:
            return False
        # print element
