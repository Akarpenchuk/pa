# !/usr/bin/env/ python
# -*- coding: utf-8 -*-
from ..config import *
from selenium import webdriver
from selenium.webdriver.support import wait
from base import BaseClass

class Wait(BaseClass):

	def wait_for_element_is_displayed(self, element):
		driver.find_elements_by_xpath(element)
