# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import base_methods.hover
import cabinet.cabinet_elements as myinfo
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
            mpe.CAMPAIGN,
            mpe.SOON_END_CAMPAIGNS,
            mpe.COMING_SOON_ITEMS[0]]

        for i in lst:
            if self.driver.find_element_by_xpath(i):
                return True
            return False


    def check_help_menu_items(self):
        self.driver.refresh()

        self.driver.find_element_by_xpath(mpe.HELP_DICT.get("MENU_HELP")).click()
        for i in mpe.HELP_DICT.values():
            return True
        return False
        
        self.driver.find_element_by_xpath(mpe.PHONE).click()

        if self.driver.find_element_by_xpath(mpe.HELP_DICT.values()[1]):
            return False
        return True


    def check_main_menu_items(self):
        for i in sorted(mpe.MENU_CATEGORIES.itervalues()):

            self.hover(i)
            self.wait_element_displayed_by_xpath(mpe.MENU_CAMPAIGN)
            menu_campaign_count = self.driver.find_elements_by_xpath(mpe.MENU_CAMPAIGN)
            assert len(menu_campaign_count) >= 1, len(menu_campaign_count)

            self.driver.find_element_by_xpath(i).click()
            self.wait_element_displayed_by_xpath(mpe.LIST_CAMPAIGN)

            campaign_name = self.driver.find_element_by_xpath(i).text
            print "campaign is ", campaign_name.encode('utf-8')
            
            self.driver.find_element_by_xpath(mpe.MENU_CAMPAIGN).click()

            #if outlet
            try:
                self.wait_element_displayed_by_xpath(ce.OUTLET_CATEGORY)
                self.driver.find_element_by_xpath(ce.OUTLET_CATEGORY).click()
                self.wait_element_displayed_by_xpath(ce.LIST_PRODUCT)
                self.driver.back()
                self.driver.back()
                self.driver.find_element_by_xpath(mpe.LIST_CAMPAIGN)
            #if simple campaign
            except:
                self.wait_element_displayed_by_xpath(ce.LIST_PRODUCT)
                self.driver.back()
                self.check_main_page_elements()
            # assert str(campaign_name) in self.driver.find_element_by_xpath(ce.CAMPAIGN_NAME).text # BUG https://jira.modnakasta.ua/browse/MK-1456
            continue
        return True


    def check_coming_soon_campaigns(self):
        '''check dates'''
        date = time.strftime("%d")
        for i in mpe.COMING_SOON_DATES:
            if date in self.driver.find_element_by_xpath(i).text:
                date = int(date) + 1
                date = str(date)
                continue

        '''check campaign count'''
        for i in mpe.COMING_SOON_ITEMS:
            assert len(self.driver.find_elements_by_xpath(i)) >= 1
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


    def check_fast_access_buttons(self): #TODO !

        for i in mpe.FAST_ACCESS_BTNS:
            print self.driver.get_window_position(windowHandle='current')
            screen_position = ["u'y': 0, u'x': 1920"] ==  str(self.driver.get_window_position(windowHandle='current'))
            
        #     for i in screen_position:
        #     self.driver.find_element_by_xpath(i).click()

        #     sleep(1)
            
        #         print current_position = self.driver.get_window_position(windowHandle='current')
        #         assert i == current_position
        #     continue
        # return True


    def send_registration_email(self):
        self.driver.find_element_by_xpath(mpe.REG_LINK).click()
        self.wait_element_displayed_by_xpath(mpe.REG_FORM)
        self.driver.find_element_by_xpath(mpe.REG_EMAIL_INPUT).send_keys(conf.RAND_EMAIL)
        self.driver.find_element_by_xpath(mpe.REG_PASS_INPUT).send_keys(conf.USER_PASS)
        self.driver.find_element_by_xpath(mpe.REG_BTN).click()
        if self.wait_element_displayed_by_xpath(mpe.REG_FORM_SEND_LOGO):
            return True
        return False


    def fill_personal_data_popup(self):
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP)

        name = self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_NAME).send_keys(u"тест")
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_SURNAME).send_keys(u"тест")

        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_DAY).click()
        self.wait
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_DAY_SELECT).click()
        
        self.wait
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_MONTH).click()
        self.wait
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_MONTH_SELECT).click()

        self.wait
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_YEAR).click()
        self.wait
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_YEAR_SELECT).click()

        self.wait
        self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_BTN).click()

        self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU)

        profile_name = self.driver.find_element_by_xpath(mpe.PROFILE_MENU).text
        profile_name = profile_name.encode('utf-8')

        assert profile_name in 'тест'

        return True


    def send_recovery_email(self):
        self.driver.find_element_by_xpath(mpe.REG_LINK).click()
        self.wait_element_displayed_by_xpath(mpe.REG_FORM)
        self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_LINK).click()

        if self.wait_element_displayed_by_xpath(mpe.RECOVERY_EMAIL_FORM):
            sleep(1)
            self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_INPUT).send_keys(conf.USER_EMAIL)
            self.driver.find_element_by_xpath(mpe.RECOVERY_EMAIL_BTN).click()
            self.wait
            if self.wait_element_displayed_by_xpath(mpe.REG_FORM_SEND_LOGO):
                return True
            return False


    def open_cabinet(self):
        login = self.driver.find_element_by_xpath(mpe.PROFILE_LINK)
        if login:
            self.driver.find_element_by_xpath(mpe.PROFILE_MENU).click()
            self.wait_element_displayed_by_xpath(mpe.PROFILE_MENU)
            self.driver.find_element_by_xpath(mpe.PROFILE_LINK).click()
            self.wait_element_displayed_by_xpath(myinfo.NAME)
            return True
        return False


    def open_campaign(self):
        camp_name = self.driver.find_element_by_xpath(mpe.CAMPAIGN_NAME).text
        self.driver.find_element_by_xpath(mpe.CAMPAIGN).click()
        self.wait_element_displayed_by_xpath(ce.PRODUCT)
        assert camp_name in self.driver.find_element_by_xpath(ce.CAMPAIGN_NAME).text
        product_count = self.driver.find_elements_by_xpath(ce.PRODUCT)
        assert product_count >= 1


    def store_campaigns_count(self):
        self.current_campaigns = self.store_elements_count(LIST_CAMPAIGN_CURRENT)
        if self.current_campaigns < 50:
            raise Exception, 'not enought current campaigns'
        return True


    def verify_affiliation_filter(self):
        #verify button is displayed
        affiliation_list = [AFF_WOMAN, AFF_MAN, AFF_CHILD, AFF_BOYS, AFF_GIRLS, AFF_HOME, AFF_UNI, AFF_ZOO]
        product_count = len(self.driver.find_elements_by_xpath(LIST_PRODUCT))
        assert product_count == LIST_PRODUCT_COUNT
        print "product_count OK"

        products_in_camp = self.driver.find_element_by_xpath(PRODUCT_COUNTER).text

        #verify product count is changed after affiliation selecting
        if self.driver.find_elements_by_xpath(AFF_WOMAN).is_displayed():

            self.driver.find_elements_by_xpath(AFF_WOMAN).click()
            self.wait.until(lambda self: self.find_element_by_xpath(SPINNER).is_displayed())
            
            new_products_counter = self.driver.find_element_by_xpath(PRODUCT_COUNTER)
            
            assert products_in_camp != new_products_counter
            print "product_count is changed"

        elif self.driver.find_elements_by_xpath(AFF_MAN).is_displayed():
            self.driver.find_elements_by_xpath(AFF_MAN).click()
        elif self.driver.find_elements_by_xpath(AFF_CHILD).is_displayed():
            self.driver.find_elements_by_xpath(AFF_CHILD).click()
        elif self.driver.find_elements_by_xpath(AFF_BOYS).is_displayed():
            self.driver.find_elements_by_xpath(AFF_BOYS).click()
        elif self.driver.find_elements_by_xpath(AFF_GIRLS).is_displayed():
            self.driver.find_elements_by_xpath(AFF_GIRLS).click()
        elif self.driver.find_elements_by_xpath(AFF_HOME).is_displayed():
            self.driver.find_elements_by_xpath(AFF_HOME).click()
        elif self.driver.find_elements_by_xpath(AFF_UNI).is_displayed():
            self.driver.find_elements_by_xpath(AFF_UNI).click()
        else:
            self.driver.find_elements_by_xpath(AFF_ZOO).is_displayed()
            self.driver.find_elements_by_xpath(AFF_ZOO).click()







        