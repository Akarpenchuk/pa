# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
from isDisplayed import isDisplayed


class Clicking(isDisplayed):

    def __init__(self, driver):
        self.driver = driver

    def click_by_xpath(self, element):
        self.driver.find_element_by_xpath(element).click()

    def click_by_id(self, element):
        self.driver.find_element_by_id(element).click()

    def click_by_class_name(self, element):
        self.driver.find_element_by_class_name(element).click()

    def click_by_link_text(self, element):
        self.driver.find_element_by_link_text(element).click()


class Filling:

    def __init__(self, driver):
        self.driver = driver

    def clear_field(self, element):
        self.driver.find_element_by_xpath(element).clear()

    def filling_field_by_xpath(self, element, value):
        self.driver.find_element_by_xpath(element).send_keys(value)