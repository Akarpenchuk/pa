# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data.main_page.main_page import Anonym
from data.main_page.main_page import Auth
from data.campaign.campaign import Campaign
from data.product.product import Product
from data.config import *

class Test(unittest.TestCase):
    
    def test_case(self):

        driver = webdriver.Firefox()

        Anonym(driver).preconditions()
        
        Campaign(driver).select_campaign()
        Campaign(driver).verify_affiliation_filter()



if __name__=="__main__":
    print "running"
    unittest.main()
