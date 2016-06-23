# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

PRODUCT_IMG = "//div[@class='img-big']//img"
ADD_PRODUCT_BTN = "//a[@class='in-basket']"
SIZE_AVAILABLE = "//div[@class='product_sizes']/div[normalize-space(@class='sizes__button_on')]"    #XPATH
SIZE_AVAILABLE_CSS = "div[class*='sizes__button_on"                                                                         #CSS
SIZE_SELECTED = "//div[@class='product_sizes']/div[normalize-space(@class='product_size_item sizes__button_on sizes__button_chose')]"
WITHOUT_SIZE = "//div[@class='single_sku']"
PRODUCT_ADDED_MSG = "//div[@class='messages__message info-msg']"


#PRODUCT DATA

#product states
PRODUCT_ID = ""
PRODUCT_BRAND = "//div[@class='manufucturer']"
PRODUCT_NAME = "//div[@class='name']"
PRODUCT_NEW_PRICE = "//span[@class='price_value']/span[1]"
PRODUCT_OLD_PRICE = "//span[@class='old-price']/span[1]"
PRODUCT_SIZE_AVAILABLE = "//div[@class='size-item ']"
PRODUCT_SIZE_SELECTED = "//div[@class='size-item selected']"
PRODUCT_SIZE_ONE = "//div[@class='size-item selected']"
PRODUCT_NO_SIZE = "//div[@class='sizes-block']/noscript"
PRODUCT_SIZE_TABLE = ""
PRODUCT_SKU_COUNT = "//div[@product_sizes]/div/@data-stock"
PRODUCT_SOLD = "//div[@class='product_sold']"
PRODUCT_RESERVED = "//div[@class='product_reserved']"
BASKET_ADD_ENABLED = "//a[text()='В корзину']"
BASKET_ADD_DISABLED = "//a[@class='in-basket disabled']"
PRODUCT_COUNT = "//"
PRODUCT_DESCRIPTION_TAB = ""
PRODUCT_DELIVERY_TAB = ""
PRODUCT_BREADCRUMBS = ""
PRODUCT_BIG_IMG = "//div[@class='img-big']/img"
PRODUCT_MINI_IMG = "//div[@class='img-views']/div/img"
PRODUCT_ZOOMBOX = ""
PRODUCT_ZOOMBOX_PHOTO_MAIN = ""
PRODUCT_ZOOMBOX_PHOTO_MINI = ""
PRODUCT_ADDED = "//div[@class='message']/div[@class='messages__message info-msg']"


