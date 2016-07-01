# !/usr/bin/env python
# -*- coding: utf-8 -*-
TEST_CAMP = u"//h1[contains(text(),'Скоро заканчиваются')]"

# HEADER
BANNER_CONTAINER_BLOCK = "//div[@class='banners-container']"
LOGO = "//a[@class='header-top_logo']"
PHONE = "//div[@class='header-top_telephone header-top_anon-tel']"
APP_BANNER = "//"
APP_BANNER_CLOSE = "//"

PERSONAL_INFO_POPUP = "//div[contains(text(),'Персональная информация')]"
PERSONAL_INFO_POPUP_NAME = "//input[@id='first_name']"
PERSONAL_INFO_POPUP_SURNAME = "//input[@id='last_name']"
PERSONAL_INFO_POPUP_DAY = "//select[@id='birthday_day']"
PERSONAL_INFO_POPUP_DAY_SELECT = "//select[@id='birthday_day']/option[2]"
PERSONAL_INFO_POPUP_MONTH = "//select[@id='birthday_month']"
PERSONAL_INFO_POPUP_MONTH_SELECT = "//select[@id='birthday_month']/option[2]"
PERSONAL_INFO_POPUP_YEAR = "//select[@id='birthday_year']"
PERSONAL_INFO_POPUP_YEAR_SELECT = "//select[@id='birthday_year']/option[2]"
PERSONAL_INFO_POPUP_GENDER = "//select[@id='gender']"
PERSONAL_INFO_POPUP_GENDER_SELECT = "//select[@id='gender']/option[@value='F']"
PERSONAL_INFO_POPUP_BTN = "//div[@class='popup__profile-bottom']/input[@type='submit']"


NEW_EMAIL_INPUT = "//form[@id='password_reset_valid']//input[@id='id_new_password1']"
NEW_EMAIL_REPEAT_INPUT = "//form[@id='password_reset_valid']//input[@id='id_new_password2']"
NEW_EMAIL_SAVE_BTN = "//form[@id='password_reset_valid']//input[@id='submit_password']"

# menu catories
MENU_CATEGORIES = {
"CATEGORY_FEMALE": "//ul[contains(@class,'nav_content')]/li[1]/a",
"CATEGORY_MALE": "//ul[contains(@class,'nav_content')]/li[2]/a",
"CATEGORY_KIDS": "//ul[contains(@class,'nav_content')]/li[3]/a",
"CATEGORY_HOME": "//ul[contains(@class,'nav_content')]/li[4]/a",
"CATEGORY_OUTLET": "//ul[contains(@class,'nav_content')]/li[5]/a"
}

#modnakarta

MODNAKARTA_HEADER_LINK = "//div[@class='header-top_anon-right']//a[@href='/modnakarta/']"
# MODNAKARTA_MENU_HELP = "//li[@class='header-top_item']//a[@href='/a/about/ModnaKarta/']"
MODNAKARTA_MENU_HELP = "//a[@href='/a/about/ModnaKarta/']"
MODNAKARTA_CAMPAIGN = "//a[@href='/campaign/modnakarta/']"

# menu help
HELP_MENU = {
"MENU_HELP": "//div[text()='Помощь']",
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
PROFILE_CABINET_MENU = "//div[@class='header-top_user header-top_menu-trigger']"
# PROFILE_MENU = "//div[@class='header-top_user']"
HEADER_USER_NAME = "//div[@class='header-top_user']"
PROFILE_LINK = "//a[@href='/me/']"
LOGOUT_LINK = "//a[@href='/user/registration/logout/']"
LOGOUT_MENU_LINK = "//a[@href='/user/registration/logout/']"

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

CLOSE_POPUP = "//div[@id='content']"

# campaigns
CAMPAIGN = "//a[contains(@href,'/campaign/')]"
LIST_CAMPAIGN_CURRENT = "//*[@class='big-small big-small--normal']//a"
CAMPAIGN_WRAPPER = "//div[@class='banners-container']//div"
MENU_CAMPAIGN = "//a[@class='drop-content_item']"



CAMPAIGN_NAME = "//div[@class='banners_title']"
LIST_CAMPAIGN_BANNER = ""
CAMPAIGN_TIMER = "//div[@class='banners_timer-val']/span"


LAST_MINUTES_BTN = "//a[@href='#last-minutes']"
SOON_END_TITLE = u"//h1[text()='Скоро заканчиваются']"
SOON_END_CAMPAIGNS = "//div[@id='last-minutes']//div[@class='banner_item banners--small']"

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


FOOTER = "//footer[@id='footer']"
FOOTER_MOB_APPS = "//div[@class='footer-apps__container']/a:following-sibling/a"
FOOTER_STATIC_PAGES = ["//",]


