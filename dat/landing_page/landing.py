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
import cabinet.cabinet_elements as ce

class Landing:

    def landing_login(self):
        self.click(le.AUTH_LINK)
        sleep(1)
        self.clear(le.AUTH_EMAIL_INPUT)
        self.send_keys(le.AUTH_EMAIL_INPUT, ce.USER_EMAIL)
        self.clear(le.AUTH_PASS_INPUT)
        self.send_keys(le.AUTH_PASS_INPUT, ce.USER_PASS)
        self.click(le.AUTH_BTN)
        if self.wait_element(mpe.CAMPAIGN):
            return True
        return False

    def landing_registration(self):
        rand_email = self.get_rand_email()
        print 'get_rand_email ', rand_email
        self.send_keys(le.REG_EMAIL_INPUT, rand_email)
        self.click(le.REG_BTN)
        sleep(1)
        self.wait_element(le.REG_SENT)
        email = self.get_text(le.REG_SENT)
        print 'get_text email ', email
        if email is rand_email:
            self.wait_element(le.CHECK_EMAIL_BTN)
        self.click(le.CHECK_EMAIL_BTN)
        sleep(1)
        self.switch_to_window(-1)
        self.find(me.EMAIL_INPUT)
        return rand_email

