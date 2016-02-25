# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from base_methods.base import BaseClass
from dat.landing_page.landing import Landing

import dat.base_methods.config as conf
import dat.landing_page.landing_elements as le


class Test(unittest.TestCase, BaseClass, Landing):

    def setUp(self):

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.wait = WebDriverWait(self.driver, 10)

    def test_case(self):

        driver = webdriver.Chrome()

        Anonym(driver).preconditions()
        Auth(driver).auth_form()

        Campaign(driver).select_campaign()

        Product(driver).select_product()
        Product(driver).select_size()
        Product(driver).open_basket_btn()

        DeliveryStep(driver).delivery_courier_cash_1sku()
        PaymentStep(driver).payment_courier_cash_1sku()
        ConfirmStep(driver).confirm_courier_cash_1sku()
        CompleteStep(driver).complete_page()
        
        PersonalInfo().verify_order_details()
        Mail(driver).verify_ordered_order_email()
        PurchaseCashCourier().cancel_order()
        Authorization().logout()

        driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()