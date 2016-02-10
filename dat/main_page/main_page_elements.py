# !/usr/bin/env python
# -*- coding: utf-8 -*-

# HEADER
LOGO = "//a[@class='logo']/img"

# menu catories
FEMALE_CATEGORY_MENU = "//ul[@class='menu_holder']/li/p"

# menu help
MENU_HELP = "//a[@class='menu_item menu_holder_item']/span[contains(text(),'Помощь')]"
MENU_HELP_LIST_ITEM = "//div[@class='user_menu support_menu']//ul[@class='dropdown_column']/li[1]"


# menu profile
PROFILE_LINK = "//a[@href='/me/']"
LOGOUT_LINK = "//a[@href='/user/registration/logout/']"

# authorization
AUTH_LINK = "//div[@class='user_menu login_link']/a"
AUTH_FORM = "//form[@id='login_form_validate']"
AUTH_EMAIL_INPUT = "//div[@id='login_form']//input[@id='username']"
AUTH_EMAIL_INPUT_ERROR = "//form[@id='login_form_validate']//div[@class='form-item']/ul/li"
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
RECOVERY_FORM = "//div[@id='recovery_form']"
RECOVERY_EMAIL_INPUT = "//form[@id='recovery_input_form']//input[@name='email']"
RECOVERY_EMAIL_BTN = "//input[@id='recovery_submit']"
RECOVERY_EMAIL_INPUT_ERROR = "//form[@id='recovery_input_form']/div/input[@class='error']"

# campaigns

#banners

