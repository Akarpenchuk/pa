# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import main_page.main_page_elements as mpe
import modnakarta_page.modnakarta_page_elements as mkpe
import base_methods.base as base
import base_methods.hover as hover
from base_methods.config import *
from selenium.common.exceptions import NoSuchElementException




class Anonym:

    def __init__(self):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)


    def check_validation_reg(self):

        self.driver.find_element_by_xpath(mpe.REG_LINK).click()

        if self.wait_element_displayed_by_xpath(mpe.REG_FORM):

            email_field = self.driver.find_element_by_xpath(mpe.REG_EMAIL_INPUT)
            pass_field = self.driver.find_element_by_xpath(mpe.REG_PASS_INPUT)
            reg_btn = self.driver.find_element_by_xpath(mpe.REG_BTN)

            valid_email = ["mktestuser3@yopmail.com"]
            invalid_email = ["mktestuser333333@yo pmail.com", "slekslienseoi231@@i.ua", ""]

            valid_pass = ["qwe123"]
            invalid_pass = ["qwe12", "", "      "]

            for i in xrange(len(valid_email)):
                email_field.clear()
                email_field.send_keys(valid_email[i])
                pass_field.clear()
                pass_field.send_keys(valid_pass)
                reg_btn.click()

                self.driver.find_element_by_xpath(mpe.REG_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_email)):
                email_field.clear()
                email_field.send_keys(invalid_email[i])
                pass_field.clear()
                pass_field.send_keys(valid_pass)
                reg_btn.click()

                self.driver.find_element_by_xpath(mpe.REG_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_pass)):
                email_field.clear()
                email_field.send_keys(valid_email)
                pass_field.clear()
                pass_field.send_keys(invalid_pass[i])
                reg_btn.click()

                self.driver.find_element_by_xpath(mpe.REG_PASS_INPUT_ERROR)

            return True
        return False


    def check_validation_auth(self):

        if self.wait_element_displayed_by_xpath(mpe.AUTH_FORM):

            email_field = self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT)
            pass_field = self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT)
            auth_btn = self.driver.find_element_by_xpath(mpe.AUTH_BTN)

            valid_email = ["absolutelynewtestemail@gmail.com"]
            invalid_email = ["   @yopmail.com", "!@#$%^&()_+~@i.ua", ""]

            valid_pass = ["qwe123"]
            invalid_pass = ["qwe12", "", "      "]

            for i in xrange(len(valid_email)):
                email_field.clear()
                email_field.send_keys(valid_email)
                pass_field.clear()
                pass_field.send_keys(valid_pass)
                auth_btn.click()

                self.wait_element_displayed_by_xpath(mpe.AUTH_EMAIL_INPUT_ERROR)
                self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT_ERROR)
                self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT_ERROR)

            for i in xrange(len(invalid_email)):
                email_field.clear()
                email_field.send_keys(invalid_email[i])
                pass_field.clear()
                pass_field.send_keys(valid_pass)
                auth_btn.click()

                self.driver.find_element_by_xpath(mpe.AUTH_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_pass)):
                email_field.clear()
                email_field.send_keys(valid_email)
                pass_field.clear()
                pass_field.send_keys(invalid_pass[i])
                auth_btn.click()

                self.driver.find_element_by_xpath(mpe.AUTH_PASS_INPUT_ERROR)
                return True
            return False


    def check_validation_recovery(self):

        if self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_LINK).is_displayed():
            self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_LINK).click()
        else:
            self.open_url(BASE_URL, mpe.AUTH_LINK)
            self.driver.find_element_by_xpath(mpe.AUTH_LINK).click()
            self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)
            self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_LINK).click()

        if self.wait_element_displayed_by_xpath(mpe.RECOVERY_EMAIL_FORM):

            email_field = self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_INPUT)
            rec_btn = self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_BTN)

            valid_email = ["absolutelynewtestemail@gmail.com"]
            invalid_email = [" 2 @yopmail.com", "!@#$%^&()_+~@i.ua", ""]

            for i in xrange(len(valid_email)):
                sleep(1)
                email_field.clear()
                email_field.send_keys(valid_email)
                rec_btn.click()

                self.wait_element_displayed_by_xpath(mpe.RECOVERY_EMAIL_INPUT_ERROR)
                self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_email)):
                email_field.clear()
                email_field.send_keys(invalid_email[i])
                rec_btn.click()

                self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_INPUT_ERROR)

            return True
        return False


    def anonym_buy_modnakarta(self):

        #buy via modnakarta btn
        self.driver.find_element_by_xpath(mpe.MODNAKARTA_MENU_BTN).click()
        self.wait_element_displayed_by_xpath(mkpe.MODNAKARTA_BASKET_ADD)
        self.driver.find_element_by_xpath(mkpe.MODNAKARTA_BASKET_ADD).click()

        if self.wait_element_displayed_by_xpath(mpe.AUTH_FORM):
            self.open_url(BASE_URL, LIST_CAMPAIGN)
        else:
            raise NoSuchElementException

        #buy via campaign
        self.driver.find_element_by_xpath(mpe.MODNAKARTA_CAMPAIGN).click()
        self.wait_element_displayed_by_xpath(mkpe.MODNAKARTA_BASKET_ADD)
        self.driver.find_element_by_xpath(mkpe.MODNAKARTA_BASKET_ADD).click()

        if self.wait_element_displayed_by_xpath(mpe.AUTH_FORM):
            self.open_url(BASE_URL, LIST_CAMPAIGN)
        else:
            raise NoSuchElementException

        #buy via help menu
        self.hover(mpe.HELP_DICT.itervalues().next())
        self.driver.find_element_by_xpath(mpe.MODNAKARTA_MENU_HELP).click()
        if self.wait_element_displayed_by_xpath(mpe.AUTH_FORM):
            self.open_url(BASE_URL, LIST_CAMPAIGN)
        else:
            raise NoSuchElementException

        #open modnakarta via url
        self.open_url(mkpe.MODNAKARTA_PRODUCT_URL, LIST_CAMPAIGN)
