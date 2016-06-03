# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
import unittest
import logging
logging.basicConfig(filename = '/home/ace/log_webdriver', level = logging.DEBUG)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from main_page.main_page import MainPage
from base_methods.wait import Wait
from product.product import Product
from campaign.campaign import Campaign
from basket.basket import Basket

import main_page.main_page_elements as mpe
import product.product_page_elements as ppe
import campaign.campaign_elements as ce
import basket.basket_elements as be


class Test(unittest.TestCase, BaseClass, Wait, MainPage, Product, Campaign, Basket):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        # self.wait = WebDriverWait(self.driver, 10)

    def testBasketLess99(self):
        self.open_base_url()
        
        self.login_old_user()
        self.open_empty_basket()

        self.add_product_less_99()
        self.login()
        n = 1
        while self.open_campaign_iter(n):
            self.hide_sold()
            self.sort_asc()
            self.scroll_bottom_product_list()
            if self.check_product_less_99():
                self.open_product_iter()
                self.add_product()
            break
            n += 1
            self.open_base_url()
            continue

        print 'step 2'
        self.open_basket_with_product()
        print 'step 3'
        self.check_product_data()
        self.check_basket_less_99()

        #! DELETE PRODUCT
        #! OPEN MAIN PAGE


    # def testBasketDeleteOneProduct(self):
    #     i = 1
    #     while self.open_campaign_iter(i):
    #         self.hide_sold()
    #         if self.open_product_iter():
    #             if self.add_product():
    #                self.open_basket_product(name, brand, new_price, count)
        #         return i += 1
    #     continue
    #     i += 1
    #     continue
    #     Basket().delete_product()


    # def testBasketIncreaseProductCount(self):
    #     self.open_campaign_iter()
    #     Campaign().hide_sold()
    #     while Campaign().open_product_iter():
    #         while Product().product_count_more_than_1() and Product(self.driver).add_product():
    #             Basket().open_baskte_product()
    #             break
    #         continue
    #     Basket().increase_product_count()

    # def testBasketDeleteOneOfTwoProducts(self, driver):
    #     BaseClass().open_base_url()
    #     Campaign().open_campaign_iter()
    #     Campaign().hide_sold()
    #     while Campaign().open_product_iter():
    #         if Product().add_product():
    #             BaseClass().back()
    #             Product().add_product()
    #             Basket().open_basket_products()
    #         return False
    #         continue
    #     Basket(self.driver).delete_product()

    # def testBasketDecreaseProductCount(self):
        # self.open_campaign_iter()
        # self.hide_sold()
        # while self.open_product_iter():
        # while self.count_less_than_1() and self.add_product():
            # self.open_baskte_product()
            # break
        # continue
        # Basket().increase_product_count()
        
    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()