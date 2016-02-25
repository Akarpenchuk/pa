# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import main_page.main_page_elements as mpe
import landing_page.landing_elements as le
import mail.mail_elements as me
import base_methods.config as conf

class Landing:

	def landing_login(self):
		self.driver.find_element_by_xpath(le.AUTH_LINK).click()
		# self.wait_element_displayed_by_xpath(le.AUTH_EMAIL_INPUT)
		sleep(1)
		self.driver.find_element_by_xpath(le.AUTH_EMAIL_INPUT).clear()
		self.driver.find_element_by_xpath(le.AUTH_EMAIL_INPUT).send_keys(conf.USER_EMAIL)
		self.driver.find_element_by_xpath(le.AUTH_PASS_INPUT).clear()
		self.driver.find_element_by_xpath(le.AUTH_PASS_INPUT).send_keys(conf.USER_PASS)
		self.driver.find_element_by_xpath(le.AUTH_BTN).click()
		if self.wait_element_displayed_by_xpath(mpe.LIST_CAMPAIGN):
			return True
		return False
