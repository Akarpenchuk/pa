# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
# sys.path.append(os.path.join(os.path.dirname('/home/ace/Documents/git/autotests/dat/base_methods')))


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base_methods.base import BaseClass
import main_page_elements as mpe
import static_page.static_page_elements as stpe
import campaign.campaign_elements as ce



class MainPage(BaseClass):
    
    def __init__(self):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.action = ActionChains(self.driver)


    def check_main_page_elements(self):

        lst = [mpe.LOGO,
            mpe.AUTH_LINK,
            mpe.BANNER_PROMO,
            mpe.BANNER_TRAILER,
            mpe.BANNER_APPS,
            mpe.MENU_CATEGORIES.itervalues().next(),
            mpe.LIST_CAMPAIGN,
            mpe.SOON_END_CAMPAIGNS,
            mpe.COMING_SOON]

        for i in lst:
            if self.driver.find_element_by_xpath(i):
                return True
            return False


    def check_help_menu_items(self):

        self.driver.refresh()

        self.hover(mpe.HELP_DICT.get("MENU_HELP"))
        for i in mpe.HELP_DICT.values():
            element = self.driver.find_element_by_xpath(i)
            if element:
                return True
            return False

    def check_main_menu_items(self):

        menu_category_btn = sorted(mpe.MENU_CATEGORIES.values())

        for i in menu_category_btn:
            self.hover(i)
            
            menu_category_campaign_count = self.driver.find_elements_by_xpath(i + '//a')
            assert len(menu_category_campaign_count) >= 1
            
            menu_category_campaign = self.driver.find_element_by_xpath(i + '//div//a')
            campaign_name = menu_category_campaign.text
            # # sleep(1)
            menu_category_campaign.click()
            self.wait_element_displayed_by_xpath(ce.CAMPAIGN_NAME)

            assert campaign_name == self.driver.find_element_by_xpath(ce.CAMPAIGN_NAME).text
            print campaign_name.encode('utf-8') + 'checked'

            self.driver.back()
            self.driver.find_element_by_xpath(mpe.LIST_CAMPAIGN)
            continue
        return True


    def check_fast_access_buttons(self):
        self.driver.find_elements_by_xpath(fst_btn).click()
        self.check_screen_position()
        self.driver.find_elements_by_xpath(scnd_btn).click()
        self.check_screen_position()
        self.driver.find_elements_by_xpath(thrd_btn).click()
        self.check_screen_position()
        self.driver.find_elements_by_xpath(frth_btn).click()
        self.check_screen_position()
        self.driver.find_elements_by_xpath(ffth_btn).click()
        self.check_screen_position()


    def anonym_verify_reg(self):
        open_register_form = self.driver.find_element_by_xpath(u"//span[contains(text(),'Регистрация')]").click()
        self.wait
        type_nonregister_email = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='email']").send_keys('')
        type_nonregister_password = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='password']").send_keys('')
        click_register_btn = self.driver.find_element_by_xpath(u"//input[@value='Зарегистрироваться']").click()
        self.wait
        register_validation_email = self.driver.find_element_by_xpath("//form[@id='register_form_validate']/div/input[@class='error']").is_displayed()
        register_validation_password = self.driver.find_element_by_xpath("//form[@id='register_form_validate']/div[2]/input[@class='error']").is_displayed()
        verify_privat_policy = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//a[contains(@href,'agreement.pdf')]").is_displayed() #TODO: verify contains text of file
        
        close_popup = self.driver.find_element_by_xpath("//a[@class='popup_close']").click()


    def anonym_verify_auth(self):
        open_login_form = self.driver.find_element_by_xpath(u"//span[contains(text(),'Вход')]").click()
        self.wait
        type_nonregister_email = self.driver.find_element_by_xpath("//form[@id='login_form_validate']//input[@id='username']").send_keys(RAND_EMAIL)
        type_nonregister_password = self.driver.find_element_by_xpath("//form[@id='login_form_validate']//input[@type='password']").send_keys(PASSWORD)
        click_login_btn = self.driver.find_element_by_xpath("//input[@id='login_submit']").click()
        login_validation_email = self.driver.find_element_by_xpath("//form[@id='login_form_validate']/div/input[@class='error']").is_displayed()
        login_validation_password = self.driver.find_element_by_xpath("//form[@id='login_form_validate']/div[2]/input[@class='error']").is_displayed()
        self.wait


    def anonym_verify_recovery(self):
        open_recovery_form = self.driver.find_element_by_xpath(u"//a[contains(text(),'Забыли пароль?')]").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//input[@id='recovery_submit']").is_displayed())
        send_recovery_email = self.driver.find_element_by_xpath("//input[@id='recovery_submit']").click()
        verify_recovery_error = self.driver.find_element_by_xpath("//form[@id='recovery_input_form']/div/input[@class='error']").is_displayed()

        verify_fb_displayed = self.driver.find_element_by_xpath("//a[@id='facebook_auth']/img[contains(@src,'https://media.modnakasta.ua/')]").is_displayed()
        verify_vk_displayed = self.driver.find_element_by_xpath("//a[@id='vkontakte_auth']/img[contains(@src,'https://media.modnakasta.ua/')]").is_displayed()
        verify_gmail_displayed = self.driver.find_element_by_xpath("//a[@id='gmail_auth']/img[contains(@src,'https://media.modnakasta.ua/')]").is_displayed()
        verify_mailru_displayed = self.driver.find_element_by_xpath("//a[@id='mailru_auth']/img[contains(@src,'https://media.modnakasta.ua/')]").is_displayed()

        self.wait.until(lambda self: self.find_element_by_xpath("//a[@class='popup_close']").is_displayed())
        close_popup = self.driver.find_element_by_xpath("//a[@class='popup_close']").click()

    
    def old_anonym_buy_modnakarta(self):
        open_mk_menu_button = self.driver.find_element_by_xpath("//div[@class='container_full main_menu']/ul/li/p/a[@href='/modnakarta/']").click()
        self.wait
        verify_female_button_present = self.driver.find_element_by_xpath("//nav[@class='menu']/div/a[@href='https://modnakasta.ua/f/female/']").is_displayed()
        verify_female_button_present = self.driver.find_element_by_xpath("//nav[@class='menu']/div/a[@href='https://modnakasta.ua/f/male/']").is_displayed()
        verify_female_button_present = self.driver.find_element_by_xpath("//nav[@class='menu']/div/a[@href='https://modnakasta.ua/f/child/']").is_displayed()
        verify_female_button_present = self.driver.find_element_by_xpath("//nav[@class='menu']/div/a[@href='https://modnakasta.ua/f/home/']").is_displayed()
        verify_female_button_present = self.driver.find_element_by_xpath("//nav[@class='menu']/div/a[@href='https://modnakasta.ua/f/foodwine/']").is_displayed()
        verify_female_button_present = self.driver.find_element_by_xpath("//nav[@class='menu']/div/a[@href='https://modnakasta.ua/f/outlet/']").is_displayed()
        verify_female_button_present = self.driver.find_element_by_xpath("//nav[@class='menu']/div/a[@href='https://modnakasta.ua/modnakarta/']").is_displayed()

        add_modnakarta = self.driver.find_element_by_xpath("//form[contains(@action,'/basket/add/')]/input[@type='submit']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//form[@id='login_form_validate']").is_displayed())
        close_auth_popup = self.driver.find_element_by_xpath("//a[@class='popup_close']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())


class Registration:
    """all kinds of registration, validation of forms"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)
        # global NEW_BOT_NAME

    def preconditions(self):
        open_main_page = self.driver.get(BASE_URL)
        #TODO: clear cookies, etc..

    def send_registration_email(self):
        open_registration_popup = self.driver.find_element_by_xpath(u"//a[@href='#auth_popup']/span[contains(text(),'Регистрация')]").click()
        self.wait
        type_new_email = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='email']").send_keys(RAND_EMAIL)
        type_new_password = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='password']").send_keys(PASSWORD)
        submit_form = self.driver.find_element_by_xpath(u"//input[@value='Зарегистрироваться']").click()
        self.wait
        verify_register_is_send_img = self.driver.find_element_by_xpath("//div[@class='recovery_email_img']/img[contains(@src,'recovery_email_img')]").is_displayed()

    def send_registration_email_bot(self, BOT_NAME):

        open_registration_popup = self.driver.find_element_by_xpath(u"//a[@href='#auth_popup']/span[contains(text(),'Регистрация')]").click()
        self.wait

        self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='email']")
        clear_input = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='email']").clear()
        type_new_email = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='email']").send_keys(BOT_NAME+EMAIL_ADDRESS)
        clear_input = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='password']").clear()
        type_new_password = self.driver.find_element_by_xpath("//form[@id='register_form_validate']//input[@name='password']").send_keys(PASSWORD)
        submit_form = self.driver.find_element_by_xpath(u"//input[@value='Зарегистрироваться']").click()
        self.wait
        
        try:
            self.driver.find_element_by_xpath("//div[@class='recovery_email_img']/img[contains(@src,'recovery_email_img')]")
        except:
            self.driver.find_element_by_xpath("//form[@id='register_form_validate']/div[@class='form-item']/input[@class='error']")
            print 'exception'
            return False
        return True
 

    def fill_bot_info_popup(self, BOT_NAME):
        type_first_name = self.driver.find_element_by_xpath("//input[@id='first_name']").send_keys(BOT_NAME)
        last_name_popup = self.driver.find_element_by_xpath("//input[@id='last_name']").send_keys(BOT_NAME)
        personal_info_popup_btn = self.driver.find_element_by_xpath("//input[@id='personal_info_submit']").click()
        self.wait

    def fill_personal_info_popup(self):
        type_first_name = self.driver.find_element_by_xpath("//input[@id='first_name']").send_keys(RAND_NAME)
        last_name_popup = self.driver.find_element_by_xpath("//input[@id='last_name']").send_keys(RAND_NAME)
        personal_info_popup_btn = self.driver.find_element_by_xpath("//input[@id='personal_info_submit']").click()
        self.wait


class Auth:
    """all kinds of authorization, validation of forms"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)


    def auth_form(self):
        click_auth_label = self.driver.find_element_by_xpath("//span[contains(text(),'Вход')]").click()
        self.wait
        type_email = self.driver.find_element_by_xpath("//input[@id='username']").send_keys(USER_EMAIL)
        type_pass = self.driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
        self.wait
        click_auth_btn = self.driver.find_element_by_xpath("//input[@id='login_submit']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//a[@href='/me/']").is_displayed())


#  def auth_fb(self):
#         pass

#     def auth_vk(self):
#         pass

#     def auth_gmail(self):
#         pass

#     def auth_mailru(self):
#         pass

#     def static_elements(self):
#         pass
    
#     def auth_form_validation(self):
#         pass

    def logout(self):
        menu_item = self.driver.find_element_by_xpath("//a[@href='/me/']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//a[@href='/user/registration/logout/']").is_displayed())
        self.driver.find_element_by_xpath("//a[@href='/user/registration/logout/']").click()
        self.wait.until(lambda self: self.find_element_by_xpath(u"//a[@href='#auth_popup']/span[contains(text(),'Регистрация')]").is_displayed())

class Recovery:
    """basic recovery email"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def preconditions(self):
        open_main_page = self.driver.get(BASE_URL)
        #TODO: clear cookies, etc..

    def send_recovery_email(self):
        self.driver.find_element_by_xpath(u"//a[@href='#auth_popup']/span[contains(text(),'Регистрация')]").click()
        self.wait
        open_recovery_form = self.driver.find_element_by_xpath(u"//a[contains(text(),'Забыли пароль?')]").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//form[@id='recovery_input_form']").is_displayed())
        email_intput = self.driver.find_element_by_xpath("//form[@id='recovery_input_form']/div/input[@type='text']").send_keys(USER_EMAIL)
        self.wait
        self.driver.find_element_by_xpath("//input[@id='recovery_submit']").click()
        self.wait
        self.driver.find_element_by_xpath("//div[@class='recovery_email_text']").is_displayed()

    def set_new_password(self):
        self.driver.find_element_by_xpath(u"//input[@placeholder='Новый пароль']").send_keys(PASSWORD)
        self.driver.find_element_by_xpath(u"//input[@placeholder='Новый пароль еще раз']").send_keys(PASSWORD)
        self.wait
        self.driver.find_element_by_xpath(u"//input[@value='Сохранить']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//input[@placeholder='e-mail']").is_displayed())

    def auth_recovery_page(self):
        self.driver.find_element_by_xpath("//input[@placeholder='e-mail']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='e-mail']").send_keys(USER_EMAIL)
        self.driver.find_element_by_xpath(u"//input[@placeholder='Пароль']").clear()
        self.driver.find_element_by_xpath(u"//input[@placeholder='Пароль']").send_keys(PASSWORD)
        self.wait
        self.driver.find_element_by_xpath(u"//input[@value='Вход']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//a[@href='/me/']").is_displayed())

class Menu:
    """base menu and help menu"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def verify_help_menu(self):
        '''hover, verify menu item is present'''

        verify_help_menu_btn = self.driver.find_element_by_xpath("//a[@href='/support/payments/']")
        self.action.move_to_element(verify_help_menu_btn)
        self.action.perform()
        self.wait
        verify_help_menu = self.driver.find_element_by_xpath(u"//ul[@class='dropdown_column']/li/a[contains(text(),'Оплата')]").is_displayed()

    def verify_main_menu(self):
        '''hover and verify menu with banner is present'''

        #check main menu (make verify through the list)
        female_menu = self.driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/female/']")
        self.action.move_to_element(female_menu)
        self.action.perform()
        female_banner = self.driver.find_element_by_xpath("//div[@class='dropdown_banner placeholder']//img")

        male = self.driver.find_element_by_xpath(u"//a[@href='/f/male/']")
        self.action.move_to_element(male)
        self.action.perform()
        male_banner = self.driver.find_element_by_xpath("//div[@class='dropdown_banner placeholder']//img")

        child = self.driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/child/']")
        self.action.move_to_element(child)
        self.action.perform()
        child_banner = self.driver.find_element_by_xpath("//div[@class='dropdown_banner placeholder']//img")

        home = self.driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/home/']")
        self.action.move_to_element(home)
        self.action.perform()
        home_banner = self.driver.find_element_by_xpath("//div[@class='dropdown_banner placeholder']//img")

        outlet = self.driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/outlet/']")
        self.action.move_to_element(outlet)
        self.action.perform()
        outlet_banner = self.driver.find_element_by_xpath("//div[@class='dropdown_banner placeholder']//img")
        
        '''verify belonging pages - open each page and verify campaign is displayed'''

        open_female_page = self.driver.find_element_by_xpath("//div[@class='container_full main_menu']//p/a[@href='/f/female/']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        
        find_first_campaign = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        find_first_campaign_timer = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()
        
        #soon end
        verify_soon_end_title = self.driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        verify_soon_end_campaign = self.driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !

        open_male_page = self.driver.find_element_by_xpath(u"//a[@href='/f/male/']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        
        find_first_campaign = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        find_first_campaign_timer = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()
        
        #soon end
        verify_soon_end_title = self.driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        verify_soon_end_campaign = self.driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !

        open_child_page = self.driver.find_element_by_xpath(u"//a[@href='/f/child/']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        
        find_first_campaign = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        find_first_campaign_timer = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()

        #soon end
        verify_soon_end_title =  self.driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        verify_soon_end_campaign = self.driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !

        open_home_page = self.driver.find_element_by_xpath(u"//a[@href='/f/home/']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        find_first_campaign = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        find_first_campaign_timer = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()

        #soon end
        verify_soon_end_title = self.driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        verify_soon_end_campaign = self.driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()
        #TODO: store product in list and check that any campaign contains 0 days !

        outlet = self.driver.find_element_by_xpath(u"//a[@href='/f/outlet/']").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").is_displayed())
        find_first_campaign = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a")
        find_first_campaign_timer = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div/div[@class='column_timer']").is_displayed()

        #soon end
        verify_soon_end_title = self.driver.find_element_by_xpath(u"//div[contains(text(),'Скоро заканчиваются')]").is_displayed()
        verify_soon_end_campaign = self.driver.find_element_by_xpath("//div[@id='soon_end']/following-sibling::div[@class='row']/div[@class='column_item column_2']/a").is_displayed()

# class Campaign:
#     """describe campaign block (timing, banners, fast scroll buttons, soon end)"""

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#         self.action = ActionChains(driver)



# class Footer:
#     """check static elements"""

#     def __init__(self, self.driver):
#         self.self.driver = self.driver
