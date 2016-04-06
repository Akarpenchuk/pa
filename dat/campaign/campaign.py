# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import main_page.main_page_elements as mpe
import campaign_elements as ce

class Campaign():

    def open_campaign_iter(self):
        campaigns = self.driver.find_elements_by_xpath(mpe.CAMPAIGN)
        for i in xrange(len(campaigns)):
            i += 1
            self.driver.find_element_by_xpath(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN).click()
            if self.check_if_outlet():
                break
            continue

            product_count = self.driver.find_elements_by_xpath(ce.PRODUCT)
            assert product_count >= 1


    def check_if_outlet(self):
        #if outlet
        try:
            self.wait_element_displayed_by_xpath(ce.OUTLET_CATEGORY)
            self.driver.find_element_by_xpath(ce.OUTLET_CATEGORY).click()
            self.wait_element_displayed_by_xpath(ce.PRODUCT)
            return True
        #if simple campaign
        except:
            self.wait_element_displayed_by_xpath(ce.PRODUCT)
            return True
            return 'campaign'


    def hide_sold_filter(self):
        hide_sold = self.find(u"//div[contains(text(),'Скрыть проданные')]").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//a[contains(@href,'/product/')]").is_displayed())
        applied_hide_sold_url = self.driver.get.current_url
        assert u"sold=Скрыть проданные" in applied_hide_sold_url
