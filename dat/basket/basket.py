    # !/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from base_methods.base import BaseClass
from base_methods.wait import Wait

import basket_elements as be
import main_page.main_page_elements as mpe

class Basket:

    def open_basket_product(self, name, brand, new_price, count):
        self.click(be.BASKET_ICO)
        self.wait_element(name)
        self.find_text(brand)
        self.find_text(new_price)
        self.find_text(count)
        return True

    def open_empty_basket(self):
        self.click(be.BASKET_ICO)
        self.wait_element(be.EMPTY_BASKET_ICO)
        self.find_elements(be.EMPTY_BASKET_MSG)
        return True

    def delete_products(self):
        delete_btns = self.count_elements(be.DELETE_BTN)
        for i in xrange(delete_btns):
            self.click(be.DELETE_BTN)
            if self.wait_element(be.DELETE_BTN):
                continue
            else:
                self.wait_element(be.EMPTY_BTN)
                self.click(be.CONTINUE_SHOPING)
                self.wait_element(mpe.CAMPAIGN)
        return True

    def add_sku_count(self):
        pass

    def open_product_from_basket(self):
        pass

    def back_btn(self, last_page_element):
        self.click(be.BACK_BTN)
        self.wait_element(last_page_element)
        return True

    def increase_product_count(self):
        self.current_count = self.find_text(be.PRODUCT_COUNT).text

        self.click(be.PRODUCT_COUNT)
        self.wait_element(be.PRODUCT_COUNTER)
        self.click(be.PRODUCT_COUNTER + '[' + int(self.current_count) + 1 + ']')
        self.wait_element(be.PRODUCT_COUNT)
        new_count = self.find_elements(be.PRODUCT_COUNT)
        assert new_count == self.current_count


        