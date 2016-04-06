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


class Test(unittest.TestCase, BaseClass, MainPage, Product, Campaign):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)


    def testBasket(self):
        self.open_base_url()
        self.login_old_user()
        self.add_product_less_99()

        self.driver.find_elements_by_xpath(mpe.LOGO).click()

        # self.assertTrue(self.add_product())
        

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()