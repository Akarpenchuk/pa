# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep

from selenium import webdriver

from base_methods.base import BaseClass
from base_methods.wait import Wait
from selenium.webdriver.common.keys import Keys
import unittest

import main_page.main_page_elements as mpe
import campaign_elements as ce

class Campaign():

    def open_campaign_iter(self, n):
        campaigns = self.find_elements(mpe.CAMPAIGN)
        for i in xrange(len(campaigns)):
            i += n
            self.click(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN)
            self.change_to_catalogue()
            
    def change_to_catalogue(self):
        if 'campaign' in self.driver.current_url:
                catalogue = self.driver.current_url.replace('campaign', 'catalogue')
                self.driver.get(catalogue)
                self.wait_element(ce.PRODUCT)
                return True

    def open_campaign_iter_with_affiliations (self):
        campaigns = self.find(mpe.CAMPAIGN)
        for i in xrange(len(campaigns)):
            i += n

            if self.find(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN): #!hover
                
                self.find(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN).click()
                if self.check_if_outlet():
                    self.find(ce.OUTLET_CATEGORY).click()
                    break
                product_count = self.wait_element(ce.PRODUCT)
                assert product_count >= 1
            return True
        return False

    def open_product_iter(self):
        products = self.driver.find_elements_by_xpath(ce.PRODUCT)
        for i in xrange(1, len(products)):
            # i += 1
            try:
                self.find(ce.PRODUCT + '[' + str(i) + ']' + '/a').click()
                self.wait_element(pe.PRODUCT_BIG_IMG)
                return True
            except:
                self.driver.back()
                self.wait_element(ce.PRODUCT)
            continue

    def check_product_less_99(self):
        count = 1
        first_product_price = self.find_text(ce.PRODUCT + '[' + str(count) + ']' + ce.PRODUCT_NEW_PRICE)
        first_product_price = first_product_price.replace(u' грн', '')
        print 'first_product_price ', first_product_price
        first_product_price = int(first_product_price)
        if first_product_price > 99:
            return False
        return True
        print "first_product_price ", first_product_price

    def check_if_outlet(self):
        #if outlet
        try:
            self.wait_element(ce.OUTLET_CATEGORY)
            self.find(ce.OUTLET_CATEGORY).click()
            self.wait_element(ce.PRODUCT)
            return True
        #if simple campaign
        except:
            self.driver.find_elements_by_xpath(ce.PRODUCT)
            return False

    def hide_sold(self):
        self.click(ce.HIDE_SOLD)
        self.wait_element(ce.PRODUCT_NEW_PRICE)
        return True

    def sort_asc(self):
        self.click(ce.FILTER_SORT)
        self.wait_element(ce.SORT_ASC)
        self.click(ce.SORT_ASC)
        self.wait_element(ce.PRODUCT_NEW_PRICE)
        sleep(2)

        first_price = self.find_text(ce.PRODUCT_NEW_PRICE)
        first_price = first_price.encode("utf-8").replace('грн', '')
        first_price = first_price.replace(' ', '')
        first_price = int(first_price)
        print "first_price ", first_price
        
        self.scroll_bottom_product_list()

        self.wait_element(ce.LAST_PRODUCT + ce.PRODUCT_NEW_PRICE)

        # last_product_name = self.find_text(ce.LAST_PRODUCT + ce.PRODUCT_NAME)
        # print 'last_product_name ', last_product_name

        last_price = self.find_text_few_elements(ce.LAST_PRODUCT, ce.PRODUCT_NEW_PRICE)
        last_price = last_price.encode("utf-8").replace('грн', '')
        last_price = last_price.replace(' ', '')
        last_price = int(last_price)
        print "last_price ", last_price

        self.assertTrue(first_price <= last_price)
        return True
            # print 'first_price <= last_price'
        # print 'first_price > last_price!'

    def sort_desc(self):
        self.find(ce.FILTER_SORT).click()
        self.find(ce.SORT_DESC).click()
        self.wait_element(ce.PRODUCT)   
        
        first_price = self.find(ce.PRODUCT_NEW_PRICE).text
        first_price = int(first_price)
        print first_price

        #get last product
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

        last_price = self.find(ce.LAST_PRODUCT + ce.PRODUCT_NEW_PRICE).text
        last_price = int(last_price)
        print last_price

        assert first_price > last_price

    def catalogue_details(self):
        camp_name = self.wait_element(ce.CAMPAIGN_NAME).text
        camp_time = self.find(ce.TIME).text
        camp_promo_banner = self.find(ce.BANNER)
        camp_app_banner = self.find(ce.app_banner)

        # !scroll
        # !save_position
        # camp_up_btn = self.driver.find_elements_by_xpath(ce.UP_BTN).click()
        # !save_position2
        # !assert positions
        # !assert camp_name is MainPage().camp_name
        # !assert camp_time is MainPage().camp_time
        # !assert camp_promo_banner
        # !assert camp_app_banner

    def catalogue_affiliation(self):
        pass

    def catalogue_categories(self):
        pass

    def catalogue_brand(self):
        pass

    def catalogue_size(self):
        pass

    def catalogue_sorting(self):
        pass

    def catalogue_hide_sold(self):
        pass