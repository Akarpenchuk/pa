# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
import unittest
import logging
logging.basicConfig(filename = '/home/ace/log_webdriver', level = logging.DEBUG)

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from base_methods.base import BaseClass
from main_page.main_page import MainPage
from product.product import Product
from campaign.campaign import Campaign
from basket.basket import Basket

import main_page.main_page_elements as mpe


class Test(unittest.TestCase, BaseClass, MainPage, Product, Campaign, Basket):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)


    def testBasket(self):
        # self.open_base_url()
        
        #check basket by anonym
        # self.login_old_user()
        # self.open_empty_basket()

        # self.add_product_less_99()

        #TODO t.txt
        BaseClass(self.driver).open_base_url()
        i = 1
        while Campaign(self.driver).open_campaign_iter(i):
            Campaign(self.driver).check_product_count()
            Campaign(self.driver).sort_asc()
            Campaign(self.driver).hide_sold()
            if Campaign(self.driver).check_product_less_99():
                Campaign(self.driver).open_product_iter()
                Product(self.driver).add_product()
                break
            i += 1
            continue
        Basket(self.driver).open_basket_with_product()
        Basket(self.driver).check_product_data()
        Basket(self.driver).check_basket_less_99()



    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()