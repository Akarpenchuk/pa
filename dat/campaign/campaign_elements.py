# !/usr/bin/env python
# -*- coding: utf-8 -*-

#CAMPAIGN ELEMENTS
CAMPAIGN_NAME = "//div[@class='shop_title']/h1"
SPINNER = "//div[@class='products']/div[@class='spinner']"
OUTLET_CATEGORY = "//div[@class='column_item column_2 column_outlet'][1]/a"

#--filters
#affiliation
AFF_WOMAN = u"//div[contains(text(),'Женщинам')]"
AFF_MAN = u"//div[contains(text(),'Мужчинам')]"
AFF_CHILD = u"//div[contains(text(),'Детям')]"
AFF_BOYS = u"//div[contains(text(),'Мальчикам')]"
AFF_GIRLS = u"//div[contains(text(),'Девочкам')]"
AFF_HOME = u"//div[contains(text(),'Дом')]"
AFF_UNI = u"//div[contains(text(),'Унисекс')]"
AFF_ZOO = u"//div[contains(text(),'Животным')]"

#category
CATEGORY_TITLE = u"//div[contains(text(),'Категория')]"
CATEGORY_CHKBOX = "//label[@class='filters__category']/input"
CATEGORY_NAME = "//label[@class='filters__category']/div/span"
CATEGORY_QUANTITY = "//label[@class='filters__category']/div/span[2]"

#CATALOGUE price
PRICE_TITLE = u"//div[contains(text(),'Цена')]"
PRICE_MIN = "//div[@class='horizontal-slider_min-max']/span"
PRICE_MIN_BTN = "//div[@class='horizontal-slider_min-max']/span"
PRICE_MAX = "//div[@class='horizontal-slider_min-max']/span[2]"
PRICE_MAX_BTN = "//div[@class='horizontal-slider_min-max']/span[2]"

#color
COLOR_TITLE = u"//div[contains(text(),'Цвет')]"
COLOR_BTN = u"//div[contains(text(),'Цвет')]/following-sibling::div[@class='sidebar__filters']/div/label/input"
COLOR_NAME = u"//div[contains(text(),'Цвет')]/following-sibling::div[@class='sidebar__filters']/div/label/div"

#size
SIZE_TITLE = u"//div[contains(text(),'Размер')]"
SIZE_BTN = u"//div[contains(text(),'Размер')]/following-sibling::div[@class='sidebar__filters']/div/label/input"
SIZE_NAME = u"//div[contains(text(),'Размер')]/following-sibling::div[@class='sidebar__filters']/div/label/div"

#brand
BRAND_TITLE = u"//div[contains(text(),'Бренд')]"
BRAND_BTN = u"/following-sibling::div[@class='sidebar__filters']/div/label/input"
BRAND_NAME = u"/following-sibling::div[@class='sidebar__filters']/div/label/div"

#product sort
SORT_ASC = "//a[@class='shop_sort_btn shop_sort_asc']"
SORT_DESC = "//a[@class='shop_sort_btn shop_sort_desc']"
SORT_UP_BTN = "//span[@class='accordion__icon-up']"
SORT_DOWN_BTN = "//span[@class='accordion__icon-down']"
HIDE_SOLD = "//a[text()='Скрыть проданные']"
PRODUCT_COUNTER = u"//div[@class='filters-selection__results-right']/span[2]"

#products
PRODUCT = "//div[@class='shop_item shop_item_adaptive']"
PRODUCT_IMG = "//a[@class='shop_item_img ']"
PRODUCT_RESERVED = "//div[@class='shop_reserved']"
PRODUCT_SOLD = "//div[@class='shop_sold']"


PRODUCT_NEW_PRICE = "//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span"
# PRODUCT_OLD_PRICE = "//div[@class='shop_old_cost']"
LAST_PRODUCT = "//div[@class='shop_item shop_item_adaptive'][last()]"



