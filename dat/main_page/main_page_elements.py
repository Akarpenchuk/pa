# !/usr/bin/env python
# -*- coding: utf-8 -*-

# HEADER
LOGO = "//a[@class='logo']/img"

# menu catories
FEMALE_CATEGORY_MENU = "//ul[@class='menu_holder']/li/p"

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
REG_EMAIL_INPUT = "//*[@id='register_form_validate']//input[@type='password']"
REG_EMAIL_INPUT_ERROR = "//input[@name='email']/following-sibling::label[@class='error']"
REG_PASS_INPUT = "//div[@class='auth_block_right']//input[@type='password']"
REG_PASS_INPUT_ERROR = "//div[@class='auth_block_right']//div[@class='form-item password']/input[@class='error']"
REG_BTN = "//input[@id='register_submit']"

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



SOON_END_CAMPAIGNS = "//div[@id='soon_end']/following-sibling::div[@class='row']//a"
COMING_SOON = "//div[@id='coming_soon']//div[@class='coming_list']/div[@class='coming_item']"

