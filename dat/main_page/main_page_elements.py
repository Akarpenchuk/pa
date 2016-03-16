# !/usr/bin/env python
# -*- coding: utf-8 -*-

# HEADER
LOGO = "//a[@class='header-top_logo']"
FAST_ACCESS_BTNS = "//div[@class='right_menu_fixed right_widget']/ul/li"
PERSONAL_INFO_POPUP = "//span[@class='h2']"
PERSONAL_INFO_POPUP_NAME = "//input[@id='first_name']"
PERSONAL_INFO_POPUP_SURNAME = "//input[@id='last_name']"
PERSONAL_INFO_POPUP_DATE = "//div[@id='id_birthday_day_chzn']/a"
PERSONAL_INFO_POPUP_DATE_SELECT = "//li[@id='id_birthday_day_chzn_o_2']"
PERSONAL_INFO_POPUP_MONTH = "//div[@id='id_birthday_month_chzn']/a"
PERSONAL_INFO_POPUP_MONTH_SELECT = "//li[@id='id_birthday_month_chzn_o_2']"
PERSONAL_INFO_POPUP_YEAR = "//div[@id='id_birthday_year_chzn']/a"
PERSONAL_INFO_POPUP_YEAR_SELECT = "//li[@id='id_birthday_year_chzn_o_2']"
PERSONAL_INFO_POPUP_GENDER = "//div[@id='id_gender_chzn']/a"
PERSONAL_INFO_POPUP_GENDER_SELECT = "//ul/li[contains(text(),'1910')]"
PERSONAL_INFO_POPUP_SUBMIT = "//input[@id='personal_info_submit']"

PROFILE_ICON = "//span[@id='user_name']"
PROFILE_MENU = "//div[@class='user_menu profile_menu']//li/a[@href='/me/']"

NEW_EMAIL_INPUT = "//form[@id='password_reset_valid']//input[@id='id_new_password1']"
NEW_EMAIL_REPEAT_INPUT = "//form[@id='password_reset_valid']//input[@id='id_new_password2']"
NEW_EMAIL_SAVE_BTN = "//form[@id='password_reset_valid']//input[@id='submit_password']"

# menu catories
MENU_CATEGORY = "//ul[@class='nav_content']/li"
MENU_CATEGORIES = {
"CATEGORY_FEMALE": "//ul[@class='menu_holder']/li[1]",
"CATEGORY_MALE": "//ul[@class='menu_holder']/li[2]",
"CATEGORY_KIDS": "//ul[@class='menu_holder']/li[3]",
"CATEGORY_HOME": "//ul[@class='menu_holder']/li[4]",
"CATEGORY_OUTLET": "//ul[@class='menu_holder']/li[5]"
# "CATEGORY_FOOD&WINE": "//ul[@class='menu_holder']/li[5]",
}

#modnakarta
MODNAKARTA_MENU_BTN = "//li[@class='menu_holder_item'][last()]//a"
MODNAKARTA_MENU_HELP = "//div[@class='user_menu support_menu']//a[@href='/me/prime/']"
MODNAKARTA_CAMPAIGN = "//a[@href='/campaign/modnakarta/']"

# menu help
HELP_DICT = {
"MENU_HELP": "//div[@class='header-top_help']",
"MENU_HELP_PAYMENT": "//div[@class='header-top_help']//a[contains(text(),'Оплата')]",
"MENU_HELP_DELIVERY": "//div[@class='header-top_help']//a[contains(text(),'Доставка')]",
"MENU_HELP_REFOUND": "//div[@class='header-top_help']//a[contains(text(),'Возврат')]",
"MENU_HELP_MODNAKARTA": "//div[@class='header-top_help']//a[contains(text(),'Modnakarta')]",
"MENU_HELP_PERSONAL_ACCOUNT": "//div[@class='header-top_help']//a[contains(text(),'Персональный счет')]",
"MENU_HELP_BONUSES": "//div[@class='header-top_help']a[contains(text(),'Бонусы')]",
"MENU_HELP_FAQ": "//div[@class='header-top_help']//a[contains(text(),'Вопросы-ответы')]",
"MENU_HELP_CONTACTS": "//div[@class='header-top_help']//a[contains(text(),'Контакты')]",
}

# menu profile
PROFILE_LINK = "//a[@href='/me/']"
PROFILE_HEADER_NAME = "//a[@href='/me/']/span"
LOGOUT_LINK = "//a[@href='/user/registration/logout/']"

#banners
BANNER_PROMO = "//div[@id='PH_campaign_002']//img"
BANNER_TRAILER = "//div[contains(@class,'video-banner')]//div[@class='front']/img"
BANNER_APPS = "//div[contains(@class,'flip-container')]//div[@class='front']//img"

# authorization
AUTH_LINK = "//div[@class='header-top_login']"
AUTH_FORM = "//form[@class='popup__left-form']/h2"
AUTH_EMAIL_INPUT = "//form[@class='popup__left-form']//input[@id='username']"

AUTH_EMAIL_INPUT_ERROR = "//div[@class='error']"
AUTH_PASS_INPUT = "//form[@class='popup__left-form']//input[@id='password']"
AUTH_PASS_INPUT_ERROR = "//div[@id='login_form']//div[@class='form-item password']/input[@class='error']"
AUTH_BTN = "//form[@class='popup__left-form']//input[@value='Вход']"

# registration
REG_LINK = "//div[@class='header-top_login']"
REG_FORM = "//form[@class='popup__right-form']/h2"
REG_EMAIL_INPUT = "//form[@class='popup__right-form']//input[@id='email']"
REG_EMAIL_INPUT_ERROR = "//div[@class='error']"
REG_PASS_INPUT = "//form[@class='popup__right-form']//input[@id='password']"
REG_PASS_INPUT_ERROR = "//div[@class='auth_block_right']//div[@class='form-item password']/input[@class='error']"
REG_BTN = "//form[@class='popup__right-form']//input[@value='Зарегистрироваться']"
REG_FORM_SEND_LOGO = "//div[@id='register_ok']/div/img"

# recovery
RECOVERY_EMAIL_LINK = "//a[@class='popup__forgot-pass-text']"
RECOVERY_EMAIL_FORM = "//form[@class='popup__left-form']/h2[text()='Восстановление пароля']"
RECOVERY_EMAIL_INPUT = "//form[@class='popup__left-form']//input[@id='email']"
RECOVERY_EMAIL_BTN = "//form[@class='popup__left-form']//input[@value='Отправить на почту']"
RECOVERY_EMAIL_INPUT_ERROR = "//form[@class='popup__left-form']//div[@class='error']"

# campaigns
LIST_CAMPAIGN_CURRENT = "//*[@id='current']//div/a"
LIST_CAMPAIGN = "//a[contains(@href,'/campaign/')]"

LIST_CAMPAIGN_LINK = "//div[@class='column_item column_1']/a/@href"
LIST_CAMPAIGN_BRAND = "//div[@class='column_item column_1']/div[@class='column_info']/div"
LIST_CAMPAIGN_NAME = ""
LIST_CAMPAIGN_BANNER = ""
LIST_CAMPAIGN_TIMER = ""

SOON_END_TITLE = "//div[text()='Скоро заканчиваются']"
SOON_END_CAMPAIGNS = "//div[@id='soon_end']/following-sibling::div[@class='row']/div"
SOON_END_CAMPAIGN = "//div[@class='column_item column_2']/a"
SOON_END_CAMPAIGN_TIME = "//div[@id='soon_end']/following-sibling::div[@class='row']//div[@class='timer_time']"


COMING_SOON_ITEM = "//div[@id='coming_soon']//div[@class='coming_list']/div[@class='coming_item']"
COMING_SOON_COLUMNS = "//div[@id='coming_soon']//div[@class='coming_list']"

COMING_SOON_DATES = [
"//div[@id='coming_soon']//div[@class='coming_list']/div[1]/span",
"//div[@id='coming_soon']//div[@class='coming_list']/following-sibling::div[2]/div[1]/span",
"//div[@class='coming_list'][1]/div[1]/span"
]





