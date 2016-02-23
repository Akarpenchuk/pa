# !/usr/bin/env python
# -*- coding: utf-8 -*-

# HEADER
LOGO = "//a[@class='logo']/img"
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

# menu catories
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
"MENU_HELP": "//div[@class='user_menu support_menu']/a/span",
"MENU_HELP_PAYMENT": "//div[@class='user_menu support_menu']//span[contains(text(),'Оплата')]",
"MENU_HELP_DELIVERY": "//div[@class='user_menu support_menu']//span[contains(text(),'Доставка')]",
"MENU_HELP_REFOUND": "//div[@class='user_menu support_menu']//span[contains(text(),'Возврат')]",
"MENU_HELP_MODNAKARTA": "///div[@class='user_menu support_menu']//span[contains(text(),'Modnakarta')]",
"MENU_HELP_PERSONAL_ACCOUNT": "//div[@class='user_menu support_menu']//span[contains(text(),'Персональный счет')]",
"MENU_HELP_BONUSES": "//div[@class='user_menu support_menu']//span[contains(text(),'Бонусы')]",
"MENU_HELP_FAQ": "//div[@class='user_menu support_menu']//span[contains(text(),'Вопросы-ответы')]",
"MENU_HELP_CONTACTS": "//div[@class='user_menu support_menu']//span[contains(text(),'Контакты')]",
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
AUTH_LINK = "//div[@class='user_menu login_link']/a"
AUTH_FORM = "//form[@id='login_form_validate']"
AUTH_EMAIL_INPUT = "//div[@id='login_form']//input[@id='username']"
AUTH_EMAIL_INPUT_ERROR = "//form[@id='login_form_validate']//div[@class='form-item']/input[@class='error']"
AUTH_PASS_INPUT = "//div[@id='login_form']//input[@type='password']"
AUTH_PASS_INPUT_ERROR = "//div[@id='login_form']//div[@class='form-item password']/input[@class='error']"
AUTH_BTN = "//input[@id='login_submit']"

# registration
REG_LINK = "//div[@class='user_menu registration_link']/a"
REG_FORM = "//form[@id='register_form_validate']"
REG_EMAIL_INPUT = "//*[@id='register_form_validate']//input[@name='email']"
REG_EMAIL_INPUT_ERROR = "//input[@name='email']/following-sibling::label[@class='error']"
REG_PASS_INPUT = "//div[@class='auth_block_right']//input[@type='password']"
REG_PASS_INPUT_ERROR = "//div[@class='auth_block_right']//div[@class='form-item password']/input[@class='error']"
REG_BTN = "//input[@id='register_submit']"
REG_FORM_SEND_LOGO = "//div[@id='register_ok']/div/img"

# recovery
RECOVERY_EMAIL_LINK = "//a[@id='forgot_password']"
RECOVERY_EMAIL_FORM = "//div[@id='recovery_form']"
RECOVERY_EMAIL_INPUT = "//form[@id='recovery_input_form']//input[@name='email']"
RECOVERY_EMAIL_BTN = "//input[@id='recovery_submit']"
RECOVERY_EMAIL_INPUT_ERROR = "//form[@id='recovery_input_form']/div/input[@class='error']"

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





