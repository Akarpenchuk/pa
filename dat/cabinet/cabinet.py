# !/usr/bin/env python 
# -*- coding: utf-8 -*-


import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import main_page.main_page_elements as mpe
import cabinet_elements as myinfo
import base_methods.config as conf



class PersonalInfo:

    def check_personal_data(self):
        name = self.driver.find_element_by_xpath(myinfo.NAME).text
        name.encode("utf-8")
        assert name in u'тест'

        surname = self.driver.find_element_by_xpath(myinfo.SURNAME).text
        surname.encode("utf-8")
        assert surname in u'тест'

        email = self.driver.find_element_by_xpath(myinfo.EMAIL).text
        assert email in conf.RAND_EMAIL

        gender = self.driver.find_element_by_xpath(myinfo.GENDER).text
        gender.encode('utf-8')
        assert gender in u'Женский'

        day = self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_DATE).text
        assert day in "3"

        month = self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_MONTH).text
        month.encode('utf-8')
        assert month in u"Март"

        year = self.driver.find_element_by_xpath(mpe.PERSONAL_INFO_POPUP_YEAR).text
        assert year in u"1916"

        phone = self.driver.find_element_by_xpath(myinfo.PERSONAL_INFO_PHONE).text
        assert phone == ""
        return True


    def verify_user_email(self):
        open_cabinet = self.driver.find_element_by_xpath("//a[@href='/me/']").click()
        self.wait
        print RAND_EMAIL
        verify_email = self.driver.find_element_by_xpath("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % RAND_EMAIL)
        click_logout_link = self.driver.find_element_by_xpath("//a[@href='/user/registration/logout/']").click()
        self.wait.until(lambda self: self.find_element_by_xpath(u"//span[contains(text(),'Регистрация')]").is_displayed())

    def verify_bot_email(self, BOT_NAME):
        open_cabinet = self.driver.find_element_by_xpath("//a[@href='/me/']").click()
        self.wait._timeout = 60
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % (BOT_NAME + EMAIL_ADDRESS)).is_displayed())
        # verify_email = self.driver.find_element_by_xpath("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % (BOT_NAME + EMAIL_ADDRESS))
        self.wait.until(lambda self: self.find_element_by_xpath("//a[@href='/user/registration/logout/']").is_displayed())
        click_logout_link = self.driver.find_element_by_xpath("//a[@href='/user/registration/logout/']").click()
        self.wait
        self.wait.until(lambda self: self.find_element_by_xpath(u"//span[contains(text(),'Регистрация')]").is_displayed())



# def check_personal_email(self):
        
#         self.driver.find_element_by_xpath("//a[@href='/me/']").click()
#         self.wait
#         self.driver.find_element_by_xpath("//div[@class='personal_info_left']/div[1]/input[@value='%s']" % self.user_email)
#         self.driver.find_element_by_xpath("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % self.user_email)
#         self.driver.find_element_by_xpath("//div[@class='personal_info_right']/div[1]/input[@value='%s']" % self.user_email)
#         print 'user has been registered'

    def verify_order_details(self):

        profile = self.driver.find_element_by_xpath("//a[@href='/me/']")
        orders = self.driver.find_element_by_xpath("//div[@class='user_menu profile_menu']/div/ul/li[1]/a")
        self.action.move_to_element(profile)
        self.wait
        self.action.click(orders)
        self.wait
        self.action.perform()
        self.wait

        #verify order
        print 'self.campaign', self.campaign.encode('utf-8')
        self.driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div/a[contains(text(),'%s')]" % self.campaign)
        self.driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a[contains(text(),'%s')]" % order).is_displayed()
        self.driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_status']/a[contains(text(),'Заказ оформлен')]").is_displayed()
        self.driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a").click()
        self.wait

        campaign_name = self.driver.find_element_by_xpath("//div[@class='order_details_block']/div[1]").text
        print campaign_name.encode('utf-8')
        assert (u'Акция: '+self.campaign) in campaign_name

        order_number = self.driver.find_element_by_xpath("//div[@class='order_details_block']/div[3]").text
        print 'order', order
        assert (u'Номер заказа: '+order) in order_number

        status = self.driver.find_element_by_xpath(u"//div[@class='order_details_block']/div[4]/span[@class='order_details_title__data']").text
        print 'status', status.encode('utf-8')
        assert u'Заказ оформлен' in status

# def verify_product_info(self):
#   pass

# def cancel_order(self):
#     cancellation = self.driver.find_element_by_xpath(u"//a[contains(text(),'Отменить')]").click()
#     self.wait
#     self.driver.find_element_by_xpath(u"//a[contains(text(),'Да')]").click()
#     self.wait
#     self.driver.find_element_by_xpath(u"//p[contains(text(),'Ваш запрос на отмену принят.')]").is_displayed()
#     self.driver.find_element_by_xpath(u"//select[@id='id_reason']").click()
#     self.wait
#     self.driver.find_element_by_xpath("//select[@id='id_reason']/option[3]").click()
#     self.wait
#     self.driver.find_element_by_xpath(u"//a[contains(text(),'Вернуться к покупкам')]").click()
#     self.wait.until(lambda self: self.driver.find_element_by_xpath("//div[@class='row']/div[@class='column_item column_1']/a").is_displayed())
#     print 'order is cancelled'