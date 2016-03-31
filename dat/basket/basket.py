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

    def check_basket_product_data(self, name, brand, old_price, new_price, count, photo):
        pass

    def check_basket_less_99(self):
        #message "order must be >= 99"
        basket_sum = self.driver.find_element_by_xpath("//span[@id='basket_total_sum']").text
        float(basket_sum)
        # try:
        while basket_sum <= 98:
            self.driver.back()
            print 'back'
            # self.wait.until(lambda self: self.find_element_by_xpath(u"//a[contains(text(),'Скрыть проданные')]").is_displayed())
            return False
        else:
            return True

    def delete_product(self):
        self.driver.find_element_by_xpath(be.DELETE_BTN).click()
        self.wait_element_displayed_by_xpath(be.EMPTY_BTN)


    def add_sku_count(self):
        pass


    def add_random_product(self):
        pass


    def add_modnakarta(self):
        pass

class MultiBasket(object):

    def open_basket_products(self, products):
        pass


        