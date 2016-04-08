# !/usr/bin/env python 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import basket_elements as be

class Basket:

    def open_basket_with_product(self, product):
        self.driver.find_element_by_xpath(be.BASKET_ICO).click()
        self.wait_element_displayed_by_xpath(product)

    def open_empty_basket(self):
        self.driver.find_element_by_xpath(be.BASKET_ICO).click()
        self.wait_element_displayed_by_xpath(be.EMPTY_BASKET_ICO)
        self.driver.find_elements_by_xpath(be.EMPTY_BASKET_MSG)

    def delete_product(self):
        self.driver.find_element_by_xpath(be.DELETE_BTN).click()
        self.wait_element_displayed_by_xpath(be.EMPTY_BTN)


    def add_sku_count(self):
        self.driver.find_elements_by_xpath(mpe.MENU_CATEGORIES.get("CATEGORY_HOME")).click()
        self.wait_element_displayed_by_xpath(mpe.CAMPAIGN_WRAPPER + mpe.CAMPAIGN)
        self.driver.find_elements_by_xpath(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN)


    def add_modnakarta(self):
        pass

class MultiBasket(object):

    def open_basket_products(self, products):
        pass


        