# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep

import unittest
from selenium import webdriver
from base_methods.wait import Wait

import cabinet.cabinet_elements as myinfo
import main_page.main_page_elements as mpe
import base_methods.config as conf


class BaseClass(Wait):

    def open_base_url(self):
        self.driver.get(conf.BASE_URL)
        if self.check_main_page_elements():
            return True
        return False


    def open_url(self, url, element):
        self.driver.get(url)
        if self.wait_element_displayed_by_xpath(element):
            return True
        return False


    def open_url_css(self, url, element):
        self.driver.get(url)
        if self.driver.find_element_by_css_selector(element):
            return True
        return False


    def registration_set_pass_and_login(self):
        self.driver.find_element_by_xpath(myinfo.NEW_PASSWORD).send_keys(conf.USER_PASS)
        self.driver.find_element_by_xpath(myinfo.NEW_PASSWORD_AGAIN).send_keys(conf.USER_PASS)
        self.driver.find_element_by_xpath(myinfo.SAVE).click()
        self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)

        self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT).send_keys(conf.RAND_EMAIL)
        self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT).send_keys(conf.USER_PASS)
        self.driver.find_element_by_xpath(mpe.AUTH_BTN).click()
        if self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU):
            return True
        return False


    def recovery_set_pass_and_login(self):
        self.driver.find_element_by_xpath(myinfo.NEW_PASSWORD).send_keys(conf.USER_PASS)
        self.driver.find_element_by_xpath(myinfo.NEW_PASSWORD_AGAIN).send_keys(conf.USER_PASS)
        self.driver.find_element_by_xpath(myinfo.SAVE).click()
        self.wait_element_displayed_by_xpath(myinfo.RECOVERY_AUTH_EMAIL)

        self.driver.find_element_by_xpath(myinfo.RECOVERY_AUTH_EMAIL).send_keys(conf.USER_EMAIL)
        self.driver.find_element_by_xpath(myinfo.RECOVERY_AUTH_PASS).send_keys(conf.USER_PASS)
        self.driver.find_element_by_xpath(myinfo.SAVE).click()
        if self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU):
            return True
        return False


    def login_new_user(self):
        try:
            self.driver.find_element_by_xpath(mpe.AUTH_LINK).click()
            self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)
            self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT).send_keys(conf.RAND_EMAIL)
            self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT).send_keys(conf.USER_PASS)
            self.driver.find_element_by_xpath(mpe.AUTH_BTN).click()
            if self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU):
                return True
            return False
        except:
            self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)
            self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT).send_keys(conf.RAND_EMAIL)
            self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT).send_keys(conf.USER_PASS)
            self.driver.find_element_by_xpath(mpe.AUTH_BTN).click()
            if self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU):
                return True
            return False


    def login_old_user(self):
        try:
            self.driver.find_element_by_xpath(mpe.AUTH_LINK).click()
            self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)
            self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT).send_keys(conf.USER_EMAIL)
            self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT).send_keys(conf.USER_PASS)
            self.driver.find_element_by_xpath(mpe.AUTH_BTN).click()
            if self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU):
                return True
            return False
        except:
            self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)
            self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT).send_keys(conf.USER_EMAIL)
            self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT).send_keys(conf.USER_PASS)
            self.driver.find_element_by_xpath(mpe.AUTH_BTN).click()
            if self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU):
                return True
            return False

    def logout(self):
        self.driver.find_element_by_xpath(myinfo.PROFILE_MENU).click()
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


    def switch_to_frame(self, frame):

        inbox = self.driver.find_element_by_xpath(frame)
        self.driver.switch_to.frame(inbox)