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


    def add_product_less_99(self):
        self.open_base_url()
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

            product_new_price = self.driver.find_element_by_xpath(ce.PRODUCT_NEW_PRICE).text
            if int(product_new_price) >= 99:
                self.driver.find_element_by_xpath(mpe.LOGO).click()
                self.wait_element_displayed_by_xpath(mpe.LOGO)
                continue
            print "first product price ", self.driver.find_element_by_xpath(ce.PRODUCT + '[' + str(i) + ']' + ce.PRODUCT_NEW_PRICE).text
            
            #TODO use add_product()

            products = self.driver.find_elements_by_xpath(ce.PRODUCT)

            for i in xrange(len(products)):
                i += 1
                self.driver.find_element_by_xpath(ce.PRODUCT + '[' + str(i) + ']' + '/a').click()
                #TODO add_product_from_product_page()
                try:
                    self.wait_element_displayed_by_xpath(pe.PRODUCT_SIZE_AVAILABLE)
                    self.driver.find_element_by_xpath(pe.PRODUCT_SIZE_AVAILABLE).click()

                    self.wait_element_displayed_by_xpath(pe.PRODUCT_SIZE_SELECTED)

                    #store product data
                    product_name = self.driver.find_element_by_xpath(pe.PRODUCT_NAME).text
                    product_brand = self.driver.find_element_by_xpath(pe.PRODUCT_BRAND).text
                    product_old_price = self.driver.find_element_by_xpath(pe.PRODUCT_OLD_PRICE).text

                    self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
                    self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MSG)
                    self.wait_element_displayed_by_xpath(be.BASKET_ICO)
                    break
                except:
                    try:
                        self.driver.find_element_by_xpath(pe.PRODUCT_SIZE_SELECTED)
                        #TODO add_product_from_product_page()

                        #store product data
                        product_name = self.driver.find_element_by_xpath(pe.PRODUCT_NAME).text
                        product_brand = self.driver.find_element_by_xpath(pe.PRODUCT_BRAND).text
                        product_old_price = self.driver.find_element_by_xpath(pe.PRODUCT_OLD_PRICE).text

                        self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
                        self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MSG)
                        self.wait_element_displayed_by_xpath(be.BASKET_ICO)
                        break
                    except:
                        try:
                            self.driver.find_element_by_xpath(pe.PRODUCT_SIZE_ONE)
                            #TODO add_product_from_product_page()

                            #store product data
                            product_name = self.driver.find_element_by_xpath(pe.PRODUCT_NAME).text
                            product_brand = self.driver.find_element_by_xpath(pe.PRODUCT_BRAND).text
                            product_old_price = self.driver.find_element_by_xpath(pe.PRODUCT_OLD_PRICE).text

                            self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
                            self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MSG)
                            self.wait_element_displayed_by_xpath(be.BASKET_ICO)
                            break
                        except:
                            try:
                                self.driver.find_element_by_xpath(pe.PRODUCT_NO_SIZE)
                                #store product data
                                product_name = self.driver.find_element_by_xpath(pe.PRODUCT_NAME).text
                                product_brand = self.driver.find_element_by_xpath(pe.PRODUCT_BRAND).text
                                product_old_price = self.driver.find_element_by_xpath(pe.PRODUCT_OLD_PRICE).text

                                self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
                                self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MSG)
                                self.wait_element_displayed_by_xpath(be.BASKET_ICO)
                                break
                            except:
                                print 'serching another product'
                                self.driver.back()
                                continue
            break
        if self.wait_element_displayed_by_xpath(be.BASKET_ICO):
            self.driver.find_element_by_xpath(be.BASKET_ICO).click()

            self.wait_element_displayed_by_xpath(be.PRODUCT_NAME)
            name = self.driver.find_element_by_xpath(be.PRODUCT_NAME).text
            product_name = product_name.encode("utf-8")
            print product_name
            name = name.encode("utf-8")
            print name

            brand = self.driver.find_element_by_xpath(be.PRODUCT_BRAND).text
            product_brand = product_brand.encode("utf-8")
            print product_brand
            brand = brand.encode("utf-8")
            print brand

            new_price = self.driver.find_element_by_xpath(be.PRODUCT_NEW_PRICE).text
            product_new_price = product_new_price.encode("utf-8")
            print product_new_price
            new_price = new_price.encode("utf-8")
            print new_price

            assert product_name == name
            assert product_brand in brand
            assert product_new_price in new_price

            self.driver.find_element_by_xpath(be.CHECKOUT_BTN).click()
            self.wait_element_displayed_by_xpath(be.MIN_BASKET_MSG)
            return True
        return False


