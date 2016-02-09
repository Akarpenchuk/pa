# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class Anonym:

    def __init__(self):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def check_validation_reg(self, link, form, email_input, pass_input, reg_btn, fst_error, scnd_error):
        self.driver.find_element_by_xpath(link).click()
        if self.wait_element_displayed_by_xpath(form) == True:

            # invalid email and password
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("slekslienseoi231@@i.ua")
            pass_field = self.driver.find_element_by_xpath(pass_input)
            pass_field.clear()
            pass_field.send_keys("      ")

            self.driver.find_element_by_xpath(reg_btn).click()

            self.driver.find_element_by_xpath(fst_error)
            self.driver.find_element_by_xpath(scnd_error)

            # empty fields
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("")
            pass_field = self.driver.find_element_by_xpath(pass_input)
            pass_field.clear()
            pass_field.send_keys("")

            self.driver.find_element_by_xpath(reg_btn).click()

            self.driver.find_element_by_xpath(fst_error)
            self.driver.find_element_by_xpath(scnd_error)

            # empty password field and valid email
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("mktestuser33333@yopmail.com")
            pass_field = self.driver.find_element_by_xpath(pass_input)
            pass_field.clear()
            pass_field.send_keys("")

            self.driver.find_element_by_xpath(reg_btn).click()

            self.driver.find_element_by_xpath(scnd_error)

            # empty email field and valid password
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("")
            pass_field = self.driver.find_element_by_xpath(pass_input)
            pass_field.clear()
            pass_field.send_keys("qwe123")

            self.driver.find_element_by_xpath(reg_btn).click()

            self.driver.find_element_by_xpath(fst_error)

            return True
        else:
            return False

    def check_validation_auth(self, form, email_input, pass_input, login_btn, fst_error, scnd_error):

        if self.wait_element_displayed_by_xpath(form) == True:

            # not registered email and valid password
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("absolutelynewtestemail@gmail.com")
            pass_field = self.driver.find_element_by_xpath(pass_input)
            pass_field.clear()
            pass_field.send_keys("qwe123")

            self.driver.find_element_by_xpath(login_btn).click()

            self.wait_element_displayed_by_xpath(fst_error)
            self.driver.find_element_by_xpath(scnd_error)

            # invalid registered email and valid password
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("mktestuser 3@gmail.com")
            pass_field = self.driver.find_element_by_xpath(pass_input)
            pass_field.clear()
            pass_field.send_keys("qwe123")

            self.driver.find_element_by_xpath(login_btn).click()

            self.driver.find_element_by_xpath(fst_error)

            # valid registered email and invalid password
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("mktestuser3@gmail.com")
            pass_field = self.driver.find_element_by_xpath(pass_input)
            pass_field.clear()
            pass_field.send_keys("qwe124")

            self.driver.find_element_by_xpath(login_btn).click()

            self.wait_element_displayed_by_xpath(scnd_error)
            # self.driver.find_element_by_xpath(scnd_error)

            # valid registered email and invalid password
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("mkt+estuser3@gmail.com")
            pass_field = self.driver.find_element_by_xpath(pass_input)
            pass_field.clear()
            pass_field.send_keys("qwe12")

            self.driver.find_element_by_xpath(login_btn).click()

            self.driver.find_element_by_xpath(fst_error)
            self.driver.find_element_by_xpath(scnd_error)
            return True
        else:
            return False

    def check_validation_recovery(self, recov_link, recov_form, email_input, send_btn, error):

        self.driver.find_element_by_xpath(recov_link).click()
        self.wait_element_displayed_by_xpath(recov_form)

        if self.wait_element_displayed_by_xpath(recov_form) == True:

            # valid and not registered email
            email_field = self.driver.find_element_by_xpath(email_input)
            sleep(1)
            email_field.clear()
            email_field.send_keys("absolutelynewtestemail@gmail.com")

            self.driver.find_element_by_xpath(send_btn).click()
            self.driver.find_element_by_xpath(send_btn)
            self.driver.find_element_by_xpath(error)

            # empty email field
            email_field.clear()
            email_field.send_keys("")

            self.driver.find_element_by_xpath(send_btn).click()
            self.wait_element_displayed_by_xpath(error)

            # invalid email
            email_field = self.driver.find_element_by_xpath(email_input)
            email_field.clear()
            email_field.send_keys("in valid@@email+com")

            self.driver.find_element_by_xpath(send_btn).click()

            self.wait_element_displayed_by_xpath(error)
            return True
        else:
            return False

    def anonym_buy_product(self):
        pass        

    def anonym_buy_modnakarta(self):
        pass

    def anonym_buy_modnakarta(self):
        pass