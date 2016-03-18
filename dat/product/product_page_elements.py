# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

PRODUCT_IMG = "//div[@class='img-big']//img"
PRODUCT_BASKET_ADD = "//a[@class='in-basket']"
SIZE_AVAILABLE = "//div[@class='product_sizes']/div[normalize-space(@class='sizes__button_on')]"    #XPATH
SIZE_AVAILABLE_CSS = "div[class*='sizes__button_on"                                                                         #CSS
SIZE_SELECTED = "//div[@class='product_sizes']/div[normalize-space(@class='product_size_item sizes__button_on sizes__button_chose')]"
WITHOUT_SIZE = "//div[@class='single_sku']"
PRODUCT_ADDED_MESSAGE = "//div[@class='messages__message info-msg']"



