# !/usr/bin/env python 
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import mail_elements as me
from base_methods.config import *

class Mail:
    """verify emails elements"""
    
    def check_ragistration_email(self):

        self.open_url("http://yopmail.com", me.EMAIL_INPUT)       
    

    def verify_registration_email(self):
        self.driver.get(EMAIL)
        self.wait
        type_new_email = self.driver.find_element_by_xpath("//input[@id='inboxfield']").send_keys(RAND_NAME)
        enter_email = self.driver.find_element_by_xpath("//btn[@class='btn btn-success']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//h2[@id='InboxNameCtrl']").is_displayed())

        try:
            verify_register_email = self.driver.find_element_by_xpath(u"//div[contains(@class,'subject ng-binding') and normalize-space(text())='Подтвердите регистрацию на modnaKasta.ua']")
            verify_register_email.click()
            self.wait.until(lambda self: self.find_element_by_xpath("//iframe[@name='rendermail']").is_displayed())
            print 'click on mail'
        except:
            self.driver.refresh()
            verify_register_email
            print 'verify email is displayed'

        mail_iframe = self.driver.find_element_by_xpath("//iframe[@name='rendermail']")
        self.driver.switch_to.frame(mail_iframe)

        click_confirm_link = self.driver.find_element_by_xpath("//a[contains(@href,'https://modnakasta.ua/user/confirm/')]").click()

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        
        self.wait.until(lambda self: self.find_element_by_xpath("//input[@id='first_name']").is_displayed())

    def verify_registration_bot(self, BOT_NAME):
        self.driver.get(EMAIL)
        self.wait

        type_new_email = self.driver.find_element_by_xpath("//input[@id='inboxfield']").send_keys(BOT_NAME)
        enter_email = self.driver.find_element_by_xpath("//btn[@class='btn btn-success']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//h2[@id='InboxNameCtrl']").is_displayed()) 
        try:
            while self.driver.find_element_by_xpath(u"//div[contains(@class,'subject ng-binding') and normalize-space(text())='Ваша регистрация в клубе modnaKasta завершена!']"):
                change_email = self.driver.get(EMAIL)
                self.wait
                type_new_email = self.driver.find_element_by_xpath("//input[@id='inboxfield']").send_keys(NEW_BOT_NAME)
                enter_email = self.driver.find_element_by_xpath("//btn[@class='btn btn-success']").click()
                self.wait.until(lambda self: self.find_element_by_xpath("//h2[@id='InboxNameCtrl']").is_displayed())
                NEW_BOT_NAME = BOT_COUNT
                continue
        except:
            verify_register_email = self.driver.find_element_by_xpath(u"//div[contains(@class,'subject ng-binding') and normalize-space(text())='Подтвердите регистрацию на modnaKasta.ua']")
            verify_register_email.click()
            self.wait.until(lambda self: self.find_element_by_xpath("//iframe[@name='rendermail']").is_displayed())

            mail_iframe = self.driver.find_element_by_xpath("//iframe[@name='rendermail']")
            self.driver.switch_to.frame(mail_iframe)

            click_confirm_link = self.driver.find_element_by_xpath("//a[contains(@href,'https://modnakasta.ua/user/confirm/')]").click()

            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            
            self.wait.until(lambda self: self.find_element_by_xpath("//input[@id='first_name']").is_displayed())

    def verify_recovery_email(self):
        self.driver.get(EMAIL)
        self.wait
        type_new_email = self.driver.find_element_by_xpath("//input[@id='inboxfield']").send_keys(USER)
        enter_email = self.driver.find_element_by_xpath("//btn[@class='btn btn-success']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//h2[@id='InboxNameCtrl']").is_displayed())

        try:
            verify_recovery_email = self.driver.find_element_by_xpath(u"//div[contains(@class,'subject ng-binding') and normalize-space(text())='Восстановление вашего пароля на modnaKasta']")
            verify_recovery_email.click()
            self.wait.until(lambda self: self.find_element_by_xpath("//iframe[@name='rendermail']").is_displayed())
            print 'click on mail'
            
        except:
            self.driver.refresh()
            verify_recovery_email = self.driver.find_element_by_xpath(u"//div[contains(@class,'subject ng-binding') and normalize-space(text())='Восстановление вашего пароля на modnaKasta']")
            print 'verify email is displayed'

        mail_iframe = self.driver.find_element_by_xpath("//iframe[@name='rendermail']")
        self.driver.switch_to.frame(mail_iframe)

        click_confirm_link = self.driver.find_element_by_xpath("//a[contains(@href,'https://modnakasta.ua/user/password/reset/confirm/')]").click()
        
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

        self.wait.until(lambda self: self.find_element_by_xpath(u"//input[@placeholder='Новый пароль']").is_displayed())

    def verify_ordered_order_email(self):
        pass


# class RecoveryMail:
    
    # driver.get(email)
    # wait
    # driver.find_element_by_xpath("//input[@id='inboxfield']").send_keys(user1)
    # wait
    # driver.find_element_by_xpath("//btn[@class='btn btn-success']").click()
    # wait
    # driver.find_element_by_xpath(u"//ul[@id='mailcontainer']/li/a/div[normalize-space(text())='Восстановление вашего пароля на modnaKasta']").click()
    # wait.until(lambda self: driver.find_element_by_xpath("//iframe[@name='rendermail']").is_displayed())

    # iframe = driver.find_element_by_xpath("//iframe[@name='rendermail']")
    # driver.switch_to.frame(iframe)

    # driver.find_element_by_xpath("//a[contains(.,'https://modnakasta.ua/user/password/reset')]").click()

    # handles = driver.window_handles
    # driver.switch_to.window(handles[-1])








# class Authorization:

#     def auth(self):
#         self.driver.get(base_url)
#         self.wait
#         self.driver.find_element_by_xpath("//a[@href='#auth_popup']").click()
#         self.wait
#         self.driver.find_element_by_xpath("//div[@id='login_form']//input[@id='username']").send_keys(user1)
#         self.driver.find_element_by_xpath("//div[@id='login_form']//input[@name='password']").send_keys(password)
#         self.driver.find_element_by_xpath("//input[@id='login_submit']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//a[@href='/f/outlet/']").is_displayed())

    #'''def logout(self):'''
#         

# class PurchaseCashCourier():

#     def select_campaign(self):
#         outlet_button = self.driver.find_element_by_xpath("//a[@href='/f/outlet/']").click()
#         self.wait
#         select_campaign = self.driver.find_element_by_xpath("//div[@class='column_item column_1']/a").click()
#         self.wait
#         select_category = self.driver.find_element_by_xpath("//div[@class='row'][1]/div/a").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath(u"//a[@class='btn btn_padding shop_sold_hide']").is_displayed())
#         hide_sold = self.driver.find_element_by_xpath(u"//a[@class='btn btn_padding shop_sold_hide']").click()
#         self.wait

#         #verify if all products in category are sold
        
#         category = 1
#         try:
#             while self.driver.find_element_by_xpath("//div[@class='shop_items_list']/h1").is_displayed():
#                 self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[1]/a").click()
#                 self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[1]/div[@class='chzn-drop']//li[%s]" % category).click()
#                 self.wait
#                 category += 1
#                 print category
#                 self.driver.find_element_by_xpath("//div[@class='row']/div[%s]/a" % category).click()
#                 self.wait
#             else:
#                 pass
#         except:
#             print 'continue'

#         self.campaign = self.driver.find_element_by_xpath(u"//h1").text
#         print self.campaign.encode('utf-8'), 'self.campaign'

#     def select_product(self):

#         s = 1
#         price = self.driver.find_element_by_xpath("//div[@class='row'][%s]//div[@class='shop_new_cost']/span" % s).text

#         # print str(product)
#         print  'price', int(price)

#         global brand
#         global name
#         global new_cost
#         global old_cost
#         global size

#         while True:
#             if int(price) < 99:
#                 print 'while'
#                 print price
#                 s += 1
#                 print 's', s
#                 price = self.driver.find_element_by_xpath("//div[@class='row'][%s]//div[@class='shop_new_cost']/span" % s).text
#                 print price
#                 continue
#             if int(price) >= 99:
#                     print 's', s
#                     self.wait.until(lambda self: self.driver.find_element_by_xpath("//div[@class='row'][%s]/div[@class='shop_item']/a" % s).is_displayed())
#                     self.driver.find_element_by_xpath("//div[@class='row'][%s]/div[@class='shop_item']/a" % s).click()
#                     self.wait
#                     print 'product >= 99'

#                     #IF PRODUCT SOLD - CHECK OTHER
#                     try:
#                         self.driver.find_element_by_xpath("//span[@class='btn btn_red btn_disabled product_basket_btn']").is_displayed()
#                         print 'sold_true'
#                         s += 1
#                         print 's', s
#                         self.driver.back()
#                         self.wait
#                         continue
#                     except:
#                         print 'next try'
#                     try:
#                         self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").is_displayed()
#                         print 'size is_present'
#                         self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div[contains(@class,'button_on')]").click()
#                         print 'click size btn'
#                         self.wait

#                         #store product data
#                         brand = self.driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
#                         name = self.driver.find_element_by_xpath(u"//div[@class='product_name']").text
#                         new_cost = self.driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
#                         old_cost = self.driver.find_element_by_xpath("//div[@class='product_old_cost']").text
#                         size = self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").text

#                         self.driver.find_element_by_xpath(u"//a[contains(.,'В корзину')]").click()
#                         print 'click basket btn'
#                         self.wait
#                         print 'added to basket'
#                         break
#                     except:
#                         print 'first exception'

#                     #ONE SIZE
#                     try:
#                         self.driver.find_element_by_xpath("//div[@class='inner_content product_card']/div[@class='product_sizes']/div[@class='product_sizes']/div[@class='product_size_item sizes__button_chosen sizes__button_on ']").is_displayed()
#                         print 'selected size is_displayed'

#                         #store product data
#                         brand = self.driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
#                         name = self.driver.find_element_by_xpath(u"//div[@class='product_name']").text
#                         new_cost = self.driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
#                         old_cost = self.driver.find_element_by_xpath("//div[@class='product_old_cost']").text
#                         size = self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").text

#                         self.driver.find_element_by_xpath("//a[@class='btn btn_red product_basket_btn  ']").click()
#                         Webself.driverself.wait(self.self.driver, 10)
#                         print 'added to basket'
#                         # break
#                     except:
#                         print 'second exception'

#                     #NO SIZE
#                     try:
#                         self.driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='clear']/following-sibling::div[@class='clear']").is_displayed()
#                         print 'no size is_displayed'

#                         #store product data
#                         brand = self.driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
#                         name = self.driver.find_element_by_xpath(u"//div[@class='product_name']").text
#                         new_cost = self.driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
#                         old_cost = self.driver.find_element_by_xpath("//div[@class='product_old_cost']").text

#                         self.driver.find_element_by_xpath("//a[@class='btn btn_red product_basket_btn  ']").click()
#                         self.wait
#                         print 'added to basket'
#                         break
#                     except:
#                         print 'third exception'
#                         print 'sold_product'
#                     self.driver.back()
#                     self.wait
#                     s += 1
#                     print 's', s
#                     continue
#             break
#             print 'added to basket'
#             self.wait

#         print 'brand', brand.encode('utf-8')
#         print 'name', name.encode('utf-8')
#         print 'new_cost', new_cost
#         print 'old_cost', old_cost
#         print 'size'

#         if len(name) >= 30:
#             name = name[:30]
#             print 'name', name.encode('utf-8')
#         else:
#             pass

#         self.wait.until(lambda self: self.driver.find_element_by_xpath(u"//h1[contains(text(),'Корзина')]").is_displayed())
#         self.driver.find_element_by_xpath(u"//div[@class='container inner_container container_basket']/h1[contains(text(),'Корзина')]")
#         self.driver.find_element_by_xpath("//div[@class='table_cell cart_photo']").is_displayed()
#         self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % brand)
#         self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % name)
#         self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % new_cost)

#         print 'basket ok'

#     def checkout_courier_delivery(self):

#         self.driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//input[@id='fsr_1']").is_displayed())

#         #verify order details
#         total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
#         order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

#         self.driver.find_element_by_xpath("//input[@id='fsr_1']").click()
#         self.wait
#         self.driver.find_element_by_xpath("//form[@id='address_form_choose']/div[last()]/input").click()
#         self.wait
#         self.driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//input[@id='pm_1']").is_displayed())
#         print 'fisrt step ok'

#     def checkout_courier_payment(self): 

#         self.driver.find_element_by_xpath("//input[@id='pm_1']").click()
#         self.wait

#         #verify order details
#         total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'%s')]" % delivery_courier)
#         total_order_sum = int(new_cost) + int(delivery_courier)
#         print total_order_sum
#         order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % total_order_sum)

#         self.driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
#         self.wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
#         print 'second step ok'

#     def checkout_courier_confirm(self):

#         #verify product details        
#         self.driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
#         self.driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
#         self.driver.find_element_by_xpath("//div[contains(@class,'pri_category') and text()='%s']" % name)
#         self.driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)

#         #verify order details
#         total_order_sum = int(new_cost) + int(delivery_courier)
#         print total_order_sum
#         self.driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
#         self.driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_courier)
#         self.driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
#         self.driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//h2[@class='complete__order']/strong").is_displayed())
#         print 'third step ok'

#     def verify_order_details(self):

#         order = self.driver.find_element_by_xpath("//h2[@class='complete__order']/strong").text
#         print 'order', order

#         profile = self.driver.find_element_by_xpath("//a[@href='/me/']")
#         orders = self.driver.find_element_by_xpath("//div[@class='user_menu profile_menu']/div/ul/li[1]/a")
#         self.action.move_to_element(profile)
#         self.wait
#         self.action.click(orders)
#         self.wait
#         self.action.perform()
#         self.wait

#         #verify order
#         print 'self.campaign', self.campaign.encode('utf-8')
#         self.driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div/a[contains(text(),'%s')]" % self.campaign)
#         self.driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a[contains(text(),'%s')]" % order).is_displayed()
#         self.driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_status']/a[contains(text(),'Заказ оформлен')]").is_displayed()
#         self.driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a").click()
#         self.wait

#         campaign_name = self.driver.find_element_by_xpath("//div[@class='order_details_block']/div[1]").text
#         print campaign_name.encode('utf-8')
#         assert (u'Акция: '+self.campaign) in campaign_name

#         order_number = self.driver.find_element_by_xpath("//div[@class='order_details_block']/div[3]").text
#         print 'order', order
#         assert (u'Номер заказа: '+order) in order_number

#         status = self.driver.find_element_by_xpath(u"//div[@class='order_details_block']/div[4]/span[@class='order_details_title__data']").text
#         print 'status', status.encode('utf-8')
#         assert u'Заказ оформлен' in status

#     # def verify product info

#     def cancel_order(self):
#         cancellation = self.driver.find_element_by_xpath(u"//a[contains(text(),'Отменить')]").click()
#         self.wait
#         self.driver.find_element_by_xpath(u"//a[contains(text(),'Да')]").click()
#         self.wait
#         self.driver.find_element_by_xpath(u"//p[contains(text(),'Ваш запрос на отмену принят.')]").is_displayed()
#         self.driver.find_element_by_xpath(u"//select[@id='id_reason']").click()
#         self.wait
#         self.driver.find_element_by_xpath("//select[@id='id_reason']/option[3]").click()
#         self.wait
#         self.driver.find_element_by_xpath(u"//a[contains(text(),'Вернуться к покупкам')]").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//div[@class='row']/div[@class='column_item column_1']/a").is_displayed())
#         print 'order is cancelled'

# class PurchaseCashPost:

#     def checkout_post_delivery(self):

#         self.driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//input[@id='fsr_3']").is_displayed())

#         #verify order details
#         total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
#         order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

#         self.driver.find_element_by_xpath("//input[@id='fsr_2']").click()
#         Webself.driverself.wait(self.driver, 5)
#         # until(lambda self: self.driver.find_element_by_xpath("//input[@id='id_first_name']").is_displayed())
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_first_name']").clear()
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_first_name']").send_keys(user1)
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_last_name']").clear()
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_last_name']").send_keys(user1)
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_phone']").clear()
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_phone']").send_keys(phone)
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_city_chzn']/a").click()
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_city_chzn']//ul/li[2]").click()
#         self.wait
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_township_chzn']/a").click()
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_township_chzn']//ul/li[2]").click()
#         self.wait
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_delivery_address_id_chzn']/a").click()
#         self.driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_delivery_address_id_chzn']//ul/li").click()
#         self.wait

#         self.driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//input[@id='pm_1']").is_displayed())
#         print 'fisrt step ok'

#     def checkout_post_payment(self):

#         #verify order details without bonuses
#         total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_post)
#         total_order_sum = int(new_cost) + int(delivery_post)
#         print 'total_order_sum', total_order_sum
#         order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

#         self.driver.find_element_by_xpath("//input[@id='pm_1']").click()
#         self.wait

#         #select bonuses
#         self.driver.find_element_by_xpath(u"//label[contains(text(),'Использовать бонусный счет')]").click()
#         self.wait
#         self.driver.find_element_by_xpath("//input[@name='voucher_id']").click()
#         self.driver.find_element_by_xpath("//a[@id='use_bonus']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//div[contains(text(),'Бонус будет использован с текущим заказом')]").is_displayed())
#         self.driver.find_element_by_xpath(u"//a[contains(text(),'Окей')]").click()
#         Webself.driverself.wait(self.driver, 15)
#         bonus_cost = self.driver.find_element_by_xpath("//span[@class='negative_cost']").text
#         print 'bonus_cost', int(bonus_cost)
#         # global bonus_cost

#         #verify order details with bonuses
#         total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_post)
#         total_order_sum = (int(new_cost) + int(delivery_post)) + int(bonus_cost)
#         print 'total_order_sum', total_order_sum
#         order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

#         self.driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
#         self.wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
#         print 'second step ok'

#     def checkout_post_confirm(self):

#         #verify product details        
#         self.driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
#         self.driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
#         self.driver.find_element_by_xpath("//div[contains(text(),'%s')]" % name)
#         self.driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)
#         # self.bonus_cost = bonus_cost

#         #verify order details
#         bonus_cost = self.driver.find_element_by_xpath("//span[@class='negative_cost']").text
#         print 'bonus_cost', int(bonus_cost)

#         total_order_sum = int(new_cost) + int(delivery_post) + int(bonus_cost)
#         print 'total_order_sum', total_order_sum
#         self.driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
#         self.driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_post)
#         self.driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
#         self.driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
#         self.wait
#         # .until(lambda self: self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % total_order_sum).is_displayed())

#     def verify_order_details(self):
        
#         order = self.driver.find_element_by_xpath("//h2[@class='complete__order']/strong").text
#         print 'order', order

#         profile = self.driver.find_element_by_xpath("//a[@href='/me/']")
#         orders = self.driver.find_element_by_xpath("//div[@class='user_menu profile_menu']/div/ul/li[1]/a")
#         self.action.move_to_element(profile)
#         self.wait
#         self.action.click(orders)
#         self.wait
#         self.action.perform()
#         self.wait

#         #verify order
#         print 'self.campaign', self.campaign.encode('utf-8')
#         self.driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div/a[contains(text(),'%s')]" % self.campaign)
#         self.driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a[contains(text(),'%s')]" % order).is_displayed()
#         self.driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_status']/a[contains(text(),'Заказ оформлен')]").is_displayed()
#         self.driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a").click()
#         self.wait

#         campaign_name = self.driver.find_element_by_xpath("//div[@class='order_details_block']/div[1]").text
#         print campaign_name.encode('utf-8')
#         assert (u'Акция: '+self.campaign) in campaign_name

#         order_number = self.driver.find_element_by_xpath("//div[@class='order_details_block']/div[3]").text
#         print 'order', order
#         assert (u'Номер заказа: '+order) in order_number

#         status = self.driver.find_element_by_xpath(u"//div[@class='order_details_block']/div[4]/span[@class='order_details_title__data']").text
#         print 'status', status.encode('utf-8')
#         assert u'Заказ оформлен' in status

# class PurchaseNonCashSelfDelivery:

#     def checkout_self_delivery(self):
#         self.driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//input[@id='fsr_3']").is_displayed())

#         #verify order details
#         total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
#         delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
#         order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

#         self.driver.find_element_by_xpath("//input[@id='fsr_3']").click()
#         self.wait
#         self.driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//input[@id='pm_2']").is_displayed())
#         print 'fisrt step ok'

#     def checkout_card_payment(self):

#         self.driver.find_element_by_xpath("//input[@id='pm_2']").click()
#         self.wait

#         #verify order details
#         total_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)

#         delivery_sum = self.driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_self)
#         total_order_sum = int(new_cost) + int(delivery_self)
#         print 'total_order_sum', total_order_sum
#         order_sum = self.driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

#         self.driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
#         self.wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
#         print 'second step ok'

#     def checkout_self_confirm(self):

#         #verify product details        
#         self.driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
#         self.driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
#         self.driver.find_element_by_xpath("//div[contains(text(),'%s')]" % name)
#         self.driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)

#         #verify order details
#         total_order_sum = int(new_cost) + int(delivery_self)
#         print 'total_order_sum', total_order_sum
#         self.driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
#         self.driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_self)
#         self.driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
#         self.driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % total_order_sum).is_displayed())

#     def fill_card_data(self):

#         self.driver.find_element_by_xpath("//input[@id='cardpay-cardnumber']").send_keys(card_number)
#         self.wait
#         self.driver.find_element_by_xpath("//input[@id='cardpay-expmonth']").send_keys(card_month)
#         self.wait
#         self.driver.find_element_by_xpath("//input[@id='cardpay-expyear']").send_keys(card_year)
#         self.wait
#         self.driver.find_element_by_xpath("//input[@id='cardpay-cardholder']").send_keys(card_name)
#         self.wait
#         self.driver.find_element_by_xpath("//input[@id='cardpay-cardsecure']").send_keys(card_cvv2)
#         self.wait
#         self.driver.find_element_by_xpath("//button[@id='cardpay-submit']").click()
#         self.wait.until(lambda self: self.driver.find_element_by_xpath("//h2[@class='complete__order']/strong").is_displayed())
        # print 'third step ok'