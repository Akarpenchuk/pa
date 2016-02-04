# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium import webdriver

class isDisplayed:
    
    def __init__(self):
        self.driver = driver

    def element_displayed_by_xpath(self, element):
        if self.driver.find_element(By.XPATH, element).is_displayed():
            return True

    def element_displayed_by_id(self, element):
        if self.driver.find_element(By.ID, element).is_displayed():
            return True

    def element_displayed_by_class_name(self, element):
        if self.driver.find_element(By.CLASS_NAME, element).is_displayed():
            return True

    def element_displayed_by_link_text(self, element):
        if self.driver.find_element(By.LINK_TEXT, element).is_displayed():
            return True
