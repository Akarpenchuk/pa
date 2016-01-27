#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest
from data.page_objects import Authorization, PurchaseCashPost, RecoveryEmail, PurchaseCashCourier

class Test(unittest.TestCase):

    def test_case(self):

        Authorization().auth()
        PurchaseCashCourier().select_campaign()
        PurchaseCashCourier().select_product()
        PurchaseCashPost().checkout_post_delivery()
        PurchaseCashPost().checkout_post_payment()
        PurchaseCashPost().checkout_post_confirm()
        PurchaseCashPost().verify_order_details()
        PurchaseCashPost().cancel_order()
        Authorization().logout()

if __name__ == "__main__":
    print 'running'
    unittest.main()