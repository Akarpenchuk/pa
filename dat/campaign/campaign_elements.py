# !/usr/bin/env python
# -*- coding: utf-8 -*-

#CAMPAIGN ELEMENTS
CAMPAIGN_NAME = "//h1[@class='main-content__campaign-name']"
SPINNER = "//div[@class='spinner']"
OUTLET_CATEGORY = "//div[@class='column_item column_2 column_outlet'][1]/a"
BREADCRUMBS = "//div[@class='bread_crumbs']//span"

#--filters
FILTER_ITEMS = ["//div[text()='Принадлежность']", "//div[text()='Категория']", "//div[text()='Цвет']", "//div[text()='Размер']", "//div[text()='Бренд']", "//div[text()='Сортировка']"]


#affiliation
AFF_ITEM = "//div[@class='filters_list affiliation']/label"
FIRST_AFF_ITEM = "//label[@class='filters__item']/div"
SELECTED_AFF = "//"
AFF_NAME = "//div[@class='filters_list affiliation']/label/div"
AFFILIATIONS = {
	u"Женщинам": "F",
	u"Мужчинам": "M",
	u"Унисекс": "FM",
	u"Детям": "C",
	u"Мальчикам": "C",
	u"Девочкам": "C",
	u"Дом": "H",
	u"Продукты и напитки": "A, P",
	u"Зоотовары": "H"
}


AFF_LIST = {
	"AFF_WOMAN": u"//div[contains(text(),'Женщинам')]",
	"AFF_MAN": u"//div[contains(text(),'Мужчинам')]",
	"AFF_CHILD": u"//div[contains(text(),'Детям')]",
	"AFF_BOYS": u"//div[contains(text(),'Мальчикам')]",
	"AFF_GIRLS": u"//div[contains(text(),'Девочкам')]",
	"AFF_HOME": u"//div[contains(text(),'Дом')]",
	"AFF_UNI": u"//div[contains(text(),'Унисекс')]",
	"AFF_ZOO": u"//div[contains(text(),'Животным')]"
}

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
FILTER_SORT = "//div[contains(text(),'Сортировка')]"
SORT_ASC = "//label[@class='filters__item'][1]/div"
SORT_DESC = "//label[@class='filters__item'][2]/div"
SORT_UP_BTN = "//span[@class='accordion__icon-up']"
SORT_DOWN_BTN = "//span[@class='accordion__icon-down']"
HIDE_SOLD = "//div[text()='Скрыть проданное']"
PRODUCT_COUNTER = u"//div[@class='filters-selection__results-right']/span[2]"

#products
PRODUCT = "//div[@class='product_item_wrap']//a"
PRODUCT_DESCRIPTION_BLOCK = "//div[@class='product_item product_item_full']"
PRODUCT_IMG = "//a[@class='shop_item_img ']"
PRODUCT_RESERVED = "//div[@class='shop_reserved']"
PRODUCT_SOLD = "//div[@class='shop_sold']"
PRODUCT_NEW_PRICE = "//span[@class='product_item__new-cost']"
PRODUCT_NAME = "//div[@class='product-info__bottom']/span[@class='product_item__category']"
PRODUCT_BRAND = "//div[@class='product-info__top']/span[@class='product_item__brand']"
# PRODUCT_SIZE = "//div[@class='product_ocb']//div[@class='size_item ']"
PRODUCT_SIZE = "//div[@class='product_ocb']//div[@class='size_list']/div"

PRODUCT_SIZE_SOLD = "//div[@class='product_ocb']//div[@class='size_item unavailable']"
PRODUCT_SIZE_SELECTED = "//div[@class='product_ocb']//div[@class='size_item selected']"
# PRODUCT_WITHOUT_SIZE = "//div[@class='size_list']/node()[not(size_item )]|node()[not(size_item selected)]"
PRODUCT_WITHOUT_SIZE = "//div[@class='size_list'][not(descendant::*)]"
FIRST_PRODUCT = "//div[@class='product_item product_item_full']/a"
# FIRST_PRODUCT_LINK = "//div[@class='product_item product_item_full']/a/@href"
LAST_PRODUCT_LINK = "(//div[@class='product_item product_item_full']/a/@href)[last()]"


# PRODUCT_OLD_PRICE = "//div[@class='shop_old_cost']"
LAST_PRODUCT = "(//div[@class='product_item_wrap'])[last()]"
PRODUCT_LIST = "//div[@id='content']"
PAGE_HEIGHT_ELEMENT = "//div[@class='products']/div"

#OCB
OCB_ADD_PRODUCT = "//div[@class='product_ocb']//div[@class='btn cta ']"

#TOOLTIP
TOOLTIP_PRODUCT_NAME = "//div[@class='msg_product-name']"
TOOLTIP_PRODUCT_SIZE = "//div[@class='msg_product-size']"
TOOLTIP_PRODUCT_QUA = "//div[@class='msg_product-qua']"
TOOLTIP_PRODUCT_NEW_PRICE = "//div[@class='msg_product-price']"

