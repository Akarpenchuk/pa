# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

PRODUCT_IMG = "//div[@class='img-big']//img"
ADD_PRODUCT_BTN = "//a[@class='in-basket']"
SIZE_AVAILABLE = "//div[@class='product_sizes']/div[normalize-space(@class='sizes__button_on')]"    #XPATH
SIZE_AVAILABLE_CSS = "div[class*='sizes__button_on"                                                                         #CSS
SIZE_SELECTED = "//div[@class='product_sizes']/div[normalize-space(@class='product_size_item sizes__button_on sizes__button_chose')]"
WITHOUT_SIZE = "//div[@class='single_sku']"
PRODUCT_ADDED_MESSAGE = "//div[@class='messages__message info-msg']"


#PRODUCT DATA
#product states
PRODUCT_ID = ""
PRODUCT_BRAND = "//h1/div[@class='product_author liked']"
PRODUCT_NAME = "//h1/div/following-sibling::div[@class='product_name']"
PRODUCT_NEW_PRICE = ""
PRODUCT_OLD_PRICE = "//div[@class='shop_old_cost']/span"
PRODUCT_SIZE_AVAILABLE = "//div[normalize-space(@class)='product_size_item sizes__button_on']"
PRODUCT_SIZE_SELECTED = "//div[normalize-space(@class)='product_size_item sizes__button_on sizes__button_chosen']"
PRODUCT_SIZE_ONE = "//div[normalize-space(@class)='product_size_item sizes__button_chosen sizes__button_on']"
PRODUCT_NO_SIZE = ""
PRODUCT_SIZE_TABLE = ""
PRODUCT_SKU_COUNT = "//div[@product_sizes]/div/@data-stock"
PRODUCT_SOLD = "//div[@class='product_sold']"
PRODUCT_RESERVED = "//div[@class='product_reserved']"
PRODUCT_ADD_ENABLED = "//a[@data-url='/basket/add/']"
PRODUCT_ADD_DISABLED = "//a[@class='btn btn_red product_basket_btn  btn_size_disabled']"
PRODUCT_DESCRIPTION_TAB = ""
PRODUCT_DELIVERY_TAB = ""
PRODUCT_BREADCRUMBS = ""
PRODUCT_BIG_IMG = "//div[@class='img-big']"
PRODUCT_MINI_IMG = "//div[@class='img-views']/div/img"
PRODUCT_ZOOMBOX = ""
PRODUCT_ZOOMBOX_PHOTO_MAIN = ""
PRODUCT_ZOOMBOX_PHOTO_MINI = ""
PRODUCT_ADDED = "//div[@class='message']/div[@class='messages__message info-msg']"


