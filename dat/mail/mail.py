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
import base_methods.config as conf
import cabinet.cabinet_elements as myinfo


class Mail():

    def check_registration_email(self, rand_email):
        url = self.driver.current_url
        if me.EMAIL_ADDRESS not in url:
            self.open_url(me.EMAIL_ADDRESS, me.EMAIL_INPUT)
        print 1
        self.send_keys(me.EMAIL_INPUT, rand_email)
        print 2
        self.wait_element(me.EMAIL_CHECK_BTN)
        self.click(me.EMAIL_CHECK_BTN)
        self.wait_and_check(me.REGISTRATION_EMAIL)

        self.click(me.REGISTRATION_EMAIL)
        self.wait_element(me.SELECT_FRAME)
        self.switch_to_frame(me.SELECT_FRAME)
        self.wait_element(me.EMAIL_REG_BTN)
        self.click(me.EMAIL_REG_BTN)

        sleep(2)
        self.switch_to_new_window()
        return True

    def clear_mailbox(self, test_email):
        self.open_url(me.EMAIL_ADDRESS, me.EMAIL_INPUT)
        self.send_keys(me.EMAIL_INPUT, test_email)
        print 'check recovery test_email ', test_email
        self.send_keys(me.EMAIL_INPUT, Keys.ENTER)
        try:
            self.wait_element(me.EMAIL_CHECKBOX)
            email_count = self.count_elements(me.EMAIL_CHECKBOX)
            print 'email_count ', email_count
            for i in xrange(email_count):
                i += 1
                self.click(me.EMAIL + '[' + str(i) + ']' + me.EMAIL_CHECKBOX)
                continue
            self.click(me.DELETE_ALL_EMAILS)
            self.wait_element(me.EMPTY_EMAIL_BOX_MSG)
        except:
            self.wait_element(me.EMPTY_EMAIL_BOX_MSG)
            return True

    def check_recovery_email(self, test_email):
        self.open_url(me.EMAIL_ADDRESS, me.EMAIL_INPUT)
        self.send_keys(me.EMAIL_INPUT, test_email)
        self.send_keys(me.EMAIL_INPUT, Keys.ENTER)

        # while not self.wait_element(me.RECOVERY_EMAIL):
        self.wait_and_check(me.RECOVERY_EMAIL)

        self.click(me.RECOVERY_EMAIL)
        self.wait_element(me.SELECT_FRAME)
        self.switch_to_frame(me.SELECT_FRAME)
        self.wait_element(me.SELECT_RECOVERY_LINK)
        self.click(me.SELECT_RECOVERY_LINK)

        sleep(2)
        self.switch_to_new_window()
        self.wait_element(myinfo.PWD_RESET_FST_INPUT)
        return True