#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest
from data.page_objects import Authorization, PurchaseNonCashSelfDelivery, RecoveryEmail, PurchaseCashCourier

class Test(unittest.TestCase):

    def test_case(self):

        Authorization().auth()
        activity = PurchaseCashCourier()
        PurchaseCashCourier().select_campaign()
        PurchaseCashCourier().select_product()
        PurchaseNonCashSelfDelivery().chekcout_self_delivery()
        PurchaseNonCashSelfDelivery().checkout_card_payment()
        PurchaseNonCashSelfDelivery().checkout_self_confirm()
        PurchaseNonCashSelfDelivery().fill_card_data()
        PurchaseCashCourier().verify_order_details()
        PurchaseCashCourier().cancel_order()
        Authorization().logout()

if __name__ == "__main__":
    print 'running'
    unittest.main()