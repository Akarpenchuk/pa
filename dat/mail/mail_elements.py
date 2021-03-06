# !/usr/bin/env python
# -*- coding: utf-8 -*-

EMAIL_ADDRESS = "https://mailinator.com"
EMAIL_DOMAIN = "@mailinator.com"

EMAIL_INPUT = "//input[@id='inboxfield']"

EMAIL_CHECK_BTN = "//span[@class='input-group-btn']"
EMAIL_INBOX = "//ul[@id='mailcontainer']/li/a/div[2]"
REGISTRATION_EMAIL = "//div[contains(text(),'Подтвердите регистрацию')]"
RECOVERY_EMAIL = "//div[contains(text(),'Восстановление пароля на modnaKasta')]"
LAST_EMAIL_TIME = "//div[contains(@class,'hidden-xs')]//div[@class='innermail ng-binding']"
OLD_EMAIL =  "//div[text()='Замена пароля не удалась']"
DELETE_ALL_EMAILS = "//button[@title='Delete']/i"
EMAIL = "//div[@ng-repeat='email in emails']"
EMAIL_CHECKBOX = "//label"
EMPTY_EMAIL_BOX_MSG = "//div[contains(text(),'This Inbox is currently Empty')]"

SELECT_FRAME = "//iframe[@id='publicshowmaildivcontent']"

TEXT = "//b[contains(text(),'Пожалуйста, подтвердите регистрацию на сайте modnaKasta.ua.')]"
SELECT_REG_BTN = "//*[@id='mailshowdivbody']/iframe"
EMAIL_REG_BTN = "//a[text()='Подтвердить регистрацию']"
SELECT_RECOVERY_LINK = "//a[contains(text(),'https://modnakasta.ua/user/password/reset/confirm/')]"
