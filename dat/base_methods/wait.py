# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from isDisplayed import isDisplayed
from selenium.webdriver.support import expected_conditions as EC


class Wait:

    def wait_element_displayed_by_xpath(self, element):
        if self.wait.until(lambda self: self.find_element_by_xpath(element)):
            return True
        return False

        # if self.wait.until(lambda self: self.find_element_by_xpath(element).is_displayed()):
        #     return True
        # else:
        #     return False
        
        # if wait.until(element_displayed_by_xpath(element)) != True:
        #     return False

    # def wait_element_displayed_by_id(self, element):
    #     try:
    #         self.wait.until(element_displayed_by_id(element))
    #         return True
    #     except:
    #         return False

    # def wait_element_displayed_by_class_name(self, element):
    #     try:
    #         self.wait.until(element_displayed_by_class_name(element))
    #         return True
    #     except:
    #         return False

    # def wait_element_displayed_by_link_text(self, element):
    #     try:
    #         self.wait.until(element_displayed_by_link_text(element))
    #         return True
    #     except:
    #         return False
