# !/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data.config import *
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class DeliveryStep:

    def __init__(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 20)
        action = ActionChains(driver)

    def add_address(self):
        pass

    def select_address(self):
        pass

    def change_address(self):
        pass

    def select_department(self):
        pass

    def change_department(self):
        pass

    def select_self_pick(self):
        pass

    def change_self_pick(self):
        pass

    def delivery_courier_cash_1sku(self):
        self.driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
        self.wait.until(lambda self: self.driver.find_element_by_xpath("//input[@id='fsr_1']").is_displayed())

        #verify order details
        total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
        delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
        order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

        self.driver.find_element_by_xpath("//input[@id='fsr_1']").click()
        self.wait
        self.driver.find_element_by_xpath("//form[@id='address_form_choose']/div[last()]/input").click()
        self.wait
        self.driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
        self.wait.until(lambda self: self.driver.find_element_by_xpath("//input[@id='pm_1']").is_displayed())
        print 'fisrt step is ok'

    def delivery_post_cash_bonus_1sku(self):
        pass

class PaymentStep:

    def __init__(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 20)
        action = ActionChains(driver)

    def payment_courier_cash_1sku(self): 
        self.driver.find_element_by_xpath("//input[@id='pm_1']").click()
        self.wait

        #verify order details
        total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
        delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'%s')]" % delivery_courier)
        total_order_sum = int(new_cost) + int(delivery_courier)
        print total_order_sum
        order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % total_order_sum)

        self.driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
        print 'second step ok'

    def payment_post_cash_bonus_1sku(self):
        pass

class ConfirmStep:

    def __init__(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 20)
        action = ActionChains(driver)

    def confirm_courier_cash_1sku(self):
        #verify product details        
        self.driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
        self.driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
        self.driver.find_element_by_xpath("//div[contains(@class,'pri_category') and text()='%s']" % name)
        self.driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)

        #verify order details
        total_order_sum = int(new_cost) + int(delivery_courier)
        print total_order_sum
        self.driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
        self.driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_courier)
        self.driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
        self.driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
        self.wait.until(lambda self: self.driver.find_element_by_xpath("//h2[@class='complete__order']/strong").is_displayed())
        print 'third step ok'

    def confirm_post_cash_bonus_1sku(self):
        pass

class CompleteStep:

    def __init__(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 20)
        action = ActionChains(driver)

    def complete_page(self):
        order = self.driver.find_element_by_xpath("//h2[@class='complete__order']/strong").text
        print 'order', order

# class PurchaseCashPost:

#     def checkout_post_delivery(self):

#         self.self.driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
#         self.self.wait.until(lambda self: self.self.driver.find_element_by_xpath("//input[@id='fsr_3']").is_displayed())

#         #verify order details
#         total_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
#         order_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

#         self.self.driver.find_element_by_xpath("//input[@id='fsr_2']").click()
#         Webself.self.driverself.self.wait(self.self.driver, 5)
#         # until(lambda self: self.self.driver.find_element_by_xpath("//input[@id='id_first_name']").is_displayed())
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_first_name']").clear()
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_first_name']").send_keys(user1)
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_last_name']").clear()
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_last_name']").send_keys(user1)
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_phone']").clear()
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_phone']").send_keys(phone)
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_city_chzn']/a").click()
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_city_chzn']//ul/li[2]").click()
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_township_chzn']/a").click()
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_township_chzn']//ul/li[2]").click()
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_delivery_address_id_chzn']/a").click()
#         self.self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_delivery_address_id_chzn']//ul/li").click()
#         self.self.wait

#         self.self.driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
#         self.self.wait.until(lambda self: self.self.driver.find_element_by_xpath("//input[@id='pm_1']").is_displayed())
#         print 'fisrt step ok'

#     def checkout_post_payment(self):

#         #verify order details without bonuses
#         total_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_post)
#         total_order_sum = int(new_cost) + int(delivery_post)
#         print 'total_order_sum', total_order_sum
#         order_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

#         self.self.driver.find_element_by_xpath("//input[@id='pm_1']").click()
#         self.self.wait

#         #select bonuses
#         self.self.driver.find_element_by_xpath(u"//label[contains(text(),'Использовать бонусный счет')]").click()
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//input[@name='voucher_id']").click()
#         self.self.driver.find_element_by_xpath("//a[@id='use_bonus']").click()
#         self.self.wait.until(lambda self: self.self.driver.find_element_by_xpath("//div[contains(text(),'Бонус будет использован с текущим заказом')]").is_displayed())
#         self.self.driver.find_element_by_xpath(u"//a[contains(text(),'Окей')]").click()
#         Webself.self.driverself.self.wait(self.self.driver, 15)
#         bonus_cost = self.self.driver.find_element_by_xpath("//span[@class='negative_cost']").text
#         print 'bonus_cost', int(bonus_cost)
#         # global bonus_cost

#         #verify order details with bonuses
#         total_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_post)
#         total_order_sum = (int(new_cost) + int(delivery_post)) + int(bonus_cost)
#         print 'total_order_sum', total_order_sum
#         order_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

#         self.self.driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
#         self.self.wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
#         print 'second step ok'

#     def checkout_post_confirm(self):

#         #verify product details        
#         self.self.driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
#         self.self.driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
#         self.self.driver.find_element_by_xpath("//div[contains(text(),'%s')]" % name)
#         self.self.driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)
#         # self.bonus_cost = bonus_cost

#         #verify order details
#         bonus_cost = self.self.driver.find_element_by_xpath("//span[@class='negative_cost']").text
#         print 'bonus_cost', int(bonus_cost)

#         total_order_sum = int(new_cost) + int(delivery_post) + int(bonus_cost)
#         print 'total_order_sum', total_order_sum
#         self.self.driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
#         self.self.driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_post)
#         self.self.driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
#         self.self.driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
#         self.self.wait
#         # .until(lambda self: self.self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % total_order_sum).is_displayed())

#     def verify_order_details(self):
        
#         order = self.self.driver.find_element_by_xpath("//h2[@class='complete__order']/strong").text
#         print 'order', order

#         profile = self.self.driver.find_element_by_xpath("//a[@href='/me/']")
#         orders = self.self.driver.find_element_by_xpath("//div[@class='user_menu profile_menu']/div/ul/li[1]/a")
#         self.action.move_to_element(profile)
#         self.self.wait
#         self.action.click(orders)
#         self.self.wait
#         self.action.perform()
#         self.self.wait

#         #verify order
#         print 'self.campaign', self.campaign.encode('utf-8')
#         self.self.driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div/a[contains(text(),'%s')]" % self.campaign)
#         self.self.driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a[contains(text(),'%s')]" % order).is_displayed()
#         self.self.driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_status']/a[contains(text(),'Заказ оформлен')]").is_displayed()
#         self.self.driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a").click()
#         self.self.wait

#         campaign_name = self.self.driver.find_element_by_xpath("//div[@class='order_details_block']/div[1]").text
#         print campaign_name.encode('utf-8')
#         assert (u'Акция: '+self.campaign) in campaign_name

#         order_number = self.self.driver.find_element_by_xpath("//div[@class='order_details_block']/div[3]").text
#         print 'order', order
#         assert (u'Номер заказа: '+order) in order_number

#         status = self.self.driver.find_element_by_xpath(u"//div[@class='order_details_block']/div[4]/span[@class='order_details_title__data']").text
#         print 'status', status.encode('utf-8')
#         assert u'Заказ оформлен' in status

# class PurchaseNonCashSelfDelivery:

#     def checkout_self_delivery(self):
#         self.self.driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
#         self.self.wait.until(lambda self: self.self.driver.find_element_by_xpath("//input[@id='fsr_3']").is_displayed())

#         #verify order details
#         total_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
#         order_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

#         self.self.driver.find_element_by_xpath("//input[@id='fsr_3']").click()
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
#         self.self.wait.until(lambda self: self.self.driver.find_element_by_xpath("//input[@id='pm_2']").is_displayed())
#         print 'fisrt step ok'

#     def checkout_card_payment(self):

#         self.self.driver.find_element_by_xpath("//input[@id='pm_2']").click()
#         self.self.wait

#         #verify order details
#         total_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)

#         delivery_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_self)
#         total_order_sum = int(new_cost) + int(delivery_self)
#         print 'total_order_sum', total_order_sum
#         order_sum = self.self.driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

#         self.self.driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
#         self.self.wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
#         print 'second step ok'

#     def checkout_self_confirm(self):

#         #verify product details        
#         self.self.driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
#         self.self.driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
#         self.self.driver.find_element_by_xpath("//div[contains(text(),'%s')]" % name)
#         self.self.driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)

#         #verify order details
#         total_order_sum = int(new_cost) + int(delivery_self)
#         print 'total_order_sum', total_order_sum
#         self.self.driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
#         self.self.driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_self)
#         self.self.driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
#         self.self.driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
#         self.self.wait.until(lambda self: self.self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % total_order_sum).is_displayed())

#     def fill_card_data(self):

#         self.self.driver.find_element_by_xpath("//input[@id='cardpay-cardnumber']").send_keys(card_number)
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//input[@id='cardpay-expmonth']").send_keys(card_month)
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//input[@id='cardpay-expyear']").send_keys(card_year)
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//input[@id='cardpay-cardholder']").send_keys(card_name)
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//input[@id='cardpay-cardsecure']").send_keys(card_cvv2)
#         self.self.wait
#         self.self.driver.find_element_by_xpath("//button[@id='cardpay-submit']").click()
#         self.self.wait.until(lambda self: self.self.driver.find_element_by_xpath("//h2[@class='complete__order']/strong").is_displayed())
        # print 'third step ok'