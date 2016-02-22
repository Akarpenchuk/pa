
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import main_page_elements as mpe
import static_page.static_page_elements as stpe
import campaign.campaign_elements as ce
import base_methods.config as conf



class MainPage:


    def check_main_page_elements(self):

        lst = [mpe.LOGO,
            mpe.BANNER_PROMO,
            mpe.BANNER_TRAILER,
            mpe.BANNER_APPS,
            mpe.MENU_CATEGORIES.itervalues().next(),
            mpe.LIST_CAMPAIGN,
            mpe.SOON_END_CAMPAIGNS,
            mpe.COMING_SOON_ITEM]

        for i in lst:
            if self.driver.find_element_by_xpath(i):
                return True
            return False


    def check_help_menu_items(self):

        self.driver.refresh()

        self.hover(mpe.HELP_DICT.get("MENU_HELP"))
        for i in mpe.HELP_DICT.values():
            element = self.driver.find_element_by_xpath(i)
            if element:
                return True
            return False


    def check_main_menu_items(self):

        menu_category_btn = sorted(mpe.MENU_CATEGORIES.values())

        for i in menu_category_btn:
            self.driver.find_element_by_xpath(i).click()
            self.wait_element_displayed_by_xpath(mpe.LIST_CAMPAIGN)

            self.hover(i)
            
            menu_category_campaign_count = self.driver.find_elements_by_xpath(i + '//a')
            assert len(menu_category_campaign_count) >= 1

            menu_category_campaign = self.driver.find_element_by_xpath(i + '//div//a')
            campaign_name = menu_category_campaign.text

            print "open ", campaign_name.encode('utf-8')
            
            menu_category_campaign.click()

            #if outlet
            try:
                self.wait_element_displayed_by_xpath(ce.OUTLET_CATEGORY)
                self.driver.find_element_by_xpath(ce.OUTLET_CATEGORY).click()
                self.wait_element_displayed_by_xpath(ce.LIST_PRODUCT)

            #if simple campaign
            except:
                self.driver.find_element_by_xpath(ce.LIST_PRODUCT)

            # assert str(campaign_name) in self.driver.find_element_by_xpath(ce.CAMPAIGN_NAME).text # BUG https://jira.modnakasta.ua/browse/MK-1456

            self.driver.back()
            self.driver.find_element_by_xpath(mpe.LIST_CAMPAIGN)
            continue
        return True

    def check_coming_soon_campaigns(self):

        assert self.elements_count(mpe.COMING_SOON_COLUMNS) == 3

        date = time.strftime("%d")

        for i in mpe.COMING_SOON_DATES:
            if date in self.driver.find_element_by_xpath(i).text:
                date = int(date) + 1
                date = str(date)          
                continue
        return True

    def check_soon_end_campaigns(self):
        
        self.open_base_url()
        assert self.driver.find_elements_by_xpath(mpe.SOON_END_CAMPAIGNS) >= 3

        soon_end_camps = self.driver.find_elements_by_xpath(mpe.SOON_END_CAMPAIGNS)
        campaigns_time = self.driver.find_elements_by_xpath(mpe.SOON_END_CAMPAIGN_TIME)
        count = 1

        for i in xrange(len(soon_end_camps)):
            print count

            self.hover(mpe.SOON_END_CAMPAIGNS + '[%d]' % count)
            time = self.driver.find_element_by_xpath(mpe.SOON_END_CAMPAIGNS + '[%d]' % count + "//div[@class='timer_time']").text
            # time = time.encode('utf-8')
            count += 1
            if '0' in time.encode('utf-8'):
                continue
        return True


    def check_fast_access_buttons(self):

        fast_btns = self.driver.find_elements_by_xpath(mpe.FAST_ACCESS_BTNS)
        
        count = 3
        for i in xrange(3):
            self.driver.find_element_by_xpath(mpe.FAST_ACCESS_BTNS + "[%d]/a" % count).click()
            sleep(1)
            self.driver.find_element_by_xpath(mpe.COMING_SOON_ITEM)
            count += 1
            continue
        return True

    def send_registration_email(self):

        self.driver.find_element_by_xpath(mpe.REG_LINK).click()
        self.wait_element_displayed_by_xpath(mpe.REG_FORM)
        self.driver.find_element_by_xpath(mpe.REG_EMAIL_INPUT).send_keys(conf.RAND_EMAIL)
        print conf.RAND_EMAIL

        self.driver.find_element_by_xpath(mpe.REG_PASS_INPUT).send_keys(conf.USER_PASS)
        self.driver.find_element_by_xpath(mpe.REG_BTN).click()
        if self.wait_element_displayed_by_xpath(mpe.REG_FORM_SEND_LOGO):
            return True
        return False


        