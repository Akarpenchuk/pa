# !/usr/bin/env python 
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import main_page.main_page_elements as mpe
import cabinet_elements as myinfo
import base_methods.config as conf



class Cabinet():

    def open_cabinet(self):
        self.click(mpe.HEADER_USER_NAME)
        self.wait_element(mpe.PROFILE_LINK)
        self.click(mpe.PROFILE_LINK)
        self.wait_element(myinfo.PERSONAL_INFO_BLOCK)
        return True

    def fill_personal_popup(self):
        name = self.get_rand_name()
        surname = self.get_rand_name()

        if self.wait_element(myinfo.PROFILE_POPUP):
            self.send_keys(myinfo.PROFILE_POPUP_NAME, name)
            self.send_keys(myinfo.PROFILE_POPUP_SURNAME, surname)
            
            #set random date
            dates = self.get_items_names(myinfo.PROFILE_POPUP_DATES)
            date = self.get_rand_item_text(dates)
            lst_item = myinfo.PROFILE_POPUP_DATE_BLOCK + myinfo.LST_ITEM + '[@text()=' + "'" + date + "']"
            print 'lst_item ', lst_item

            self.click(myinfo.PROFILE_POPUP_DATE_BLOCK)
            self.wait_element(lst_item)
            self.click(lst_item)
            selected_date = self.get_text(myinfo.PROFILE_POPUP_DATE_SELECTED)
            if selected_date in lst_item:
                return True
            return False

            #set random month
            dates = self.get_items_names(myinfo.PROFILE_POPUP_DATES)
            date = self.get_rand_item_text(dates)
            lst_item = myinfo.PROFILE_POPUP_DATE_BLOCK + myinfo.LST_ITEM + '[@text()=' + "'" + date + "']"
            print 'lst_item ', lst_item

            self.click(myinfo.PROFILE_POPUP_DATE_BLOCK)
            self.wait_element(lst_item)
            self.click(lst_item)
            selected_date = self.get_text(myinfo.PROFILE_POPUP_DATE_SELECTED)
            if selected_date in lst_item:
                return True
            return False

            #set random year
            dates = self.get_items_names(myinfo.PROFILE_POPUP_DATES)
            date = self.get_rand_item_text(dates)
            lst_item = myinfo.PROFILE_POPUP_DATE_BLOCK + myinfo.LST_ITEM + '[@text()=' + "'" + date + "']"
            print 'lst_item ', lst_item

            self.click(myinfo.PROFILE_POPUP_DATE_BLOCK)
            self.wait_element(lst_item)
            self.click(lst_item)
            selected_date = self.get_text(myinfo.PROFILE_POPUP_DATE_SELECTED)
            if selected_date in lst_item:
                return True
            return False

            #set random gender
            dates = self.get_items_names(myinfo.PROFILE_POPUP_DATES)
            date = self.get_rand_item_text(dates)
            lst_item = myinfo.PROFILE_POPUP_DATE_BLOCK + myinfo.LST_ITEM + '[@text()=' + "'" + date + "']"
            print 'lst_item ', lst_item

            self.click(myinfo.PROFILE_POPUP_DATE_BLOCK)
            self.wait_element(lst_item)
            self.click(lst_item)
            selected_date = self.get_text(myinfo.PROFILE_POPUP_DATE_SELECTED)
            if selected_date in lst_item:
                return True
            return False

    def fill_password_reset_popup(self):
        self.send_keys(myinfo.PWD_RESET_FST_INPUT, myinfo.USER_PASS)
        self.send_keys(myinfo.PWD_RESET_SND_INPUT, myinfo.USER_PASS)
        self.wait_element(myinfo.PWD_RESET_SAVE_BTN)
        self.click(myinfo.PWD_RESET_SAVE_BTN)
        sleep(2)
        self.wait_element(mpe.AUTH_FORM)      

    def check_personal_data(self, name='', surname='', email='', date='', month='', year='', gender='', phone=''):
        self.wait_element(myinfo.NAME)
        
        self.find_text(myinfo.NAME, name)
        self.find_text(myinfo.SURNAME, surname)
        self.find_text(myinfo.EMAIL, email)
        self.find_text(myinfo.DATE, date)
        self.find_text(myinfo.MONTH, month)
        self.find_text(myinfo.YEAR, year)
        self.find_text(myinfo.GENDER, gender)
        self.find_text(myinfo.PHONE, phone)

    def logout_cabinet(self):
        self.wait_element(mpe.CABINET_HEADER_USER_NAME)
        self.click(mpe.CABINET_HEADER_USER_NAME)
        # self.wait_element(myinfo.PROFILE_LOGOUT_LINK)
        sleep(1)
        self.click(myinfo.PROFILE_LOGOUT_LINK)
        if self.wait_element(mpe.AUTH_LINK):
            return True
        return False


    def check_user_email(self):
        open_cabinet = self.find("//a[@href='/me/']").click()
        self.wait
        print RAND_EMAIL
        check_email = self.find("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % RAND_EMAIL)
        click_logout_link = self.find("//a[@href='/user/registration/logout/']").click()
        self.wait.until(lambda self: self.find_element(u"//span[contains(text(),'Регистрация')]").is_displayed())


    def check_bot_email(self, BOT_NAME):
        open_cabinet = self.find("//a[@href='/me/']").click()
        self.wait._timeout = 60
        self.wait.until(lambda self: self.find_element("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % (BOT_NAME + EMAIL_ADDRESS)).is_displayed())
        # check_email = self.find("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % (BOT_NAME + EMAIL_ADDRESS))
        self.wait.until(lambda self: self.find_element("//a[@href='/user/registration/logout/']").is_displayed())
        click_logout_link = self.find("//a[@href='/user/registration/logout/']").click()
        self.wait
        self.wait.until(lambda self: self.find_element(u"//span[contains(text(),'Регистрация')]").is_displayed())


    def check_order_details(self):
        profile = self.find("//a[@href='/me/']")
        orders = self.find("//div[@class='user_menu profile_menu']/div/ul/li[1]/a")
        self.action.move_to_element(profile)
        self.wait
        self.action.click(orders)
        self.wait
        self.action.perform()
        self.wait

        #check order
        print 'self.campaign', self.campaign.encode('utf-8')
        self.find(u"//div[@class='cabinet_cells cabinet_orders_cells']/div/a[contains(text(),'%s')]" % self.campaign)
        self.find("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a[contains(text(),'%s')]" % order).is_displayed()
        self.find(u"//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_status']/a[contains(text(),'Заказ оформлен')]").is_displayed()
        self.find("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a").click()
        self.wait

        campaign_name = self.find("//div[@class='order_details_block']/div[1]").text
        print campaign_name.encode('utf-8')
        assert (u'Акция: '+self.campaign) in campaign_name

        order_number = self.find("//div[@class='order_details_block']/div[3]").text
        print 'order', order
        assert (u'Номер заказа: '+order) in order_number

        status = self.find(u"//div[@class='order_details_block']/div[4]/span[@class='order_details_title__data']").text
        print 'status', status.encode('utf-8')
        assert u'Заказ оформлен' in status