# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from isDisplayed import isDisplayed


class Wait:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_element_displayed_by_xpath(self, element):
        try:
            self.wait.until(lambda self: element_displayed_by_xpath(element))
            return True
        except:
            return False

    def wait_element_displayed_by_id(self, element):
        try:
            self.wait.until(element_displayed_by_id(element))
            return True
        except:
            return False

    def wait_element_displayed_by_class_name(self, element):
        try:
            self.wait.until(element_displayed_by_class_name(element))
            return True
        except:
            return False

    def wait_element_displayed_by_link_text(self, element):
        try:
            self.wait.until(element_displayed_by_link_text(element))
            return True
        except:
            return False
