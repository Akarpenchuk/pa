# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from base_methods.base import BaseClass
from base_methods.hover import Action
from base_methods.wait import Wait
from base_methods.config import *

import main_page.main_page_elements as mpe
import modnakarta_page.modnakarta_page_elements as mkpe
import campaign.campaign_elements as ce
import product.product_page_elements as ppe

from selenium.common.exceptions import NoSuchElementException




class Anonym(Action, Wait, BaseClass):

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

                self.wait_element_displayed_by_xpath(mpe.REG_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_email)):
                email_field.clear()
                email_field.send_keys(invalid_email[i])
                pass_field.clear()
                pass_field.send_keys(valid_pass)
                reg_btn.click()

                self.wait_element_displayed_by_xpath(mpe.REG_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_pass)):
                email_field.clear()
                email_field.send_keys(valid_email)
                pass_field.clear()
                pass_field.send_keys(invalid_pass[i])
                reg_btn.click()

                self.wait_element_displayed_by_xpath(mpe.REG_EMAIL_INPUT_ERROR)

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

            for i in xrange(len(invalid_email)):
                email_field.clear()
                email_field.send_keys(invalid_email[i])
                pass_field.clear()
                pass_field.send_keys(valid_pass)
                auth_btn.click()

                self.wait_element_displayed_by_xpath(mpe.AUTH_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_pass)):
                email_field.clear()
                email_field.send_keys(valid_email)
                pass_field.clear()
                pass_field.send_keys(invalid_pass[i])
                auth_btn.click()

                self.wait_element_displayed_by_xpath(mpe.AUTH_EMAIL_INPUT_ERROR)

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

                self.wait_element_displayed_by_xpath(mpe.RECOVERY_EMAIL_INPUT_ERROR)

            return True
        return False


    def anonym_buy_modnakarta(self):
        #buy via modnakarta btn
        self.wait_element_displayed_by_xpath(mpe.MODNAKARTA_HEADER_LINK)
        self.driver.find_element_by_xpath(mpe.MODNAKARTA_HEADER_LINK).click()

        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

        self.driver.find_element_by_xpath(mkpe.MODNAKARTA_BASKET_ADD).click()

        if self.wait_element_displayed_by_xpath(mpe.AUTH_FORM):
            self.open_base_url()
        else:
            raise NoSuchElementException

        #buy via campaign
        self.driver.find_element_by_xpath(mpe.MODNAKARTA_CAMPAIGN).click()
        self.wait_element_displayed_by_xpath(mkpe.MODNAKARTA_BASKET_ADD)
        self.driver.find_element_by_xpath(mkpe.MODNAKARTA_BASKET_ADD).click()

        if self.wait_element_displayed_by_xpath(mpe.AUTH_FORM):
            self.open_base_url()
        else:
            raise NoSuchElementException

        #buy via help menu
        self.driver.find_element_by_xpath(mpe.HELP_DICT.itervalues().next()).click()
        self.wait_element_displayed_by_xpath(mpe.MODNAKARTA_MENU_HELP)
        self.driver.find_element_by_xpath(mpe.MODNAKARTA_MENU_HELP).click()

        if self.wait_element_displayed_by_xpath(mkpe.ABOUT_MODNAKARTA):
            self.open_base_url()
            return True
        else:
            raise NoSuchElementException

    def anonym_buy_product(self):
        self.driver.find_element_by_xpath(mpe.LIST_CAMPAIGN_CURRENT).click()
        count_product = 0

        #outlet
        try:
            self.wait_element_displayed_by_xpath(ce.OUTLET_CATEGORY)
            self.driver.find_element_by_xpath(ce.OUTLET_CATEGORY).click()
            wait_product_list = self.wait_element_displayed_by_xpath(ce.LIST_PRODUCT)
            hide_sold = self.driver.find_element_by_xpath(ce.HIDE_SOLD).click()
            wait_product_list

            product_added = False
            while product_added != True:
                try:
                    count_product += 1
                    self.wait_element_displayed_by_xpath(ce.LIST_PRODUCT)
                    open_product = self.driver.find_element_by_xpath(ce.LIST_PRODUCT + '[' + str(count_product) + ']' + '/a').click()
                    wait_product_page = self.wait_element_displayed_by_xpath(ppe.PRODUCT_BASKET_ADD)
                    add_product = self.driver.find_element_by_xpath(ppe.PRODUCT_BASKET_ADD).click()
                    wait_product_added = self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)
                    product_added = True
                except:
                    self.driver.back()
                    continue
            return True

        #campaign
        except:
            hide_sold = self.driver.find_element_by_xpath(ce.HIDE_SOLD).click()
            wait_product_list = self.wait_element_displayed_by_xpath(ce.LIST_PRODUCT)

            product_added = False
            while product_added != True:
                try:
                    count_product += 1
                    open_product = self.driver.find_element_by_xpath(ce.LIST_PRODUCT + '[' + str(count_product) + ']' + '/a').click()
                    wait_product_page = self.wait_element_displayed_by_xpath(ppe.PRODUCT_BASKET_ADD)
                    add_product = self.driver.find_element_by_xpath(ppe.PRODUCT_BASKET_ADD).click()
                    wait_product_added = self.wait_element_displayed_by_xpath(mpe.AUTH_FORM)
                    product_added = True
                except:
                    self.driver.back()
                    continue
            return True

    def anonym_open_basket(self):
        self.driver.find_element_by_xpath(be.BASKET_ICO).click()
        self.wait_element_displayed_by_xpath(be.EMPY)