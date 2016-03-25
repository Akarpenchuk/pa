# !/usr/bin/env python
# -*- coding: utf-8 -*-

# HEADER
BANNER_CONTAINER_BLOCK = "//div[@class='banners-container']"
LOGO = "//a[@class='header-top_logo']"
PHONE = "//div[@class='header-top_telephone header-top_anon-tel']"


NEW_EMAIL_INPUT = "//form[@id='password_reset_valid']//input[@id='id_new_password1']"
NEW_EMAIL_REPEAT_INPUT = "//form[@id='password_reset_valid']//input[@id='id_new_password2']"
NEW_EMAIL_SAVE_BTN = "//form[@id='password_reset_valid']//input[@id='submit_password']"

# menu catories
MENU_CATEGORIES = {
"CATEGORY_FEMALE": "//ul[@class='nav_content']/li[1]/a",
"CATEGORY_MALE": "//ul[@class='nav_content']/li[2]/a",
"CATEGORY_KIDS": "//ul[@class='nav_content']/li[3]/a",
"CATEGORY_HOME": "//ul[@class='nav_content']/li[4]/a",
"CATEGORY_OUTLET": "//ul[@class='nav_content']/li[5]/a"
}

MENU_CAMPAIGN = "//a[@class='drop-content_item']"

#modnakarta
MODNAKARTA_HEADER_LINK = "//div[@class='header-top_anon-right']//a[@href='/modnakarta/']"
MODNAKARTA_MENU_HELP = "//li[@class='header-top_item']//a[@href='/a/about/ModnaKarta/']"
MODNAKARTA_CAMPAIGN = "//a[@href='/campaign/modnakarta/']"

# menu help
HELP_DICT = {
"MENU_HELP": "//div[contains(text(),'Помощь')]",
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
PROFILE_MENU = "//div[@class='header-top_user']"
PROFILE_LINK = "//a[@href='/me/']"
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
REG_FORM_SEND_LOGO = "//div[@class='popup__recovery-email-img']"

# recovery
RECOVERY_EMAIL_LINK = "//a[@class='popup__forgot-pass-text']"
RECOVERY_EMAIL_FORM = "//form[@class='popup__left-form']/h2[text()='Восстановление пароля']"
RECOVERY_EMAIL_INPUT = "//form[@class='popup__left-form']//input[@id='email']"
RECOVERY_EMAIL_BTN = "//form[@class='popup__left-form']//input[@value='Отправить на почту']"
RECOVERY_EMAIL_INPUT_ERROR = "//form[@class='popup__left-form']//div[@class='error']"

# campaigns
LIST_CAMPAIGN_CURRENT = "//*[@class='big-small big-small--normal']//a"
LIST_CAMPAIGN = "//a[contains(@href,'/campaign/')]"

LIST_CAMPAIGN_LINK = "//div[@class='column_item column_1']/a/@href"
LIST_CAMPAIGN_BRAND = "//div[@class='column_item column_1']/div[@class='column_info']/div"
LIST_CAMPAIGN_NAME = ""
LIST_CAMPAIGN_BANNER = ""
LIST_CAMPAIGN_TIMER = ""


LAST_MINUTES_BTN = "//a[@href='#last-minutes']"
SOON_END_TITLE = "//div[text()='Скоро заканчиваются']"
SOON_END_CAMPAIGNS = "//div[@id='soon_end']/following-sibling::div[@class='row']/div"
SOON_END_CAMPAIGN = "//div[@class='column_item column_2']/a"
SOON_END_CAMPAIGN_TIME = "//div[@id='soon_end']/following-sibling::div[@class='row']//div[@class='timer_time']"


SOON_BTN = "//a[@href='#soon']"
COMING_SOON_ITEMS = [
"//div[@class='coming-soon__content']/div[@class='block'][1]/div[@class='coming-item']//span",
"//div[@class='coming-soon__content']/div[@class='block'][2]/div[@class='coming-item']//span",
"//div[@class='coming-soon__content']/div[@class='block'][3]/div[@class='coming-item']//span"
]

COMING_SOON_DATES = [
"//div[@class='coming-soon__content']/div[@class='block'][1]//span[@class='pink']",
"//div[@class='coming-soon__content']/div[@class='block'][2]//span[@class='pink']",
"//div[@class='coming-soon__content']/div[@class='block'][3]//span[@class='pink']"
]

FAST_ACCESS_BTNS = [
"//a[@href='#last-minutes']",
"//a[@href='#soon']",
"//a[@href='#up']"
]




