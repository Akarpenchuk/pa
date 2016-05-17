# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
import logging
logging.basicConfig(filename = '/home/ace/log_webdriver', level = logging.DEBUG)

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import main_page.main_page_elements as mpe
import basket.basket_elements as be
import product_page_elements as pe
import campaign.campaign_elements as ce
import base_methods.config as conf

class Product():

    def select_size(self):
        if self.driver.find_element_by_xpath(PRODUCT_SIZE_AVAILABLE):
            self.driver.find_element_by_xpath(PRODUCT_SIZE_AVAILABLE).click()
            self.driver.find_element_by_xpath(PRODUCT_SIZE_SELECTED).is_displayed()

        self.driver.find_element_by_xpath(PRODUCT_ADD_ENABLED).click()
        self.wait.until(lambda self: self.find_element_by_xpath(POP_SKU_ADDED).is_displayed())
        print 'product added'


    def add_product(self):
        if not self.add_product_available_size():
            self.add_product_selected_size()
        elif not self.add_product_selected_size():
            self.add_product_one_size()
        elif not self.add_product_one_size():
            self.add_product_without_size()
        elif not self.add_product_without_size():
            print 'serching another product'
            self.driver.back()
            self.wait_element_displayed_by_xpath(ce.PRODUCT)
            return False
        
        return True


    def add_product_available_size(self):
        self.wait_element_displayed_by_xpath(pe.PRODUCT_SIZE_AVAILABLE)
        self.driver.find_element_by_xpath(pe.PRODUCT_SIZE_AVAILABLE).click()

        self.wait_element_displayed_by_xpath(pe.PRODUCT_SIZE_SELECTED)

        self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
        self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MSG)
        self.wait_element_displayed_by_xpath(be.BASKET_ICO)
        return True


    def add_product_selected_size(self):
        self.driver.find_element_by_xpath(pe.PRODUCT_SIZE_SELECTED)

        self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
        self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MSG)
        self.wait_element_displayed_by_xpath(be.BASKET_ICO)
        return True


    def add_product_size_one(self):
        self.driver.find_element_by_xpath(pe.PRODUCT_SIZE_ONE)

        self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
        self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MSG)
        self.wait_element_displayed_by_xpath(be.BASKET_ICO)
        return True


    def add_product_without_size(self):
        self.driver.find_element_by_xpath(pe.PRODUCT_NO_SIZE)

        self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
        self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MSG)
        self.wait_element_displayed_by_xpath(be.BASKET_ICO)
        return True


    def product_count_more_than_1(self):
        product_count = self.driver.find_elements_by_xpath(pe.PRODUCT_COUNT)
        if len(product_count) > 1:
            return False
        return True


    def product_count_less_than_1(self):
        product_count = self.driver.find_elements_by_xpath(pe.PRODUCT_COUNT)
        if len(product_count) < 1:
            return False    
        return True