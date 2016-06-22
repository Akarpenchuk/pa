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
        self.click(le.AUTH_LINK)
        sleep(1)
        self.clear(le.AUTH_EMAIL_INPUT)
        self.send_keys(le.AUTH_EMAIL_INPUT, conf.USER_EMAIL)
        self.clear(le.AUTH_PASS_INPUT)
        self.send_keys(le.AUTH_PASS_INPUT, conf.USER_PASS)
        self.click(le.AUTH_BTN)
        if self.wait_element(mpe.LIST_CAMPAIGN):
            return True
        return False

    def landing_registration(self):
        self.send_keys(le.REG_EMAIL_INPUT, conf.RAND_EMAIL)
        self.click(le.REG_BTN)
        self.wait_element(le.REG_SENT)
        email = self.find_text(le.REG_SENT)
        assert email in conf.RAND_EMAIL
        sleep(1)
        self.click(le.CHECK_EMAIL_BTN)
        sleep(1)
        self.switch_to_new_window()
        self.find(me.EMAIL_INPUT)
        return True
