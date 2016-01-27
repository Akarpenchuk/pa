# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data.main_page.main_page import Anonym
from data.main_page.main_page import Auth
from data.campaign.campaign import Campaign
from data.product.product import Product
from data.basket.basket import Basket
from data.checkout.checkout import DeliveryStep
from data.checkout.checkout import PaymentStep
from data.checkout.checkout import ConfirmStep
from data.checkout.checkout import CompleteStep
from data.mail.mail import Mail
from data.cabinet.cabinet import PersonalInfo
from data.config import *

class Test(unittest.TestCase):
    """Verify order creation and cancellation path """

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