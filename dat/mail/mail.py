# !/usr/bin/env python 
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


import mail_elements as me
import main_page.main_page_elements as mpe
import base_methods.config as conf

class Mail:
    """check emails"""

    def __init__(self):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def check_registration_email(self):

        self.open_url("http://mailinator.com/inbox.jsp?to=" + conf.RAND_NAME, me.EMAIL_INPUT)

        self.wait_with_check(me.EMAIL_SELECT_LETTER)
        self.driver.find_element_by_xpath(me.EMAIL_SELECT_LETTER).click()
        self.wait_element_displayed_by_xpath(me.SELECT_REG_BTN)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(me.SELECT_REG_BTN))      
        self.driver.find_element_by_xpath(me.EMAIL_REG_BTN).click()

        sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP)
        return True

    def check_recovery_email(self):
        self.open_url("http://mailinator.com/inbox.jsp?to=" + conf.USER_NAME, me.EMAIL_INPUT)

        self.wait_with_check(me.EMAIL_SELECT_LETTER)
        self.driver.find_element_by_xpath(me.EMAIL_SELECT_LETTER).click()
        self.wait_element_displayed_by_xpath(me.SELECT_RECOVERY_LINK)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(me.SELECT_RECOVERY_LINK))      
        self.driver.find_element_by_xpath(me.EMAIL_REG_BTN).click()

        sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.driver.find_element_by_xpath(mpe.CREATE_NEW_EMAIL)
        return True