# !/usr/bin/env python
# -*- coding: utf-8 -*-

EMAIL_INPUT = "//input[@id='inboxfield']"

EMAIL_CHECK_BTN = "//span[@class='input-group-btn']"
EMAIL_INBOX = "//ul[@id='mailcontainer']/li/a/div[2]"
# EMAIL_SELECT_LETTER = "//ul[@id='mailcontainer']/li/a"
EMAIL_SELECT_LETTER = "//ul[@id='mailcontainer']/li//div/parent::a"
SELECT_FRAME = "//iframe[@name='rendermail']"

SELECT_REG_BTN = "//*[@id='mailshowdivbody']/iframe"
EMAIL_REG_BTN = "html/body/div/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/font/a"
SELECT_RECOVERY_LINK = "html/body/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/p[4]/font/font/a"
# EMAIL_REG_BTN = "//a[contains(text(),'https://modnakasta.ua/user/confirm/')]"
