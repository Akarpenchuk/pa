# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
import psycopg2

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from base_methods.wait import Wait
from main_page.main_page import MainPage
from selenium.webdriver.common.keys import Keys

import campaign.campaign_elements as ce
import cabinet.cabinet_elements as myinfo
import main_page.main_page_elements as mpe
import base_methods.config as conf



class BaseClass():

    def open_url(self, url):
        self.driver.get(url)
        self.check_main_page_elements()

    def find(self, item):
        element = self.driver.find_element_by_xpath(item)
        return element

    def find_text(self, item):
        element_text = self.driver.find_element_by_xpath(item).text
        return element_text

    def find_text_few_elements(self, item, new_item):
        element_text = self.driver.find_element_by_xpath(item + new_item).text
        return element_text

    def find_elements(self, items):
        elements = self.driver.find_elements_by_xpath(items)
        return elements

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

    def scroll_down(self, element):
        self.driver.find_element_by_xpath(element).send_keys(Keys.COMMAND, Keys.END)

    def scroll_to_element(self, element):
        while not self.find(element):
            self.driver.execute_script("window.scrollTo(0, 100000);")

    def scroll_bottom_product_list(self):
        #check current position
        item = self.find(ce.LAST_PRODUCT)
        item = item.location
        last_product_position = item.get('y')
        last_product_position = int(last_product_position)
        print 'last_product_position ', last_product_position

        #check height
        height = self.driver.execute_script("return document.querySelector('.products > div:last-child').style.height");
        height = height.replace('px', '')
        print 'height ', height

        while last_product_position < height:
            self.driver.execute_script("document.querySelector('.products > div:last-child').scrollIntoView(true)");

            #check current position again
            item = self.find(ce.LAST_PRODUCT)
            item = item.location
            last_product_position = item.get('y')
            last_product_position = int(last_product_position)
            print 'last_product_position ', last_product_position
        else:
            return True

    def db_select(self, query):
        conn_string = "host='10.38.0.122' dbname='modnakasta' user='modnakastauser' password='fai4Sag/inoo' port='5433'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        print  'Connnected from config to -> %s' % (conn_string)
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