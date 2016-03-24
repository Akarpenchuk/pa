# !/usr/bin/env python 
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from landing_page.landing import Landing

import mail_elements as me
import main_page.main_page_elements as mpe
import base_methods.config as conf
import cabinet.cabinet_elements as myinfo

class Mail(Landing):
    """check emails"""
    
    def check_registration_email(self):
        self.open_url(conf.EMAIL_ADDRESS, me.EMAIL_INPUT)
        self.driver.find_element_by_xpath(me.EMAIL_INPUT).send_keys(conf.RAND_EMAIL)
        self.driver.find_element_by_xpath(me.EMAIL_CHECK_BTN).click()
        self.wait_with_check(me.EMAIL_SELECT_LETTER)

        self.driver.find_element_by_xpath(me.EMAIL_SELECT_LETTER).click()
        self.wait_element_displayed_by_xpath(me.SELECT_FRAME)
        self.switch_to_frame(me.SELECT_FRAME)
        self.wait_element_displayed_by_xpath(me.EMAIL_REG_BTN)
        self.driver.find_element_by_xpath(me.EMAIL_REG_BTN).click()

        sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.wait_element_displayed_by_xpath(myinfo.RESET_POPUP)
        return True


    def check_recovery_email(self):
        self.open_url("http://mailinator.com", me.EMAIL_INPUT)

        self.driver.find_element_by_xpath(me.EMAIL_INPUT).send_keys(conf.RAND_EMAIL)
        print conf.RAND_EMAIL
        self.driver.find_element_by_xpath(me.EMAIL_INPUT).send_keys(Keys.ENTER)

        self.wait_with_check(me.EMAIL_SELECT_LETTER)
        self.driver.find_element_by_xpath(me.EMAIL_SELECT_LETTER).click()
        self.wait_element_displayed_by_xpath(me.SELECT_FRAME)
        # self.wait_element_displayed_by_xpath(me.SELECT_RECOVERY_LINK)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(me.SELECT_FRAME))
        self.driver.find_element_by_xpath(me.SELECT_RECOVERY_LINK).click()

        sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.driver.find_element_by_xpath(mpe.CREATE_NEW_EMAIL_FORM)
        return True