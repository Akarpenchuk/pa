# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



class Action:

    def hover(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(element))
        actions.perform()

    def hover_and_click(self, hover, click):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(hover))
        actions.click(self.driver.find_element_by_xpath(click))
        actions.perform()