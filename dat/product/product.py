# !/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from ..config import *

class Product:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.action = ActionChains(driver)

    def select_product(self):
        global LIST_PRODUCT
        product_card_count = self.driver.find_elements_by_xpath(LIST_PRODUCT)
        for i in xrange(len(product_card_count)):
            print "1 product_card_count"
            product_count = 1
            while True:
                print "2 while true"

                if self.driver.find_element_by_xpath(LIST_PRODUCT + LIST_PRODUCT_PRICE_NEW) < 99 or self.driver.find_elements_by_xpath(LIST_PRODUCT + LIST_PRODUCT_RESERVED) or self.driver.find_elements_by_xpath(LIST_PRODUCT + LIST_PRODUCT_SOLD):
                    print "3 if < 99"
                    product_count += 1
                    print "5 product_count", product_count
                    LIST_PRODUCT = LIST_PRODUCT[:37] + str(product_count) + ']'
                    print "NEXT LIST_PRODUCT", LIST_PRODUCT
                    continue
                else:
                    list_product_brand = self.driver.find_element_by_xpath(LIST_PRODUCT + LIST_PRODUCT_BRAND).text
                    list_product_name = self.driver.find_element_by_xpath(LIST_PRODUCT + LIST_PRODUCT_NAME).text

                    print "list_product_brand", list_product_brand.encode("utf-8")
                    print "list_product_name", list_product_name.encode("utf-8")

                    self.driver.find_element_by_xpath(LIST_PRODUCT + LIST_PRODUCT_CARD).click()
                    self.wait
                    print "6 wait product brand"
                    self.driver.find_element_by_xpath("//div[contains(text(),'%s')]" % list_product_brand.encode("utf-8"))
                    print "6 chck brand in product"
                return False

    def select_size(self):
        if self.driver.find_element_by_xpath(PRODUCT_SIZE_AVAILABLE):
            self.driver.find_element_by_xpath(PRODUCT_SIZE_AVAILABLE).click()
            self.driver.find_element_by_xpath(PRODUCT_SIZE_SELECTED).is_displayed()

        self.driver.find_element_by_xpath(PRODUCT_ADD_ENABLED).click()
        self.wait.until(lambda self: self.find_element_by_xpath(POP_SKU_ADDED).is_displayed())
        print 'product added'

    def open_basket_btn(self):
        self.driver.find_element_by_xpath(POP_OPEN_BASKET_BTN).click()
