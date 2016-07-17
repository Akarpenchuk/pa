# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
import psycopg2
import random
import string

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from base_methods.wait import Wait
from main_page.main_page import MainPage
from selenium.webdriver.common.keys import Keys

import campaign.campaign_elements as ce
import cabinet.cabinet_elements as myinfo
import main_page.main_page_elements as mpe
import mail.mail_elements as me
import base_methods.config as conf



class BaseClass():

    def login(self, user_email, user_pass):
        self.wait_element(mpe.AUTH_LINK)
        self.click(mpe.AUTH_LINK)
        self.clear(mpe.AUTH_EMAIL_INPUT)
        self.send_keys(mpe.AUTH_EMAIL_INPUT, user_email)
        sleep(1)
        self.clear(mpe.AUTH_PASS_INPUT)
        self.send_keys(mpe.AUTH_PASS_INPUT, user_pass)
        sleep(1)
        self.click(mpe.AUTH_BTN)
        self.wait_element(mpe.CAMPAIGN)
        count = 0
        while not count == 20:
            print 'while not login'
            self.wait_element(mpe.HEADER_USER_NAME)
            count += 1
            continue
        print 'login true'
        return True

    def logout(self):
        while not self.wait_element(mpe.HEADER_USER_NAME):
            print 'logout while'
            continue
        self.click(mpe.HEADER_USER_NAME)
        self.wait_element(mpe.LOGOUT_MENU_LINK)
        self.click(mpe.LOGOUT_MENU_LINK)
        self.wait_element(mpe.AUTH_LINK)
        print 'logout AUTH_LINK true'
        return True





        # if self.wait_element(mpe.PROFILE_LINK):
        #     self.click(mpe.HEADER_USER_NAME)
        #     self.wait_element(mpe.LOGOUT_MENU_LINK)
        #     self.click(mpe.LOGOUT_MENU_LINK)
        # return False
        # print 'user is anonym'

    def open_url(self, url, element):
        self.driver.get(url)
        self.wait_element(element)

    def open_main_page(self):
        self.driver.get(conf.BASE_URL)
        self.check_main_page_elements()

    def find(self, item):
        element = self.driver.find_element_by_xpath(item)
        return element

    def get_text(self, item):
        element_text = self.driver.find_element_by_xpath(item).text
        # return element_text.encode('utf-8')
        return str(element_text)

    def get_items_attributes(self, attr):
        lst = []
        items = self.count_elements(attr)
        for i in xrange(items):
            attribute = self.driver.find_element_by_xpath(item).get_attribute
            lst.append(attribute)
        print 'lst ', lst
        return lst

    def get_items_names(self, count_items, item):
        lst = []
        items = self.count_elements(count_items)
        for i in xrange(items):
            text = self.driver.find_element_by_xpath(item).text
            name = text.encode('utf-8')
            lst.append(name)
        print 'lst ', lst
        return lst
        # .encode("utf-8")


        # return elem_text.encode('utf-8')

    def find_text(self, item, text):
        elem = self.driver.find_element_by_xpath(item).text
        # elem.decode('utf-8')
        if u'text' in elem:
            return True
        return False

    def get_elements(self, items):
        elements = self.driver.find_elements_by_xpath(items)
        return elements

    def find_elements(self, items):
        elements = self.driver.find_elements_by_xpath(items)
        return True

    def find_list_elements(self, *items):
        for i in items:
            self.driver.find_element_by_xpath(i)
            return True
        return False

    def clear(self, item):
        self.driver.find_element_by_xpath(item).clear()

    def click(self, item):
        self.driver.find_element_by_xpath(item).click()

    def send_keys(self, item, data):
        self.driver.find_element_by_xpath(item).send_keys(data)

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def count_elements(self, element):
        elements = self.driver.find_elements_by_xpath(element)
        return len(elements)

    def hover(self, element):
        action = ActionChains(self.driver)
        el = self.find(element)
        action.move_to_element(el)
        action.perform()

    def switch_to_frame(self, frame):
        inbox = self.find(frame)
        self.driver.switch_to.frame(inbox)

    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def get_rand_email(self):
        RAND_EMAIL_NAME = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
        RAND_EMAIL = RAND_EMAIL_NAME + me.EMAIL_DOMAIN
        return RAND_EMAIL

    def get_rand_item_text(self, items_text):
        rand_text = random.choice(items_text)
        return rand_text

    def scroll_down(self, element):
        # self.driver.find_element_by_xpath(element).send_keys(Keys.END)
        item = self.find(element)
        item = int(item.location.get('y'))
        print 'item ', item

        while not True:
            self.driver.execute_script("document.querySelector('.products > div:last-child').scrollIntoView(true)");

            current_position = self.driver.find(element)
            current_position = int(item.location.get('y'))
            print 'current_position ', current_position

            if current_position == item:
                continue
            return True

        # self.driver.find_element_by_xpath(element).send_keys(Keys.COMMAND, Keys.END)

    def scroll_to_element(self, element):
        while not self.find(element):
            self.driver.execute_script("window.scrollTo(0, 100000);")

    def get_tooltip_product_name(self):
        if self.wait_element(ce.TOOLTIP_PRODUCT_NAME):
            name = self.find_text(ce.TOOLTIP_PRODUCT_NAME)
            return name.encode('utf-8')
        return False

    def get_tooltip_product_brand(self):
        if self.wait_element(ce.TOOLTIP_PRODUCT_BRAND):
            name = self.find_text(ce.TOOLTIP_PRODUCT_BRAND)
            return name.encode('utf-8')
        return False

    def get_tooltip_product_price(self):
        if self.wait_element(ce.TOOLTIP_PRODUCT_PRICE):
            name = self.find_text(ce.TOOLTIP_PRODUCT_PRICE)
            return name.encode('utf-8')
        return False

    def get_tooltip_product_size(self):
        if self.wait_element(ce.TOOLTIP_PRODUCT_SIZE):
            name = self.find_text(ce.TOOLTIP_PRODUCT_SIZE)
            return name.encode('utf-8')
        return False


    # def scroll_bottom_product_list(self):
    #     #check current position
    #     item = self.find(ce.LAST_PRODUCT)
    #     last_product_position = int(item.location.get('y'))
    #     print 'last_product_position ', last_product_position

    #     #check height
    #     height = self.driver.execute_script("return document.querySelector('.products > div:last-child').style.height");
    #     height = height.replace('px', '')
    #     print 'height ', height

    #     while not True:
    #         if last_product_position < height:
    #             self.driver.execute_script("document.querySelector('.products > div:last-child').scrollIntoView(true)");
    #             continue
    #         #check current position again
    #         # item = self.find(ce.LAST_PRODUCT)
    #         # print 'item while', item
    #         # last_product_position = int(item.location.get('y'))
    #         # print 'last_product_position ', last_product_position
    #     else:
    #         return True

    def db_select(self, query):
        conn_string = "host='10.38.0.122' dbname='modnakasta' user='modnakastauser' password='fai4Sag/inoo' port='5433'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        print  'Connnected to db!'
        cursor.execute(query)
        records = cursor.fetchall()
        return records

        # while current position != screen position:
        #   scroll this shit!
        #   or
        #   window.scrollTo(?, ?)

        # while pos.get('y') != page_height:
        #     print 'while'
        #     self.driver.execute_script("document.querySelector('div.products > div').style.height");

        # self.action = ActionChains(self.driver)
        # self.driver.execute_script('document.documentElement.scrollIntoView(0, 1);')
        # self.find(element)
        # self.driver.execute_script("document.querySelector('div.products > div > div > div').scrollIntoView(true)");
        # self.driver.execute_script("document.querySelector('div.products > div').style.height");
        # if self.driver.execute_script("document.querySelector('div .product_item_wrap:last-child').scrollIntoView(true)") == False