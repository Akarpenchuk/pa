# !/usr/bin/env python 
# -*- coding: utf-8 -*-

"This module is describe certain locators and interaction between them"

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string
import unittest
import httplib

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

# TODO: make a dict 'user_data'
base_url = "https://modnakasta.ua"
email = "mailinator.com"
email_address = '@mailinator.com'
user1 = "user1@mailinator.com"
password = "qwe123"
phone = 380639728933

# TODO: make a dict for 'card data'
card_number = '5299190000150191'
card_month = '01'
card_year = '16'
card_name = 'test test'
card_cvv2 = '924'

#TODO: make a dict 'delivery_data'
user_range = 8
actions = ActionChains(driver)
delivery_courier = 35
delivery_post = 25
delivery_self = 0

class NonAuthUser:

    def main_page(self):
        driver.get(base_url)
        wait

        #check auth/register/recovery popup
        driver.find_element_by_xpath("//a[@href='#auth_popup']").click()
        wait
        driver.find_element_by_xpath("//div[@class='popup_container']//form[@id='login_form_validate']").is_displayed()
        driver.find_element_by_xpath("//div[@class='popup_container']//form[@id='register_form_validate']").is_displayed()
        driver.find_element_by_xpath("//div[@class='popup_container']/div[@class='auth_social']").is_displayed()
        driver.find_element_by_xpath("//a[@id='forgot_password']").click()
        wait
        #check availability of publick agreement
        driver.find_element_by_xpath("//div[@id='recovery_form']/div[contains(text(),'Восстановление пароля')]/following-sibling::form[@id='recovery_input_form']").is_displayed()
        driver.find_element_by_xpath("//div[@id='auth_popup']//a[@class='popup_close']").click()

        #coming soon
        driver.find_element_by_xpath("//div[@id='coming_soon']//div[contains(text(),'Скоро в продаже')]").is_displayed()
        driver.find_element_by_xpath("//div[@class='coming_list']//div[@class='coming_item']/span[@class='coming_collection']").is_displayed()

        #check help menu
        driver.refresh()
        help = driver.find_element_by_xpath("//a[@href='/support/payments/']")
        actions.move_to_element(help)
        actions.perform()
        help_menu = driver.find_element_by_xpath("//div[@class='user_menu support_menu']/div/ul/li").is_displayed()

        #check main menu (make verify through the list)
        female = driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/female/']")
        female_banner = driver.find_element_by_xpath("//div[@class='dropdown dropdown_cols_3 ']/div//img[contains(@src,'https://media.modnakasta.ua/')]")
        male = driver.find_element_by_xpath(u"//a[@href='/f/male/']")
        male_banner = driver.find_element_by_xpath("//div[@class='dropdown dropdown_cols_2 items2']/div//img[contains(@src,'https://media.modnakasta.ua/')]")
        child = driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/child/']")
        child_banner = driver.find_element_by_xpath("//div[@class='dropdown dropdown_cols_2 items2']/div//img[contains(@src,'https://media.modnakasta.ua/')]")
        home = driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/home/']")
        home_banner = driver.find_element_by_xpath("//div[@class='dropdown dropdown_cols_1 ']/div//img[contains(@src,'https://media.modnakasta.ua/')]")
        outlet = driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/outlet/']")
        outlet_banner = driver.find_element_by_xpath("//div[@class='dropdown_banner placeholder']//img[contains(@src,'https://media.modnakasta.ua/')]")

        actions.move_to_element(male)
        actions.move_to_element(male_banner)
        actions.move_to_element(female)
        actions.move_to_element(female_banner)
        actions.move_to_element(child)
        actions.move_to_element(child_banner)
        actions.move_to_element(home)
        actions.move_to_element(home_banner)
        actions.move_to_element(outlet)
        actions.move_to_element(outlet_banner)
        actions.perform()
        
        female = driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/female/']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        first_campaign = driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        actions.move_to_element(first_campaign)
        actions.perform
        driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()
        driver.switch_to_default_content()
        #first campaign
        driver.find_element_by_xpath("//div[@id='current']/div[@class='row']/div/a").is_displayed()
        #soon end
        driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !
        
        male = driver.find_element_by_xpath(u"//a[@href='/f/male/']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        first_campaign = driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        actions.move_to_element(first_campaign)
        actions.perform
        driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()
        driver.switch_to_default_content()
        #first campaign
        driver.find_element_by_xpath("//div[@id='current']/div[@class='row']/div/a").is_displayed()
        #soon end
        driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !
        
        child = driver.find_element_by_xpath(u"//a[@href='/f/child/']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        first_campaign = driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        actions.move_to_element(first_campaign)
        actions.perform
        driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()
        driver.switch_to_default_content()
        #first campaign
        driver.find_element_by_xpath("//div[@id='current']/div[@class='row']/div/a").is_displayed()
        #soon end
        driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !
       
        home = driver.find_element_by_xpath(u"//a[@href='/f/home/']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        first_campaign = driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        actions.move_to_element(first_campaign)
        actions.perform
        driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()
        driver.switch_to_default_content()
        #first campaign
        driver.find_element_by_xpath("//div[@id='current']/div[@class='row']/div/a").is_displayed()
        #soon end
        driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !
        
        outlet = driver.find_element_by_xpath(u"//a[@href='/f/outlet/']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        first_campaign = driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        actions.move_to_element(first_campaign)
        actions.perform
        driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()
        driver.switch_to_default_content()
        #first campaign
        driver.find_element_by_xpath("//div[@id='current']/div[@class='row']/div/a").is_displayed()
        #soon end
        driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !
        
    def check_anonym_purchase_loyalty(self):
        driver.get(base_url)
        wait
        driver.find_element_by_xpath("//div[@class='container_full main_menu']/ul/li/p/a[@href='/modnakarta/']").click()
        wait
        driver.find_element_by_xpath("//nav[@class='menu']/div/a").is_displayed()
        driver.find_element_by_xpath("//a[@href='https://modnakasta.ua/f/female/']").is_displayed()
        driver.find_element_by_xpath("//a[@href='https://modnakasta.ua/f/male/']").is_displayed()
        driver.find_element_by_xpath("//a[@href='https://modnakasta.ua/f/child/']").is_displayed()
        driver.find_element_by_xpath("//a[@href='https://modnakasta.ua/f/home/']").is_displayed()
        driver.find_element_by_xpath("//a[@href='https://modnakasta.ua/f/foodwine/']").is_displayed()
        driver.find_element_by_xpath("//a[@href='https://modnakasta.ua/f/outlet/']").is_displayed()
        driver.find_element_by_xpath("//a[@href='https://modnakasta.ua/modnakarta/']").is_displayed()
        driver.find_element_by_xpath("//form[contains(@action,'/basket/add/')]/input[@type='submit']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//form[@id='login_form_validate']").is_displayed())
        driver.find_element_by_xpath("//a[@class='popup_close']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())

    def check_campaign_filters(self):
        #check category filter
        select_campaign = driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").click()
        wait
        try:
            if driver.find_element_by_xpath("//div[@class='column_item column_2 column_outlet']").is_displayed():
                print 'outlet'
                select_category = driver.find_element_by_xpath("//div[@class='column_item column_2 column_outlet']/a[contains(@href,'/campaign/')]").click()
                wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row']/div[@class='shop_item']").is_displayed())
            else:
                print 'not outlet'
        except:
            pass
        
        common_product_count = driver.find_elements_by_xpath("//div[@class='row']/div[@class='shop_item']")
        print 'common_product_count', len(common_product_count)
        select_category_list = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div/a").click()
        wait
        select_category = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[1]//ul//li[3]").click()
        wait
        category_product_count = driver.find_elements_by_xpath("//div[@class='row']/div[@class='shop_item']")
        print 'category_product_count', len(category_product_count)
        
        current_url = driver.current_url
        print current_url
        
        assert '?category=' in current_url
        
        assert len(common_product_count) != len(category_product_count)
        print 'category is changing'

        #switch category back
        select_category_menu = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div/a").click()
        wait
        select_category = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[1]//ul//li[1]").click()
        wait
        common_product_count = driver.find_elements_by_xpath("//div[@class='row']/div[@class='shop_item']")

        assert len(common_product_count) != len(category_product_count)
        print 'category is switching back'

        #check brand filter
        try:
            driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]/a").click()
            wait
            print 'select simple category'
        except:
            driver.find_element_by_xpath("//div[@class='column_item column_2 column_outlet'][1]/a").click()
            wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row']/div[@class='shop_item']").is_displayed())
            print 'select outlet category'
        
        select_brand_menu = driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]/a").click()
        select_brand = driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]//ul//li[2]").click()

        brand_name = driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]/a/span").text
        print 'brand_name', brand_name.encode('utf-8')
        fst_product_brand = driver.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_name']/span[contains(text(),'%s')]" % brand_name)
        lst_product_brand = driver.find_element_by_xpath("//div[@class='row']/div[last()]//div[@class='shop_item_name']/span[contains(text(),'%s')]" % brand_name)
        #TODO: assert product_brand == any list item
        # products_brand_list = driver.find_elements_by_xpath("//div[@class='shop_item']//div[@class='shop_item_name']/span")

        #switch brand back
        select_brand_menu = driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]/a").click()
        wait
        select_brand = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[2]//ul//li[1]").click()
        wait

        #check size filter
        select_size_menu = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]/a").click()
        wait
        select_brand = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]//ul//li[2]").click()
        wait
        size_name = driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[3]/a/span").text
        print 'size_name', size_name.encode('utf-8')

        fst_product = driver.find_element_by_xpath("//div[@class='row'][1]/div[1]/a").click()
        fst_product_size = driver.find_element_by_xpath("//div[@class='product_sizes']/div[contains(text(),'%s')]" % size_name)
        driver.back()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]/a").is_displayed())

        # lst_product = driver.find_element_by_xpath("//div[@class='row']/div[last()]/a").click()
        # lst_product_size = driver.find_element_by_xpath("//div[@class='product_sizes']/div[contains(text(),'%s')]" % size_name)
        # driver.back()
        # wait
        
        #switch brand back
        select_size_menu = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]/a").click()
        wait
        select_brand = driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]//ul//li[1]").click()
        wait

        #check price sort by asc
        select_sortUp = driver.find_element_by_xpath("//div[@class='shop_sort']/a").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").is_displayed())
        fst_product_price = driver.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").text
        print 'fst_product_price', fst_product_price
        lst_product_price = driver.find_element_by_xpath("//div[@class='row'][last()]/div[last()]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").text
        print 'lst_product_price', lst_product_price
        assert int(fst_product_price) < int(lst_product_price)

        #check price sort by desc
        select_sortDown = driver.find_element_by_xpath("//div[@class='shop_sort']/a[2]").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").is_displayed())
        fst_product_price = driver.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").text
        print 'fst_product_price', fst_product_price
        lst_product_price = driver.find_element_by_xpath("//div[@class='row'][last()]/div[last()]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").text
        print 'lst_product_price', lst_product_price
        assert int(fst_product_price) > int(lst_product_price)

        #check hide sold filter
        select_hide_sold = driver.find_element_by_xpath(u"//a[contains(text(),'Скрыть проданные')]").click()
        wait
        try:
            sold_is_present = driver.find_element_by_xpath("//div[@class='shop_sold']").is_displayed()
            assert sold_is_present == True
        except:
            print 'sold is not present'

        #check auth popup while adding product
        s = 1
        while s != 1000:
            try:
                select_product = driver.find_element_by_xpath("//div[@class='row'][%s]/div[@class='shop_item']/a" % s).click()
                wait
                add_product = driver.find_element_by_xpath(u"//a[contains(text(),'В корзину')]").click()
                wait
                if driver.find_element_by_xpath(u"//div[contains(text(),'Выберите сначала размер')]").is_displayed():
                    driver.find_element_by_xpath(u"//a[contains(text(),'Окей')]").click()
                    wait
                    select_size = driver.find_element_by_xpath("//div[@class='product_sizes']/div[contains(@class,'product_size_item')]").click()
                    wait
                    add_product = driver.find_element_by_xpath(u"//a[contains(text(),'В корзину')]").click()
                    wait
                    # .until(lambda self: 
                    driver.find_element_by_xpath("//form[@id='login_form_validate']").is_displayed()
                    s = 1000
                    print 'popoup is is displayed'
                else:
                    wait.until(lambda self: driver.find_element_by_xpath("//form[@id='login_form_validate']").is_displayed())
                    s = 1000
                    print 'popoup is is displayed'
            except Exception, e:
                    print 'product is sold'
                    driver.back()
                    s += 1
                    wait

class RecoveryEmail:

    def send_recovery_email(self):
        driver.get(base_url)
        wait
        driver.find_element_by_xpath(u"//a[@href='#auth_popup']/span[contains(text,'Регистрация')]").click()
        wait
        switch_to_recovery_form = driver.find_element_by_xpath(u"//a[contains(@href,'forgot_password') and (text='Забыли пароль?')]").click()
        wait.until(lambda self: driver.find_element_by_xpath("//form[@id='recovery_input_form']").is_displayed())
        email_intput = driver.find_element_by_xpath("//form[@id='recovery_input_form']/div/input[@type='text']").send_keys(""+user1)
        wait
        driver.find_element_by_xpath("//input[@id='recovery_submit']").click()
        wait
        driver.find_element_by_xpath("//div[@class='recovery_email_text']").is_displayed()
        driver.find_element_by_xpath("//div[@class='recovery_email_text']").click()

    def approve_recovery_email(self):
        driver.get(email)
        wait
        driver.find_element_by_xpath("//input[@id='inboxfield']").send_keys(user1)
        wait
        driver.find_element_by_xpath("//btn[@class='btn btn-success']").click()
        wait

        driver.find_element_by_xpath(u"//ul[@id='mailcontainer']/li/a/div[normalize-space(text())='Восстановление вашего пароля на modnaKasta']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//iframe[@name='rendermail']").is_displayed())

        iframe = driver.find_element_by_xpath("//iframe[@name='rendermail']")
        driver.switch_to.frame(iframe)

        driver.find_element_by_xpath("//a[contains(.,'https://modnakasta.ua/user/password/reset')]").click()

        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        
        wait.until(lambda self: driver.find_element_by_id('id_new_password1')).is_displayed()

    def set_new_password(self):
        driver.find_element_by_id('id_new_password1').send_keys(password)
        driver.find_element_by_id('id_new_password2').send_keys(password)
        driver.find_element_by_id('submit_password').click()

    def auth_in_recovery_form(self):
        driver.find_element_by_id('login__email').clear()
        driver.find_element_by_id('login__email').send_keys(user1)
        driver.find_element_by_id('login__pass').clear()
        driver.find_element_by_id('login__pass').send_keys(password)
        driver.find_element_by_id('submit_password').click()
        wait

class Registration:
        
    def make_random_name(self):
        self.rand_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
        print 'self.rand_name', self.rand_name
        self.user_email = self.rand_name+email_address
        print 'self.user_email', self.user_email

    def send_register_link(self):
        driver.get(base_url)
        wait.until(lambda self: driver.find_element_by_xpath(u"//a[@href='#auth_popup']/span[contains(text,'Регистрация')]").is_displayed())
        open_register_popup = driver.find_element_by_xpath(u"//a[@href='#auth_popup']/span[contains(text,'Регистрация')]").click()
        wait
        driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='email']").send_keys(self.user_email)
        driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='password']").send_keys(""+password)
        wait
        driver.find_element_by_xpath("//input[@id='register_submit']").click()
        wait.until(lambda self: u"Сообщение со ссылкой для" in driver.page_source)

    def approve_registration_email(self):
        driver.get(email)
        wait
        driver.find_element_by_xpath("//input[@id='inboxfield']").send_keys(self.rand_name)
        driver.find_element_by_xpath("//btn[@class='btn btn-success']").click()
        wait
        driver.find_element_by_xpath(u"//ul[@id='mailcontainer']//div[contains(@class,'subject ng-binding') and normalize-space(text())='Подтвердите регистрацию на modnaKasta.ua']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//iframe[@name='rendermail']").is_displayed())

        iframe = driver.find_element_by_xpath("//iframe[@name='rendermail']")
        driver.switch_to.frame(iframe)

        driver.find_element_by_xpath("//a[contains(@href,'https://modnakasta.ua/user/confirm/')]").click()
        wait

        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        wait.until(lambda self: driver.find_element_by_xpath("//input[@id='first_name']").is_displayed())
        
    def fill_personal_info_popup(self):
        driver.find_element_by_xpath("//input[@id='first_name']").send_keys(self.user_email)
        driver.find_element_by_xpath("//input[@id='last_name']").send_keys(self.user_email)
        driver.find_element_by_xpath("//input[@id='personal_info_submit']").click()
        wait
        driver.find_element_by_xpath("//span[@id='user_name']")

    def check_personal_email(self):
        driver.find_element_by_xpath("//a[@href='/me/']").click()
        wait
        driver.find_element_by_xpath("//div[@class='personal_info_left']/div[1]/input[@value='%s']" % self.user_email)
        driver.find_element_by_xpath("//div[@class='personal_info_left']/div[2]/input[@value='%s']" % self.user_email)
        driver.find_element_by_xpath("//div[@class='personal_info_right']/div[1]/input[@value='%s']" % self.user_email)
        print 'user has been registered'


class Authorization:

    def auth(self):
        driver.get(base_url)
        wait
        driver.find_element_by_xpath("//a[@href='#auth_popup']").click()
        wait
        driver.find_element_by_xpath("//div[@id='login_form']//input[@id='username']").send_keys(user1)
        driver.find_element_by_xpath("//div[@id='login_form']//input[@name='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@id='login_submit']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//a[@href='/f/outlet/']").is_displayed())

    def logout(self):
        menu_item = driver.find_element_by_xpath("//a[@href='/me/']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//a[@href='/user/registration/logout/']").is_displayed())
        driver.find_element_by_xpath("//a[@href='/user/registration/logout/']").click()
        wait.until(lambda self: driver.find_element_by_xpath(u"//a[@href='#auth_popup']/span[contains(text(),'Регистрация')]").is_displayed())

class PurchaseCashCourier():

    def select_campaign(self):
        outlet_button = driver.find_element_by_xpath("//a[@href='/f/outlet/']").click()
        wait
        select_campaign = driver.find_element_by_xpath("//div[@class='column_item column_1']/a").click()
        wait
        select_category = driver.find_element_by_xpath("//div[@class='row'][1]/div/a").click()
        wait.until(lambda self: driver.find_element_by_xpath(u"//a[@class='btn btn_padding shop_sold_hide']").is_displayed())
        hide_sold = driver.find_element_by_xpath(u"//a[@class='btn btn_padding shop_sold_hide']").click()
        wait

        #verify if all products in category are sold
        
        category = 1
        try:
            while driver.find_element_by_xpath("//div[@class='shop_items_list']/h1").is_displayed():
                driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[1]/a").click()
                driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[1]/div[@class='chzn-drop']//li[%s]" % category).click()
                wait
                category += 1
                print category
                driver.find_element_by_xpath("//div[@class='row']/div[%s]/a" % category).click()
                wait
            else:
                pass
        except:
            print 'continue'

        self.campaign = driver.find_element_by_xpath(u"//h1").text
        print self.campaign.encode('utf-8'), 'self.campaign'

    def select_product(self):

        s = 1
        price = driver.find_element_by_xpath("//div[@class='row'][%s]//div[@class='shop_new_cost']/span" % s).text

        # print str(product)
        print  'price', int(price)

        global brand
        global name
        global new_cost
        global old_cost
        global size

        while True:
            if int(price) < 99:
                print 'while'
                print price
                s += 1
                print 's', s
                price = driver.find_element_by_xpath("//div[@class='row'][%s]//div[@class='shop_new_cost']/span" % s).text
                print price
                continue
            if int(price) >= 99:
                    print 's', s
                    wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row'][%s]/div[@class='shop_item']/a" % s).is_displayed())
                    driver.find_element_by_xpath("//div[@class='row'][%s]/div[@class='shop_item']/a" % s).click()
                    wait
                    print 'product >= 99'

                    #IF PRODUCT SOLD - CHECK OTHER
                    try:
                        driver.find_element_by_xpath("//span[@class='btn btn_red btn_disabled product_basket_btn']").is_displayed()
                        print 'sold_true'
                        s += 1
                        print 's', s
                        driver.back()
                        wait
                        continue
                    except:
                        print 'next try'
                    try:
                        driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").is_displayed()
                        print 'size is_present'
                        driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div[contains(@class,'button_on')]").click()
                        print 'click size btn'
                        wait

                        #store product data
                        brand = driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
                        name = driver.find_element_by_xpath(u"//div[@class='product_name']").text
                        new_cost = driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
                        old_cost = driver.find_element_by_xpath("//div[@class='product_old_cost']").text
                        size = driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").text

                        driver.find_element_by_xpath(u"//a[contains(.,'В корзину')]").click()
                        print 'click basket btn'
                        wait
                        print 'added to basket'
                        break
                    except:
                        print 'first exception'

                    #ONE SIZE
                    try:
                        driver.find_element_by_xpath("//div[@class='inner_content product_card']/div[@class='product_sizes']/div[@class='product_sizes']/div[@class='product_size_item sizes__button_chosen sizes__button_on ']").is_displayed()
                        print 'selected size is_displayed'

                        #store product data
                        brand = driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
                        name = driver.find_element_by_xpath(u"//div[@class='product_name']").text
                        new_cost = driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
                        old_cost = driver.find_element_by_xpath("//div[@class='product_old_cost']").text
                        size = driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='product_sizes']/div").text

                        driver.find_element_by_xpath("//a[@class='btn btn_red product_basket_btn  ']").click()
                        WebDriverWait(self.driver, 10)
                        print 'added to basket'
                        # break
                    except:
                        print 'second exception'

                    #NO SIZE
                    try:
                        driver.find_element_by_xpath("//div[@class='product_sizes']/div[@class='clear']/following-sibling::div[@class='clear']").is_displayed()
                        print 'no size is_displayed'

                        #store product data
                        brand = driver.find_element_by_xpath(u"//div[@class='product_author liked']").text
                        name = driver.find_element_by_xpath(u"//div[@class='product_name']").text
                        new_cost = driver.find_element_by_xpath("//div[@class='product_new_cost']/div").text
                        old_cost = driver.find_element_by_xpath("//div[@class='product_old_cost']").text

                        driver.find_element_by_xpath("//a[@class='btn btn_red product_basket_btn  ']").click()
                        wait
                        print 'added to basket'
                        break
                    except:
                        print 'third exception'
                        print 'sold_product'
                    driver.back()
                    wait
                    s += 1
                    print 's', s
                    continue
            break
            print 'added to basket'
            wait

        print 'brand', brand.encode('utf-8')
        print 'name', name.encode('utf-8')
        print 'new_cost', new_cost
        print 'old_cost', old_cost
        print 'size'

        if len(name) >= 30:
            name = name[:30]
            print 'name', name.encode('utf-8')
        else:
            pass

        wait.until(lambda self: driver.find_element_by_xpath(u"//h1[contains(text(),'Корзина')]").is_displayed())
        driver.find_element_by_xpath(u"//div[@class='container inner_container container_basket']/h1[contains(text(),'Корзина')]")
        driver.find_element_by_xpath("//div[@class='table_cell cart_photo']").is_displayed()
        driver.find_element_by_xpath("//a[contains(text(),'%s')]" % brand)
        driver.find_element_by_xpath("//a[contains(text(),'%s')]" % name)
        driver.find_element_by_xpath("//span[contains(text(),'%s')]" % new_cost)

        print 'basket ok'

    def checkout_courier_delivery(self):

        driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//input[@id='fsr_1']").is_displayed())

        #verify order details
        total_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
        delivery_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
        order_sum = driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

        driver.find_element_by_xpath("//input[@id='fsr_1']").click()
        wait
        driver.find_element_by_xpath("//form[@id='address_form_choose']/div[last()]/input").click()
        wait
        driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//input[@id='pm_1']").is_displayed())
        print 'fisrt step ok'

    def checkout_courier_payment(self): 

        driver.find_element_by_xpath("//input[@id='pm_1']").click()
        wait

        #verify order details
        total_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
        delivery_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'%s')]" % delivery_courier)
        total_order_sum = int(new_cost) + int(delivery_courier)
        print total_order_sum
        order_sum = driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % total_order_sum)

        driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
        wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
        print 'second step ok'

    def checkout_courier_confirm(self):

        #verify product details        
        driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
        driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
        driver.find_element_by_xpath("//div[contains(@class,'pri_category') and text()='%s']" % name)
        driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)

        #verify order details
        total_order_sum = int(new_cost) + int(delivery_courier)
        print total_order_sum
        driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
        driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_courier)
        driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
        driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//h2[@class='complete__order']/strong").is_displayed())
        print 'third step ok'

    def verify_order_details(self):

        order = driver.find_element_by_xpath("//h2[@class='complete__order']/strong").text
        print 'order', order

        profile = driver.find_element_by_xpath("//a[@href='/me/']")
        orders = driver.find_element_by_xpath("//div[@class='user_menu profile_menu']/div/ul/li[1]/a")
        actions.move_to_element(profile)
        wait
        actions.click(orders)
        wait
        actions.perform()
        wait

        #verify order
        print 'self.campaign', self.campaign.encode('utf-8')
        driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div/a[contains(text(),'%s')]" % self.campaign)
        driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a[contains(text(),'%s')]" % order).is_displayed()
        driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_status']/a[contains(text(),'Заказ оформлен')]").is_displayed()
        driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a").click()
        wait

        campaign_name = driver.find_element_by_xpath("//div[@class='order_details_block']/div[1]").text
        print campaign_name.encode('utf-8')
        assert (u'Акция: '+self.campaign) in campaign_name

        order_number = driver.find_element_by_xpath("//div[@class='order_details_block']/div[3]").text
        print 'order', order
        assert (u'Номер заказа: '+order) in order_number

        status = driver.find_element_by_xpath(u"//div[@class='order_details_block']/div[4]/span[@class='order_details_title__data']").text
        print 'status', status.encode('utf-8')
        assert u'Заказ оформлен' in status

    # def verify product info

    def cancel_order(self):
        cancellation = driver.find_element_by_xpath(u"//a[contains(text(),'Отменить')]").click()
        wait
        driver.find_element_by_xpath(u"//a[contains(text(),'Да')]").click()
        wait
        driver.find_element_by_xpath(u"//p[contains(text(),'Ваш запрос на отмену принят.')]").is_displayed()
        driver.find_element_by_xpath(u"//select[@id='id_reason']").click()
        wait
        driver.find_element_by_xpath("//select[@id='id_reason']/option[3]").click()
        wait
        driver.find_element_by_xpath(u"//a[contains(text(),'Вернуться к покупкам')]").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[@class='row']/div[@class='column_item column_1']/a").is_displayed())
        print 'order is cancelled'

class PurchaseCashPost:

    def checkout_post_delivery(self):

        driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//input[@id='fsr_3']").is_displayed())

        #verify order details
        total_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
        delivery_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
        order_sum = driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

        driver.find_element_by_xpath("//input[@id='fsr_2']").click()
        WebDriverWait(driver, 5)
        # until(lambda self: driver.find_element_by_xpath("//input[@id='id_first_name']").is_displayed())
        driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_first_name']").clear()
        driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_first_name']").send_keys(user1)
        driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_last_name']").clear()
        driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_last_name']").send_keys(user1)
        driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_phone']").clear()
        driver.find_element_by_xpath("//form[@id='address_form_departments']//input[@id='id_phone']").send_keys(phone)
        driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_city_chzn']/a").click()
        driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_city_chzn']//ul/li[2]").click()
        wait
        driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_township_chzn']/a").click()
        driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_township_chzn']//ul/li[2]").click()
        wait
        driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_delivery_address_id_chzn']/a").click()
        driver.find_element_by_xpath("//form[@id='address_form_departments']//div[@id='id_delivery_address_id_chzn']//ul/li").click()
        wait

        driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//input[@id='pm_1']").is_displayed())
        print 'fisrt step ok'

    def checkout_post_payment(self):

        #verify order details without bonuses
        total_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)
        delivery_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_post)
        total_order_sum = int(new_cost) + int(delivery_post)
        print 'total_order_sum', total_order_sum
        order_sum = driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

        driver.find_element_by_xpath("//input[@id='pm_1']").click()
        wait

        #select bonuses
        driver.find_element_by_xpath(u"//label[contains(text(),'Использовать бонусный счет')]").click()
        wait
        driver.find_element_by_xpath("//input[@name='voucher_id']").click()
        driver.find_element_by_xpath("//a[@id='use_bonus']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//div[contains(text(),'Бонус будет использован с текущим заказом')]").is_displayed())
        driver.find_element_by_xpath(u"//a[contains(text(),'Окей')]").click()
        WebDriverWait(driver, 15)
        bonus_cost = driver.find_element_by_xpath("//span[@class='negative_cost']").text
        print 'bonus_cost', int(bonus_cost)
        # global bonus_cost

        #verify order details with bonuses
        total_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)
        delivery_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_post)
        total_order_sum = (int(new_cost) + int(delivery_post)) + int(bonus_cost)
        print 'total_order_sum', total_order_sum
        order_sum = driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

        driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
        wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
        print 'second step ok'

    def checkout_post_confirm(self):

        #verify product details        
        driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
        driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
        driver.find_element_by_xpath("//div[contains(text(),'%s')]" % name)
        driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)
        # self.bonus_cost = bonus_cost

        #verify order details
        bonus_cost = driver.find_element_by_xpath("//span[@class='negative_cost']").text
        print 'bonus_cost', int(bonus_cost)

        total_order_sum = int(new_cost) + int(delivery_post) + int(bonus_cost)
        print 'total_order_sum', total_order_sum
        driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
        driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_post)
        driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
        driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
        wait
        # .until(lambda self: driver.find_element_by_xpath("//span[contains(text(),'%s')]" % total_order_sum).is_displayed())

    def verify_order_details(self):
        
        order = driver.find_element_by_xpath("//h2[@class='complete__order']/strong").text
        print 'order', order

        profile = driver.find_element_by_xpath("//a[@href='/me/']")
        orders = driver.find_element_by_xpath("//div[@class='user_menu profile_menu']/div/ul/li[1]/a")
        actions.move_to_element(profile)
        wait
        actions.click(orders)
        wait
        actions.perform()
        wait

        #verify order
        print 'self.campaign', self.campaign.encode('utf-8')
        driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div/a[contains(text(),'%s')]" % self.campaign)
        driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a[contains(text(),'%s')]" % order).is_displayed()
        driver.find_element_by_xpath(u"//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_status']/a[contains(text(),'Заказ оформлен')]").is_displayed()
        driver.find_element_by_xpath("//div[@class='cabinet_cells cabinet_orders_cells']/div[@class='table_cell order_number']/a").click()
        wait

        campaign_name = driver.find_element_by_xpath("//div[@class='order_details_block']/div[1]").text
        print campaign_name.encode('utf-8')
        assert (u'Акция: '+self.campaign) in campaign_name

        order_number = driver.find_element_by_xpath("//div[@class='order_details_block']/div[3]").text
        print 'order', order
        assert (u'Номер заказа: '+order) in order_number

        status = driver.find_element_by_xpath(u"//div[@class='order_details_block']/div[4]/span[@class='order_details_title__data']").text
        print 'status', status.encode('utf-8')
        assert u'Заказ оформлен' in status

class PurchaseNonCashSelfDelivery:

    def checkout_self_delivery(self):
        driver.find_element_by_xpath("//a[@id='btn_checkout']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//input[@id='fsr_3']").is_displayed())

        #verify order details
        total_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]/div/span[contains(text(),'%s')]" % new_cost)
        delivery_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]/div/span[contains(text(),'0')]")
        order_sum = driver.find_element_by_xpath("//div[@class='make_order_total']/div/span[contains(text(),'%s')]" % new_cost)

        driver.find_element_by_xpath("//input[@id='fsr_3']").click()
        wait
        driver.find_element_by_xpath("//a[@id='first_step_submit']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//input[@id='pm_2']").is_displayed())
        print 'fisrt step ok'

    def checkout_card_payment(self):

        driver.find_element_by_xpath("//input[@id='pm_2']").click()
        wait

        #verify order details
        total_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[1]//span[contains(text(),'%s')]" % new_cost)

        delivery_sum = driver.find_element_by_xpath("//div[@class='make_order_list']/div[2]//span[contains(text(),'%s')]" % delivery_self)
        total_order_sum = int(new_cost) + int(delivery_self)
        print 'total_order_sum', total_order_sum
        order_sum = driver.find_element_by_xpath("//div[@class='make_order_total']//span[contains(text(),'%s')]" % total_order_sum)

        driver.find_element_by_xpath("//a[@id='second_step_submit']").click()
        wait.until(lambda self: self.find_element_by_xpath("//a[@class='pri_image']/img").is_displayed())
        print 'second step ok'

    def checkout_self_confirm(self):

        #verify product details        
        driver.find_element_by_xpath("//a[@class='pri_image']/img[contains(@src,'https://media.modnakasta.ua/')]")
        driver.find_element_by_xpath("//div[contains(@class,'pri_name') and text()='%s']" % brand)
        driver.find_element_by_xpath("//div[contains(text(),'%s')]" % name)
        driver.find_element_by_xpath("//div[@class='pri_new_cost']/span[contains(text(),'%s.00')]" % new_cost)

        #verify order details
        total_order_sum = int(new_cost) + int(delivery_self)
        print 'total_order_sum', total_order_sum
        driver.find_element_by_xpath("//div[@class='mol_cost total_sum']/span[contains(text(),'%s')]" % new_cost)
        driver.find_element_by_xpath("//div[@class='mol_cost delivery']/span[contains(text(),'%s')]" % delivery_self)
        driver.find_element_by_xpath("//div[@class='make_order_total_cost']/span[contains(text(),'%s')]" % total_order_sum)
        driver.find_element_by_xpath("//a[@id='make_order_submit']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//span[contains(text(),'%s')]" % total_order_sum).is_displayed())

    def fill_card_data(self):

        driver.find_element_by_xpath("//input[@id='cardpay-cardnumber']").send_keys(card_number)
        wait
        driver.find_element_by_xpath("//input[@id='cardpay-expmonth']").send_keys(card_month)
        wait
        driver.find_element_by_xpath("//input[@id='cardpay-expyear']").send_keys(card_year)
        wait
        driver.find_element_by_xpath("//input[@id='cardpay-cardholder']").send_keys(card_name)
        wait
        driver.find_element_by_xpath("//input[@id='cardpay-cardsecure']").send_keys(card_cvv2)
        wait
        driver.find_element_by_xpath("//button[@id='cardpay-submit']").click()
        wait.until(lambda self: driver.find_element_by_xpath("//h2[@class='complete__order']/strong").is_displayed())
        print 'third step ok'

