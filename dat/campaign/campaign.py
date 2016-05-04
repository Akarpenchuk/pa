# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from base_methods.wait import Wait

import main_page.main_page_elements as mpe
import campaign_elements as ce

class Campaign():

    def open_campaign_iter(self, n):
        campaigns = self.driver.find_elements_by_xpath(mpe.CAMPAIGN)
        for i in xrange(len(campaigns)):
            i += n
            self.driver.find_element_by_xpath(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN).click()
            if self.check_if_outlet():
                self.driver.find_element_by_xpath(ce.OUTLET_CATEGORY).click()
            product_count = self.driver.find_elements_by_xpath(ce.PRODUCT)
            assert product_count >= 1
            return True
        return False


    def open_campaign_iter_with_affiliations (self):
        campaigns = self.driver.find_elements_by_xpath(mpe.CAMPAIGN)
        for i in xrange(len(campaigns)):
            i += n

            if self.driver.find_element_by_xpath(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN).!hover:
                
                self.driver.find_element_by_xpath(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN).click()
                if self.check_if_outlet():
                    self.driver.find_elements_by_xpath(ce.OUTLET_CATEGORY).click()
                    print 'check_if_outlet'
                    break
                product_count = self.driver.find_elements_by_xpath(ce.PRODUCT)
                assert product_count >= 1
            return True
        return False        


    def open_product_iter(self):
        products = self.driver.find_elements_by_xpath(ce.PRODUCT)
        for i in xrange(1, len(products)):
            # i += 1
            try:
                self.driver.find_element_by_xpath(ce.PRODUCT + '[' + str(i) + ']' + '/a').click()
                self.wait_element_displayed_by_xpath(pe.PRODUCT_BIG_IMG)
                return True
            except:
                self.driver.back()
                self.wait_element_displayed_by_xpath(ce.PRODUCT)
            continue


    def check_product_less_99(self, n):
        product_new_price = self.driver.find_element_by_xpath(ce.PRODUCT + '[' + int(n) + ']' + ce.PRODUCT_NEW_PRICE).text
        if int(product_new_price) >= 99:
            return False
        print "first product price ", product_new_price
        return True



    def check_if_outlet(self):
        #if outlet
        try:
            self.wait_element_displayed_by_xpath(ce.OUTLET_CATEGORY)
            self.driver.find_element_by_xpath(ce.OUTLET_CATEGORY).click()
            self.wait_element_displayed_by_xpath(ce.PRODUCT)
            return True
        #if simple campaign
        except:
            self.driver.find_elements_by_xpath_by_xpath(ce.PRODUCT)
            return False


    def hide_sold(self):
        self.driver.find_element_by_xpath(ce.HIDE_SOLD).click()
        self.wait_element_displayed_by_xpath(ce.PRODUCT)
        return True


    def sort_asc(self):

        self.driver.find_element_by_xpath(ce.SORT_ASC).click()
        self.wait_element_displayed_by_xpath(ce.PRODUCT)   
        
        first_price = self.driver.find_element_by_xpath(ce.PRODUCT_NEW_PRICE).text
        first_price = int(first_price)
        print first_price

        last_price = self.driver.find_element_by_xpath(ce.LAST_PRODUCT + ce.PRODUCT_NEW_PRICE).text
        last_price = int(last_price)
        print last_price

        assert first_price < last_price

    def catalogue_details(self):
        camp_name = self.wait_element_displayed_by_xpath(ce.CAMPAIGN_NAME).text
        camp_time = self.driver.find_element_by_xpath(ce.TIME).text
        camp_promo_banner = self.driver.find_element_by_xpath(ce.BANNER)
        camp_app_banner = self.driver.find_element_by_xpath(ce.app_banner)

        !scroll
        !save_position
        camp_up_btn = self.driver.find_elements_by_xpath(ce.UP_BTN).click()
        !save_position2
        !assert positions
        !assert camp_name is MainPage().camp_name
        !assert camp_time is MainPage().camp_time
        !assert camp_promo_banner
        !assert camp_app_banner

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