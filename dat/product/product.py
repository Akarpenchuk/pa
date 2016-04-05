# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
import logging
logging.basicConfig(filename = '/home/ace/log_webdriver', level = logging.DEBUG)

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from main_page.main_page import MainPage

import main_page.main_page_elements as mpe
import basket.basket_elements as be
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


    def add_product_less_99(self):
        campaigns = self.driver.find_elements_by_xpath(mpe.CAMPAIGN)
        for i in xrange(len(campaigns)):
            i += 1
            
            self.driver.find_element_by_xpath(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN).click()
            self.check_if_outlet()
            
            product_count = self.driver.find_elements_by_xpath(ce.PRODUCT)
            assert product_count >= 1

            self.driver.find_element_by_xpath(ce.SORT_ASC).click()
            self.wait_element_displayed_by_xpath(ce.PRODUCT)
            self.driver.find_element_by_xpath(ce.HIDE_SOLD).click()
            self.wait_element_displayed_by_xpath(ce.PRODUCT)
            
            product_price = self.driver.find_element_by_xpath(ce.PRODUCT + '[' + str(i) + ']' + ce.PRODUCT_NEW_PRICE).text
            print product_price
            if product_price >= 99:
                self.driver.find_element_by_xpath(mpe.LOGO).click()
                self.wait_element_displayed_by_xpath(mpe.LOGO)
                continue

            products = self.driver.find_elements_by_xpath(ce.PRODUCT)

            for i in xrange(len(products)):
                i += 1
                if product_price <= 98:
                    try:
                        self.driver.find_element_by_xpath(ce.PRODUCT + '[' + str(i) + ']' + '/a').click()
                        self.wait_element_displayed_by_xpath(pe.PRODUCT_BIG_IMG)
                        self.driver.find_element_by_xpath(be.ADD_PRODUCT_BTN).click()
                        self.wait_element_displayed_by_xpath()
                    except:
                        print 'product not added'
                else:
                    print '> 99'
                continue

