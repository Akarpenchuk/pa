# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep

class Wait:

    def __init__(self):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def wait_element(self, element):
        if self.wait.until(lambda self: self.find_element_by_xpath(element)):
            return True
        return False, TimeoutException

    def wait_element_displayed_by_id(self, element):
        if self.wait.until(lambda self: self.find_element_by_id(element)):
            return True
        return False, TimeoutException

    def wait_element_displayed_by_class_name(self, element):
        if self.wait.until(lambda self: self.find_element_by_class_name(element)):
            return True
        return False, TimeoutException

    def wait_element_displayed_by_link_text(self, element):
        if self.wait.until(lambda self: self.find_element_by_link_text(element)):
            return True
        return False, TimeoutException

    def wait_and_check(self, element):
        count = 0
        sleep(2)
        while count < 20:
            print 'wait_and_check: wait email ', count
            try:
                self.wait_element(element)
                break
                print 'wait_and_check: email %s found' % element
            except:
                count += 1
                self.driver.refresh()
                continue

    # def switch_to_new_window(self):
    #     self.wait.until(lambda self: len(self.window_handles) == 2)
    #     self.driver.switch_to.window(1)