#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import psycopg2

# from campaign.campaign import Campaign

import cabinet.cabinet_elements as myinfo
import main_page_elements as mpe
import static_page.static_page_elements as stpe
import campaign.campaign_elements as ce
import base_methods.config as conf



class MainPage():

    def login(self):
        self.find(mpe.AUTH_LINK)
        self.click(mpe.AUTH_LINK)
        self.wait_element(mpe.AUTH_FORM)

        email_field = self.find(mpe.AUTH_EMAIL_INPUT)
        pass_field = self.find(mpe.AUTH_PASS_INPUT)
        auth_btn = self.find(mpe.AUTH_BTN)

        email_field.clear()
        email_field.send_keys(conf.USER_EMAIL)
        pass_field.clear()
        pass_field.send_keys(conf.USER_PASS)
        auth_btn.click()
        self.wait_element(mpe.LOGGED_IN)
        return True


    def close_app_banner(self):
        self.wait_element(mpe.APP_BANNER)
        self.find(mpe.APP_BANNER_CLOSE)

    def check_main_page_elements(self):
        lst = [mpe.LOGO,
            mpe.BANNER_PROMO,
            mpe.BANNER_TRAILER,
            mpe.BANNER_APPS,
            mpe.MENU_CATEGORIES.itervalues().next(),
            mpe.CAMPAIGN,
            mpe.SOON_END_CAMPAIGNS,
            mpe.COMING_SOON_ITEMS[0],
            mpe.COMING_SOON_ITEMS[1],
            mpe.COMING_SOON_ITEMS[2]]

            #FOOTER ITEMS

        for i in lst:
            if self.find(i):
                return True
            return False


    def check_help_menu_items(self):
        # self.find(mpe.HELP_MENU.get("MENU_HELP"))
        for i in mpe.HELP_MENU.values():
            return True
        return False
        
        self.click(mpe.PHONE)

        # check is it closed
        if self.find(mpe.HELP_MENU.values()[1]):
            return False
        return True


    def check_main_menu_items(self):
        for i in sorted(mpe.MENU_CATEGORIES.itervalues()):

            self.hover(i)
            self.wait_element(mpe.MENU_CAMPAIGN)
            menu_campaign_count = self.count_elements(mpe.MENU_CAMPAIGN)
            assert menu_campaign_count >= 1
            print 'menu_campaign_count', menu_campaign_count

            self.click(i)
            self.wait_element(mpe.LIST_CAMPAIGN_CURRENT)
            campaign_count = self.count_elements(mpe.CAMPAIGN)
            assert campaign_count >= 1
            print 'campaign_count', campaign_count

            self.hover(i)
            self.wait_element(mpe.MENU_CAMPAIGN)
            self.click(mpe.MENU_CAMPAIGN)
            self.change_to_catalogue()
            self.wait_element(ce.PRODUCT)

            continue
        return True


    def check_soon_end_campaigns(self):
        current_url = str(self.driver.current_url)
        if self.driver.current_url != conf.BASE_URL:
            self.open_main_page()

        query = "select count(*) from campaign_campaign where starts_at < now() and finishes_at < now() + interval '1 days';"
        if self.db_select(query):
            return True
        return False
        
        soon_end_camps = self.count_elements(mpe.SOON_END_CAMPAIGNS)
        print 'soon_end_camps', soon_end_camps
        print 'record', record

        assert soon_end_camps >= int(self.record)
        return True


    def check_fast_access_buttons(self): #TODO !
        for i in mpe.FAST_ACCESS_BTNS:
            print self.driver.get_window_position(windowHandle='current')
            screen_position = ["u'y': 0, u'x': 1920"] == str(self.driver.get_window_position(windowHandle='current'))
            
        #     for i in screen_position:
        #     self.find(i).click()

        #     sleep(1)
            
        #         print current_position = self.driver.get_window_position(windowHandle='current')
        #         assert i == current_position
        #     continue
        # return True


    def send_registration_email(self):
        rand_email = self.get_rand_email()
        print 'rand_email ', rand_email

        self.click(mpe.REG_LINK)
        self.wait_element(mpe.REG_FORM)
        self.send_keys(mpe.REG_EMAIL_INPUT, rand_email)
        self.send_keys(mpe.REG_PASS_INPUT, myinfo.USER_PASS)
        self.click(mpe.REG_BTN)
        if self.wait_element(mpe.REG_FORM_SEND_LOGO):
            return True
        return False


    def fill_personal_data_popup(self):
        self.find(mpe.PERSONAL_INFO_POPUP)

        name = self.find(mpe.PERSONAL_INFO_POPUP_NAME).send_keys(u"тест")
        self.find(mpe.PERSONAL_INFO_POPUP_SURNAME).send_keys(u"тест")

        self.find(mpe.PERSONAL_INFO_POPUP_DAY).click()
        self.wait
        self.find(mpe.PERSONAL_INFO_POPUP_DAY_SELECT).click()
        
        self.wait
        self.find(mpe.PERSONAL_INFO_POPUP_MONTH).click()
        self.wait
        self.find(mpe.PERSONAL_INFO_POPUP_MONTH_SELECT).click()

        self.wait
        self.find(mpe.PERSONAL_INFO_POPUP_YEAR).click()
        self.wait
        self.find(mpe.PERSONAL_INFO_POPUP_YEAR_SELECT).click()

        self.wait
        self.find(mpe.PERSONAL_INFO_POPUP_BTN).click()

        sleep(2)
        self.wait_element(mpe.HEADER_USER_NAME)

        profile_name = self.find(mpe.HEADER_USER_NAME).text
        profile_name = profile_name.encode('utf-8')

        assert profile_name in 'тест'

        return True


    def send_recovery_email(self):
        self.find(mpe.REG_LINK).click()
        self.wait_element(mpe.REG_FORM)
        self.find(mpe.RECOVERY_EMAIL_LINK).click()

        if self.wait_element(mpe.RECOVERY_EMAIL_FORM):
            sleep(1)
            self.find(mpe.RECOVERY_EMAIL_INPUT).send_keys(conf.USER_EMAIL)
            self.find(mpe.RECOVERY_EMAIL_BTN).click()
            self.wait
            if self.wait_element(mpe.REG_FORM_SEND_LOGO):
                return True
            return False


    # def open_campaign(self):
    #     camp_name = self.find(mpe.CAMPAIGN_NAME).text
    #     self.find(mpe.CAMPAIGN).click()
    #     Campaign().check_if_outlet()

    #     self.wait_element(ce.PRODUCT)
    #     assert camp_name in self.find(ce.CAMPAIGN_NAME).text
    #     product_count = self.driver.find_elements_by_xpath(ce.PRODUCT)
    #     assert product_count >= 1


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

        products_in_camp = self.find(PRODUCT_COUNTER).text

        #verify product count is changed after affiliation selecting
        if self.driver.find_elements_by_xpath(AFF_WOMAN).is_displayed():

            self.driver.find_elements_by_xpath(AFF_WOMAN).click()
            self.wait.until(lambda self: self.find_element_by_xpath(SPINNER).is_displayed())
            
            new_products_counter = self.find(PRODUCT_COUNTER)
            
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







        