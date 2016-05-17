# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from base_methods.wait import Wait
from main_page.main_page import MainPage
from selenium.webdriver.common.keys import Keys

import campaign.campaign_elements as ce
import cabinet.cabinet_elements as myinfo
import main_page.main_page_elements as mpe
import base_methods.config as conf



class BaseClass():

    def find(self, item):
        self.driver.find_element_by_xpath(item)

    def find_text(self, items):
        element_text = self.driver.find_element_by_xpath(items).text
        return element_text

    def find_elements(self, items):
        elements = self.driver.find_elements_by_xpath(items)
        return elements

    def click(self, item):
        self.driver.find_element_by_xpath(item).click()

    def send_keys(self, item, data):
        self.driver.find_element_by_xpath(item).send_keys(data)

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def count_elements(self, element):
        elements = self.driver.find_elements_by_xpath(element)
        return len(elements)

    def switch_to_frame(self, frame):
        inbox = self.find(frame)
        self.driver.switch_to.frame(inbox)

    def scroll_down(self, element):
        self.driver.find_element_by_xpath(element).send_keys(Keys.PAGE_DOWN)

    def scroll_to_element(self):
        while not self.find(ce.LAST_PRODUCT):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);");
            self.wait_element(ce.PRODUCT)