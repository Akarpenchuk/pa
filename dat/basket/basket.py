# !/usr/bin/env python 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import basket_elements as be
import main_page.main_page_elements as mpe

class Basket:

    def open_basket_with_product(self):
        self.driver.find_element_by_xpath(be.BASKET_ICO).click()
        self.wait_element_displayed_by_xpath(mpe.PRODUCT)
        return True


    def open_empty_basket(self):
        self.driver.find_element_by_xpath(be.BASKET_ICO).click()
        self.wait_element_displayed_by_xpath(be.EMPTY_BASKET_ICO)
        self.driver.find_elements_by_xpath(be.EMPTY_BASKET_MSG)
        return True


    def delete_product(self):
        self.driver.find_element_by_xpath(be.DELETE_BTN).click()
        self.wait_element_displayed_by_xpath(be.EMPTY_BTN)
        self.driver.find_element_by_xpath(be.CONTINUE_SHOPING).click()
        self.wait_element_displayed_by_xpath(mpe.CAMPAIGN)
        return True


    def add_sku_count(self):
        pass

    def open_product_from_basket(self):
        pass

    def back_btn(self, last_page_element):
        self.driver.find_element_by_xpath(be.BACK_BTN).click()
        self.wait_element_displayed_by_xpath(last_page_element)
        return True

    def increase_product_count(self):
        self.current_count = self.driver.find_elements_by_xpath(be.PRODUCT_COUNT).text

        self.driver.find_element_by_xpath(be.PRODUCT_COUNT).click()
        self.wait_element_displayed_by_xpath(be.PRODUCT_COUNTER)
        self.driver.find_element_by_xpath(be.PRODUCT_COUNTER + '[' + int(self.current_count) + 1 + ']').click()
        self.wait_element_displayed_by_xpath(be.PRODUCT_COUNT)
        new_count = self.driver.find_elements_by_xpath(be.PRODUCT_COUNT)
        assert new_count == self.current_count


        