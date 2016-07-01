# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import mail.mail_elements as me

USER_PASS = "qwe123"
USER_NAME = "mktest1"
USER_EMAIL = "mktest1@mailinator.com"


PROFILE_MENU = "//div[@class='header-top_user header-top_menu-trigger']"
NAME = "//input[@id='id_first_name']"
SURNAME = "//input[@id='id_last_name']"
EMAIL = "//input[@id='id_email']"
GENDER = "//div[@id='id_gender_chzn']/a/span"
PERSONAL_INFO_PHONE = "//input[@id='id_phone']"
PROFILE_LOGOUT_LINK = "//div[@class='header_drop-user header-top_drop-content header-top_drop']/ul[@class='header-top_list-items']/li/a[@href='/user/registration/logout/']"

RESET_ = "//div[@class='_form']"
NEW_PASSWORD = "//input[@name='new_password1']"
NEW_PASSWORD_AGAIN = "//input[@name='new_password2']"
SAVE = "//input[@type='submit']"

RECOVERY_AUTH_EMAIL = "//input[@id='login__email']"
RECOVERY_AUTH_PASS = "//input[@id='login__pass']"

PERSONAL_INFO_BLOCK = "//div[contains(text(),'Персональная информация')]"
PERSONAL_INFO_NAME = "//input[@id='id_first_name']"
PERSONAL_INFO_SURNAME = "//input[@id='id_last_name']"
PERSONAL_INFO_DAY = "//div[@id='id_birthday_day_chzn']/a/span"
PERSONAL_INFO_MONTH = "//div[@id='id_birthday_month_chzn']/a/span"
PERSONAL_INFO_YEAR = "//div[@id='id_birthday_year_chzn']/a/span"
PERSONAL_INFO_GENDER = "//div[@id='id_gender_chzn']/a/span"