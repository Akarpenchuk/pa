# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import random
import string
import psycopg2

BASE_URL = "http://modnakasta.ua" # TODO: make a dict 'user_data'
# BASE_URL = "http://mk:mkstaging@catalogue.modnakasta.ua"
EMAIL = "yopmail.com"
EMAIL_ADDRESS = "@yopmail.com"
USER = "mktestuser3"
USER_EMAIL = "mktestuser3@yopmail.com"
PASSWORD = "qwe123"
PHONE = 380639728933
RAND_NAME = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
RAND_EMAIL = RAND_NAME + EMAIL_ADDRESS

CARD_NUBER = "4149 5070 2155 7861" # TODO: make a dict for 'card data'
CARD_MONTH = "07"
CARD_YEAR = "19"
CARD_NAME = "dmytro malovanyi"
CARD_CVV2 = "010"

#MAIN PAGE ELEMENTS
LOGO = "//a[@class='logo']/img"

#CAMPAIGN ELEMENTS

#--campaign data
LIST_CAMPAIGN = "//div[@class='column_item column_1']/a"
LIST_CAMPAIGN_link = "//div[@class='column_item column_1']/a/@href"
LIST_CAMPAIGN_BRAND = "//div[@class='column_item column_1']/div[@class='column_info']/div"
LIST_CAMPAIGN_NAME = ""
LIST_CAMPAIGN_BANNER = ""
LIST_CAMPAIGN_TIMER = ""

SPINNER = "//div[@class='products']/div[@class='spinner']"

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

#price
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
SORT_TITLE_UP = u"//div[@class='sort__by']/span[contains(text(),'По возрастанию цены')]"
SORT_TITLE_DOWN = u"//div[@class='sort__by']/span[contains(text(),'По убыванию цены')]"
SORT_UP_BTN = "//span[@class='accordion__icon-up']"
SORT_DOWN_BTN = "//span[@class='accordion__icon-down']"
#HIDE_SOLD_BTN = u"//div[@class='sidebar__section'][last()]/div[@class='sidebar__filters']/div/label/div[contains(text(),'Скрыть проданные')]/preceding-sibling::input[@class='filters__checkbox']"
HIDE_SOLD_BTN = u"//div[@class='sidebar__section'][last()]/div[@class='sidebar__filters']/div/label/input"
PRODUCT_COUNTER = u"//div[@class='filters-selection__results-right']/span[2]"

#product list data
# global LIST_PRODUCT
LIST_PRODUCT = "//div[@class='product-item_wrapper']"
LIST_PRODUCT_COUNT = 30
LIST_PRODUCT_CARD = "/div[2]/a"
LIST_PRODUCT_PHOTO = "/div[2]/a/img/@src" #.text
LIST_PRODUCT_BRAND = "/div[2]/a/div[@class='product-item__info']/div/span" #.text
LIST_PRODUCT_NAME = "/div[2]/a/div[@class='product-item__info']/div[2]/span" #.text
LIST_PRODUCT_PRICE_NEW = "/div[2]/a/div[@class='product-item__info']/div/span[2]/span" #.text
LIST_PRODUCT_PRICE_OLD = "/div[2]/a/div[@class='product-item__info']/div[2]/span[2]/span" #.text
LIST_PRODUCT_OCB_ADD = "/div[@class='product__add-in-basket']"
LIST_PRODUCT_OCB_SIZE_TITLE = "/div[@class='product__add-in-basket']/div[@class='product__sizes']/label/input/div" #.text
LIST_PRODUCT_OCB_SIZE_ADD = "/div[@class='product__add-in-basket']/div[@class='product__sizes']/label/input"
LIST_PRODUCT_SOLD = u"/div[2]/div[@class='product-status product__sales']/h3[contains(text(),'Продано')]" #.text
LIST_PRODUCT_RESERVED = "/div[2]/div[@class='product-status product__reserved']/h3[contains(text(),'Зарезервировано')]" #.text
SOLD_PRODUCT = u"//h3[contains(text(),'Продано')]"

#PRODUCT DATA
#product states
PRODUCT_ID = ""
PRODUCT_BRAND = "//h1/div[@class='product_author liked']"
PRODUCT_NAME = "//h1/div/following-sibling::div[@class='product_name']"
PRODUCT_NEW_PRICE = ""
PRODUCT_OLD_PRICE = ""
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
PRODUCT_PHOTO_MAIN = ""
PRODUCT_PHOTO_MINI = "//div[@class='product_thumb_overlay']/img[contains(@data-image,'http://media2.modnakasta.ua/imgw/')]"
PRODUCT_ZOOMBOX = ""
PRODUCT_ZOOMBOX_PHOTO_MAIN = ""
PRODUCT_ZOOMBOX_PHOTO_MINI = ""

#popups
POP_STOCK_LIMIT = u"//div[contains(text(),'Ваш запрос превышает лимиты, установленные для заказа.')]"
POP_RESERVATION = ""
POP_SELECT_SIZE = u"//div[contains(text(),'Выберите сначала размер')]"
POP_SKU_ADDED = u"//div[contains(text(),'Ваш товар успешно добавлен в корзину')]"
POP_OPEN_BASKET_BTN = u"//div[@class='popup_notify_bottom']/a[contains(text(),'Оформить заказ')]"
POP_CONTINUE_SHOPING_BTN = u"//div[@class='popup_notify_bottom']/a[contains(text(),'Продолжить покупки')]"

#basket elements


#checkout delivery elements
DELIVERY_COURIER_TYPE = ""
DELIVERY_POST_TYPE = ""
DELIVERY_SELF_TYPE = ""

DELIVERY_COURIER_COST = 35 #TODO: make a dict 'delivery_data'
DELIVERY_POST_COST = 25
DELIVERY_SELF_COST = 0

#checkout payment payments
PAY_BONUS_TYPE = ""
PAY_PERSONAL_ACC_TYPE = ""
PAY_CASH_TYPE = ""
PAY_NONCASH_TYPE = ""

#checkout receipt
COST_SUM = "//span[@class='mol_cost_sum']"
DELIVERY_SUM = "//span[@class='mol_cost_sum']"
TOTAL_SUM = "//div[@class='make_order_total_cost']/span"

# #run db
# conn_string = "host='10.38.0.122' dbname='modnakasta' user='modnakastauser' port='5433'"
# conn = psycopg2.connect(conn_string)
# cursor = conn.cursor()
# print  'Connnected from config to -> %s' % (conn_string)

# #select all existed bots
# cursor.execute("select email from auth_user where email like 'user%' and email like '%\@mailinator.com';")
# RECORDS = cursor.fetchall()


# BOT_COUNT = len(RECORDS) + 1
# BOT_NAME = 'user'+str(BOT_COUNT)

# NEW_BOT_COUNT = len(RECORDS) + 2
# NEW_BOT_NAME = 'user'+str(NEW_BOT_COUNT)




