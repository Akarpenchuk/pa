# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
import random

from selenium import webdriver

# from base_methods.base import BaseClass
from base_methods.wait import Wait
from selenium.webdriver.common.keys import Keys
import unittest

import main_page.main_page_elements as mpe
import campaign_elements as ce

class Campaign():

    # def open_campaign_iter(self):
    #     campaigns = self.find_elements(mpe.CAMPAIGN)
    #     for i in xrange(len(campaigns)):
    #         i += 1
    #         self.click(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN)
    #         self.change_to_catalogue()
    #     return True    

    def open_rand_campaign(self):
        camp_count = self.count_elements(mpe.CAMPAIGN)
        rand_count = random.randint(1, camp_count)
        camp_name = self.get_text(mpe.CAMPAIGN_NAME)
        print 'camp_count', camp_count
        print 'camp_name', camp_name

        while 'modnakarta' in self.driver.current_url:
            rand_count = randint(1, camp_count)
            self.click('(' + mpe.CAMPAIGN + ')' + '[' + str(rand_count) + ']')

        self.click('(' + mpe.CAMPAIGN + ')' + '[' + str(rand_count) + ']')
        self.change_to_catalogue()
        self.wait_element(ce.PRODUCT)
        return camp_name.encode('utf-8')

        #check campaign details
        self.find_text(ce.BREADCRUMBS, camp_name)
        self.find_text(ce.CAMPAIGN_NAME, camp_name)
        self.find_list_elements(ce.FILTER_ITEMS)
        self.find(ce.HIDE_SOLD)
        self.find(ce.PRODUCT)

    def change_to_catalogue(self):
        if 'campaign' in self.driver.current_url:
            catalogue = self.driver.current_url.replace('campaign', 'catalogue')
            self.driver.get(catalogue)
            # sleep(2)
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

    def hide_sold(self):
        self.click(ce.HIDE_SOLD)
        sleep(1)
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
        
        self.scroll_down(ce.LAST_PRODUCT)

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

    def affiliation_apply(self):
        self.click(ce.FILTER_ITEMS[0])
        self.wait_element(ce.FIRST_AFF_ITEM)
        self.get_items_list(ce.AFF_NAME)

        for i in xrange(ce.AFF_LIST.items()):

            self.click(i)
            self.wait_element(ce.PRODUCT)
            
            #check product aff in db
            link = self.get_attr(ce.FIRST_PRODUCT_LINK)
            link = str(link)[9:20]
            self.connect_db()



        

    def check_categories(self):
        pass

    def check_brand(self):
        pass

    def check_size(self):
        pass

    def check_sorting(self):
        pass

    def check_hide_sold(self):
        pass