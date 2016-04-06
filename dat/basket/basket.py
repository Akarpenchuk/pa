# !/usr/bin/env python 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data.config import *

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from campaign.campaign import Campaign

class Basket:

    def open_basket_with_product(self, product):
        self.driver.find_element_by_xpath(conf.BASKET_ICO).click()
        self.wait_element_displayed_by_xpath(product)



    def delete_product(self):
        self.driver.find_element_by_xpath(be.DELETE_BTN).click()
        self.wait_element_displayed_by_xpath(be.EMPTY_BTN)


    def add_sku_count(self):
        self.driver.find_elements_by_xpath(mpe.MENU_CATEGORIES.get("CATEGORY_HOME")).click()
        self.wait_element_displayed_by_xpath(mpe.CAMPAIGN_WRAPPER + mpe.CAMPAIGN)
        self.driver.find_elements_by_xpath(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN)


    def add_product(self):
        products = self.driver.find_elements_by_xpath(ce.PRODUCT)

        for i in xrange(len(products)):
            i += 1
            self.driver.find_element_by_xpath(ce.PRODUCT + '[' + str(i) + ']' + '/a').click()
            if self.wait_element_displayed_by_xpath(pe.ADD_PRODUCT_BTN):

                #store product data
                product_name = self.driver.find_element_by_xpath(pe.PRODUCT_NAME).text
                product_brand = self.driver.find_elements_by_xpath(pe.PRODUCT_BRAND).text
                product_old_price = self.driver.find_elements_by_xpath(pe.PRODUCT_OLD_PRICE).text
                product_new_price = self.driver.find_elements_by_xpath(pe.PRODUCT_NEW_PRICE).text

                self.driver.find_element_by_xpath(pe.ADD_PRODUCT_BTN).click()
                self.wait_element_displayed_by_xpath(pe.PRODUCT_ADDED_MESSAGE)
                return True
                break
            else:
                print 'product not added'
                self.driver.back()
                continue


    def add_modnakarta(self):
        pass

class MultiBasket(object):

    def open_basket_products(self, products):
        pass


        