# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from config import *
from selenium import webdriver
import unittest
from wait import Wait
from clickandfill import Clicking
from clickandfill import Filling
from hover import Action


class BaseClass(Wait, Clicking, Filling, Action):

    # def __init__(self):
        # self.wait = WebDriverWait(self.driver, 5)

    def open_url(self, url, element):
        self.driver.get(url)
        if self.wait_element_displayed_by_xpath(element):
            return True
        return False



    def login(self):
        self.driver.get(BASE_URL)
        self.wait_element_displayed_by_xpath(AUTH_LINK)
        self.click_by_xpath(AUTH_LINK)
        self.wait_element_displayed_by_xpath(AUTH_FORM)
        self.click_by_xpath(AUTH_EMAIL_INPUT)
        self.filling_field_by_xpath(AUTH_EMAIL_INPUT, USER_EMAIL)
        self.click_by_xpath(REG_EMAIL_INPUT)
        self.filling_field_by_xpath(REG_EMAIL_INPUT, USER_PASS)
        self.click_by_xpath(LOGIN_BTN)
        if self.wait_element_displayed_by_xpath(PROFILE_LINK):
            return True
        return False

    def logout(self):
        self.element_displayed_by_xpath(PROFILE_LINK)
        self.hover_and_click(PROFILE_LINK, LOGOUT_LINK)
        # self.click_by_xpath(LOGOUT_LINK)
        if self.wait_element_displayed_by_xpath(AUTH_LINK):
            return True
        return False

    def refresh(self):
        self.driver.refresh()

    def store_elements_count(self, element):
        elements = self.driver.find_elements_by_xpath(element)
        if elements:
            return elements

