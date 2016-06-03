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
from base_methods.wait import Wait
from campaign.campaign import Campaign
from base_methods.config import *

import main_page.main_page_elements as mpe
import modnakarta_page.modnakarta_page_elements as mkpe
import campaign.campaign_elements as ce
import product.product_page_elements as ppe
import base_methods.config as conf

from selenium.common.exceptions import NoSuchElementException




class Anonym(Campaign, Wait, BaseClass):

    def check_validation_reg(self):
        self.find(mpe.REG_LINK).click()

        if self.wait_element(mpe.REG_FORM):

            email_field = self.find(mpe.REG_EMAIL_INPUT)
            pass_field = self.find(mpe.REG_PASS_INPUT)
            reg_btn = self.find(mpe.REG_BTN)

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

                self.wait_element(mpe.REG_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_email)):
                email_field.clear()
                email_field.send_keys(invalid_email[i])
                pass_field.clear()
                pass_field.send_keys(valid_pass)
                reg_btn.click()

                self.wait_element(mpe.REG_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_pass)):
                email_field.clear()
                email_field.send_keys(valid_email)
                pass_field.clear()
                pass_field.send_keys(invalid_pass[i])
                reg_btn.click()

                self.wait_element(mpe.REG_EMAIL_INPUT_ERROR)

            return True
        return False


    def check_validation_auth(self):
        if self.wait_element(mpe.AUTH_FORM):

            email_field = self.find(mpe.AUTH_EMAIL_INPUT)
            pass_field = self.find(mpe.AUTH_PASS_INPUT)
            auth_btn = self.find(mpe.AUTH_BTN)

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

                self.wait_element(mpe.AUTH_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_email)):
                email_field.clear()
                email_field.send_keys(invalid_email[i])
                pass_field.clear()
                pass_field.send_keys(valid_pass)
                auth_btn.click()

                self.wait_element(mpe.AUTH_EMAIL_INPUT_ERROR)

            for i in xrange(len(invalid_pass)):
                email_field.clear()
                email_field.send_keys(valid_email)
                pass_field.clear()
                pass_field.send_keys(invalid_pass[i])
                auth_btn.click()

                self.wait_element(mpe.AUTH_EMAIL_INPUT_ERROR)

                return True
            return False


    def check_validation_recovery(self):
        if self.find(mpe.RECOVERY_EMAIL_LINK):
            self.click(mpe.RECOVERY_EMAIL_LINK)
        else:
            self.open_url(BASE_URL, mpe.AUTH_LINK)
            self.click(mpe.AUTH_LINK)
            self.wait_element(mpe.AUTH_FORM)
            self.click(mpe.RECOVERY_EMAIL_LINK)

        if self.wait_element(mpe.RECOVERY_EMAIL_FORM):

            email_field = self.find(mpe.RECOVERY_EMAIL_INPUT)
            rec_btn = self.find(mpe.RECOVERY_EMAIL_BTN)

            valid_email = ["absolutelynewtestemail@gmail.com"]
            invalid_email = [" 2 @yopmail.com", "!@#$%^&()_+~@i.ua", ""]

            for i in xrange(len(valid_email)):
                sleep(1)
                email_field.clear()
                email_field.send_keys(valid_email)
                rec_btn.click()

                self.wait_element(mpe.RECOVERY_EMAIL_INPUT_ERROR)
                print 'valid email length', len(valid_email)

            for i in xrange(len(invalid_email)):
                email_field.clear()
                email_field.send_keys(invalid_email[i])
                rec_btn.click()

                self.wait_element(mpe.RECOVERY_EMAIL_INPUT_ERROR)
                print 'invalid email length', len(invalid_email)
        
        self.refresh()


    def anonym_buy_modnakarta(self):
        #buy via modnakarta btn
        self.wait_element(mpe.MODNAKARTA_HEADER_LINK)
        self.find(mpe.MODNAKARTA_HEADER_LINK).click()

        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

        self.click(mkpe.MODNAKARTA_BASKET_ADD)

        if self.wait_element(mpe.AUTH_FORM):
            self.open_url(conf.BASE_URL)
        else:
            raise NoSuchElementException

        #buy via campaign
        self.find(mpe.MODNAKARTA_CAMPAIGN).click()
        self.wait_element(mkpe.MODNAKARTA_BASKET_ADD)
        self.find(mkpe.MODNAKARTA_BASKET_ADD).click()

        if self.wait_element(mpe.AUTH_FORM):
            self.open_url(conf.BASE_URL)
        else:
            raise NoSuchElementException

        #buy via help menu
        self.click(mpe.HELP_MENU.itervalues().next())
        self.find(mpe.MODNAKARTA_MENU_HELP)
        self.click(mpe.MODNAKARTA_MENU_HELP)

        if self.wait_element(mkpe.ABOUT_MODNAKARTA):
            self.open_url(conf.BASE_URL)
            return True
        else:
            raise NoSuchElementException

    def anonym_buy_product(self):
        self.click(mpe.LIST_CAMPAIGN_CURRENT)
        self.change_to_catalogue()

        #outlet
        try:
            self.wait_element(ce.OUTLET_CATEGORY)
            self.click(ce.OUTLET_CATEGORY)
            self.wait_element(ce.LIST_PRODUCT)
            self.click(ce.HIDE_SOLD)

            is_auth_form = False
            while is_auth_form != True:
                try:
                    count_product += 1
                    self.wait_element(ce.LIST_PRODUCT)
                    open_product = self.click(ce.LIST_PRODUCT + '[' + str(count_product) + ']' + '/a')
                    wait_product_page = self.wait_element(ppe.PRODUCT_BASKET_ADD)
                    add_product = self.click(ppe.PRODUCT_BASKET_ADD)
                    wait_auth_form = self.wait_element(mpe.AUTH_FORM)
                except:
                    self.driver.back()
                    continue
            return True

        #campaign
        except:
            self.wait_element(ce.PRODUCT)
            self.click(ce.HIDE_SOLD)
            self.wait_element(ce.PRODUCT)



            count_product = 0
            is_auth_form = False
            while is_auth_form != True:
                count_product += 1
                self.wait_element(ce.PRODUCT)
                self.click(ce.PRODUCT + '[' + str(count_product) + ']' + '/a')
                # sleep(1)
                self.wait_element(ppe.BASKET_ADD_ENABLED)
                self.click(ppe.BASKET_ADD_ENABLED)
                self.wait_element(mpe.AUTH_FORM)
                break
            else:
                self.driver.back()
                # continue
            # return True

    def open_empty_basket(self):
        self.find(be.BASKET_ICO).click()
        self.wait_element(be.EMPTY_BASKET_MSG)