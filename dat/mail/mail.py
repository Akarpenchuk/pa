# !/usr/bin/env python 
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# from base_methods.base import BaseClass

import mail_elements as me
import main_page.main_page_elements as mpe
import base_methods.config as conf


class Mail():
    """check emails"""
    
    def check_registration_email(self):
        rand_email = self.get_rand_email()

        self.open_url(me.EMAIL_ADDRESS, me.EMAIL_INPUT)
        self.send_keys(me.EMAIL_INPUT, rand_email)
        self.find(me.EMAIL_CHECK_BTN).click()
        self.wait_with_check(me.REGISTRATION_EMAIL)

        self.click(me.REGISTRATION_EMAIL)
        self.wait_element(me.SELECT_FRAME)
        self.switch_to_frame(me.SELECT_FRAME)
        self.wait_element(me.EMAIL_REG_BTN)
        self.click(me.EMAIL_REG_BTN)

        sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.wait_element(mpe.PERSONAL_INFO_POPUP)
        return True


    def check_recovery_email(self):
        self.open_url("http://mailinator.com", me.EMAIL_INPUT)

        self.find(me.EMAIL_INPUT).send_keys(conf.USER_EMAIL)
        print conf.USER_EMAIL
        self.find(me.EMAIL_INPUT).send_keys(Keys.ENTER)

        self.wait_with_check(me.RECOVERY_EMAIL)
        self.find(me.RECOVERY_EMAIL).click()
        self.wait_element(me.SELECT_FRAME)
        self.switch_to_frame(me.SELECT_FRAME)
        self.wait_element(me.SELECT_RECOVERY_LINK)
        self.find(me.SELECT_RECOVERY_LINK).click()

        sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.wait_element(mpe.PERSONAL_INFO_POPUP)
        return True