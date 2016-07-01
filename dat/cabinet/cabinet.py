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

    def check_personal_data(self):
        name = self.find(myinfo.NAME).text
        name.encode("utf-8")
        assert name in u'тест'

        surname = self.find(myinfo.SURNAME).text
        surname.encode("utf-8")
        assert surname in u'тест'

        email = self.find(myinfo.EMAIL).text
        assert email in conf.RAND_EMAIL

        gender = self.find(myinfo.GENDER).text
        gender.encode('utf-8')
        assert gender in u'Женский'

        day = self.find(myinfo.PERSONAL_INFO_DAY).text
        assert day in "2"

        month = self.find(myinfo.PERSONAL_INFO_MONTH).text
        month.encode('utf-8')
        assert month in u"Февраль"

        year = self.find(myinfo.PERSONAL_INFO_YEAR).text
        assert year in u"1916"

        phone = self.find(myinfo.PERSONAL_INFO_PHONE).text
        assert phone == ""
        sleep(2)
        return True


    def logout_cabinet(self):
        self.wait_element(mpe.CABINET_HEADER_USER_NAME)
        self.click(mpe.CABINET_HEADER_USER_NAME)
        # self.wait_element(myinfo.PROFILE_LOGOUT_LINK)
        sleep(1)
        self.click(myinfo.PROFILE_LOGOUT_LINK)
        if self.wait_element(mpe.AUTH_LINK):
            return True
        return False


    def verify_user_email(self):
        open_cabinet = self.find("//a[@href='/me/']").click()
        self.wait
        print RAND_EMAIL
        verify_email = self.find("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % RAND_EMAIL)
        click_logout_link = self.find("//a[@href='/user/registration/logout/']").click()
        self.wait.until(lambda self: self.find_elementfind(u"//span[contains(text(),'Регистрация')]").is_displayed())


    def verify_bot_email(self, BOT_NAME):
        open_cabinet = self.find("//a[@href='/me/']").click()
        self.wait._timeout = 60
        self.wait.until(lambda self: self.find_elementfind("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % (BOT_NAME + EMAIL_ADDRESS)).is_displayed())
        # verify_email = self.find("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % (BOT_NAME + EMAIL_ADDRESS))
        self.wait.until(lambda self: self.find_elementfind("//a[@href='/user/registration/logout/']").is_displayed())
        click_logout_link = self.find("//a[@href='/user/registration/logout/']").click()
        self.wait
        self.wait.until(lambda self: self.find_elementfind(u"//span[contains(text(),'Регистрация')]").is_displayed())


    def verify_order_details(self):
        profile = self.find("//a[@href='/me/']")
        orders = self.find("//div[@class='user_menu profile_menu']/div/ul/li[1]/a")
        self.action.move_to_element(profile)
        self.wait
        self.action.click(orders)
        self.wait
        self.action.perform()
        self.wait

        #verify order
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