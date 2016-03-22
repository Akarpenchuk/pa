# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from hover import Action
from base_methods.wait import Wait
import main_page.main_page_elements as mpe
from config import *


class BaseClass(Wait, Action):

    def open_base_url(self):

        self.driver.get(BASE_URL)
        if self.check_main_page_elements():
            return True
        return False

    def open_url(self, url, element):

        self.driver.get(url)
        if self.driver.find_elements_by_xpath(element):
            return True
        return False

    def open_url_css(self, url, element):

        self.driver.get(url)
        if self.driver.find_element_by_css_selector(element):
            return True
        return False

    def login(self, email):

        auth_link = self.driver.find_element_by_xpath(mpe.AUTH_LINK)
        auth_link.click()
        self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)
        self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT).send_keys(email)
        self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT).send_keys(USER_PASS)
        self.driver.find_element_by_xpath(mpe.AUTH_BTN).click()
        if self.wait_element_displayed_by_xpath(mpe.PROFILE_LINK):
            return True
        return False

    def logout(self):

        self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU)
        self.driver.find_element_by_xpath(mpe.PROFILE_MENU).click()
        self.wait_element_displayed_by_xpath(mpe.LOGOUT_LINK)
        self.driver.find_element_by_xpath(mpe.LOGOUT_LINK).click()
        if self.wait_element_displayed_by_xpath(mpe.AUTH_LINK):
            return True
        return False

    def refresh(self):

        self.driver.refresh()

    def elements_count(self, element):

        elements = self.driver.find_elements_by_xpath(element)
        return len(elements)

    def switch_to_iframe(self, iframe):

        inbox = self.driver.find_element_by_xpath(iframe)
        self.driver.switch_to.frame(inbox)






