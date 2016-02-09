# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from hover import Action
from wait import Wait
from config import *

# from .campaign.campaign import Campaign


class BaseClass(Wait, Action):

    def open_url(self, url, element, **args):
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
        if self.wait_element_displayed_by_xpath(AUTH_LINK):
            return True
        return False

    def refresh(self):
        self.driver.refresh()

    def elements_count(self, element):
        elements = self.driver.find_elements_by_xpath(element)
        return len(elements)






