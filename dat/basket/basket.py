# !/usr/bin/env python 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data.config import *
from ..campaign.campaign import Campaign
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string

class Basket:
    '''"Static data for use in tests'''

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def open_basket():
        self.driver.find_element_by_xpath().click()
        self.wait.until(lambda self: find_element_by_xpath().is_displayed())

    def verify_basket_product(self):
        verify_brand = self.driver.find_element_by_xpath("//div[@class='cabinet_cells'][%s]/div/p/a[contains(text(),'%d')]" % self.count_added_products, self.brand).is_displayed()
        print 'brand', self.brand
        print 'count_added_products', self.count_added_products

    def assert_less_99(self):
        basket_sum = self.driver.find_element_by_xpath("//span[@id='basket_total_sum']").text
        float(basket_sum)
        # try:
        while basket_sum <= 98:
            self.driver.back()
            print 'back'
            # self.wait.until(lambda self: self.find_element_by_xpath(u"//a[contains(text(),'Скрыть проданные')]").is_displayed())
            return False
        else:
            return True



# def select_product(self):

#     s = 1
#     price = self.driver.find_element_by_xpath("//div[@class='row'][%s]//div[@class='shop_new_cost']/span" % s).text

#     print  'price', int(price)

#     global brand
#     global name
#     global new_cost
#     global old_cost
#     global size

#     while True:
#         if int(price) < 99:
#             print 'while'
#             print price
#             s += 1
#             print 's', s
#             price = self.driver.find_element_by_xpath("//div[@class='row'][%s]//div[@class='shop_new_cost']/span" % s).text
#             print price
#             continue
#         if int(price) >= 99:
#                 print 's', s
#                 self.wait.until(lambda self: self.driver.find_element_by_xpath("//div[@class='row'][%s]/div[@class='shop_item']/a" % s).is_displayed())
#                 self.driver.find_element_by_xpath("//div[@class='row'][%s]/div[@class='shop_item']/a" % s).click()
#                 self.wait
#                 print 'product >= 99'

#                 #IF PRODUCT SOLD - CHECK OTHER
#                 try:
#                     self.driver.find_element_by_xpath("//span[@class='btn btn_red btn_disabled product_basket_btn']").is_displayed()
#                     print 'sold_true'
#                     s += 1
#                     print 's', s
#                     self.driver.back()
#                     self.wait
#                     continue
#                 except:
#                     print 'next try'
#                 try:
#                     self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").is_displayed()
#                     print 'size is_present'
#                     self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div[contains(@class,'button_on')]").click()
#                     print 'click size btn'
#                     self.wait

#                     #store product data
#                     brand = self.driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
#                     name = self.driver.find_element_by_xpath(u"//div[@class='product_name']").text
#                     new_cost = self.driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
#                     old_cost = self.driver.find_element_by_xpath("//div[@class='product_old_cost']").text
#                     size = self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").text

#                     self.driver.find_element_by_xpath(u"//a[contains(.,'В корзину')]").click()
#                     print 'click basket btn'
#                     self.wait
#                     print 'added to basket'
#                     break
#                 except:
#                     print 'first exception'

#                 #ONE SIZE
#                 try:
#                     self.driver.find_element_by_xpath("//div[@class='inner_content product_card']/div[@class='product_sizes']/div[@class='product_sizes']/div[@class='product_size_item sizes__button_chosen sizes__button_on ']").is_displayed()
#                     print 'selected size is_displayed'

#                     #store product data
#                     brand = self.driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
#                     name = self.driver.find_element_by_xpath(u"//div[@class='product_name']").text
#                     new_cost = self.driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
#                     old_cost = self.driver.find_element_by_xpath("//div[@class='product_old_cost']").text
#                     size = self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").text

#                     self.driver.find_element_by_xpath("//a[@class='btn btn_red product_basket_btn  ']").click()
#                     Webself.driverself.wait(self.self.driver, 10)
#                     print 'added to basket'
#                     # break
#                 except:
#                     print 'second exception'

#                 #NO SIZE
#                 try:
#                     self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='clear']/following-sibling::div[@class='clear']").is_displayed()
#                     print 'no size is_displayed'

#                     #store product data
#                     brand = self.driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
#                     name = self.driver.find_element_by_xpath(u"//div[@class='product_name']").text
#                     new_cost = self.driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
#                     old_cost = self.driver.find_element_by_xpath("//div[@class='product_old_cost']").text

#                     self.driver.find_element_by_xpath("//a[@class='btn btn_red product_basket_btn  ']").click()
#                     self.wait
#                     print 'added to basket'
#                     break
#                 except:
#                     print 'third exception'
#                     print 'sold_product'
#                 self.driver.back()
#                 self.wait
#                 s += 1
#                 print 's', s
#                 continue
#         break
#         print 'added to basket'
#         self.wait

#     print 'brand', brand.encode('utf-8')
#     print 'name', name.encode('utf-8')
#     print 'new_cost', new_cost
#     print 'old_cost', old_cost
#     print 'size'

#     if len(name) >= 30:
#         name = name[:30]
#         print 'name', name.encode('utf-8')
#     else:
#         pass

#     self.wait.until(lambda self: self.driver.find_element_by_xpath(u"//h1[contains(text(),'Корзина')]").is_displayed())
#     self.driver.find_element_by_xpath(u"//div[@class='container inner_container container_basket']/h1[contains(text(),'Корзина')]")
#     self.driver.find_element_by_xpath("//div[@class='table_cell cart_photo']").is_displayed()
#     self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % brand)
#     self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % name)
#     self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % new_cost)
#     print 'basket ok'