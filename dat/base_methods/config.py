# !/usr/bin/env/ python
# -*- coding: utf-8 -*-
# fai4Sag/inoo
import random
# import string
import psycopg2

# BASE_URL = "file:///home/ace/Downloads/site%20pages/%D0%94%D0%B5%D1%88%D0%B5%D0%B2%D0%BB%D0%B5!%20%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%20%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD%20%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D1%8B%20%D0%B8%20%D0%BE%D0%B1%D1%83%D0%B2%D0%B8%20-%20%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0,%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B8%20%D0%B8%20%D1%81%D0%BA%D0%B8%D0%B4%D0%BA%D0%B8%20%D0%BD%D0%B0%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B%20%D0%B2%20ModnaKasta.html" # TODO: make a dict 'user_data'
# BASE_URL = "https://modnakasta.ua/catalogue/s-19381-night-mix" # TODO: make a dict 'user_data'
BASE_URL = "https://modnakasta.ua" # TODO: make a dict 'user_data'
# BASE_URL = "http://mk:mkstaging@catalogue.modnakasta.ua"
# BASE_URL = "http://mk:mkstaging@staging.modnakasta.ua"
# EMAIL_DOMAIN = "@mailinator.com"
# RAND_NAME = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
# RAND_EMAIL = RAND_NAME + EMAIL_DOMAIN
# EMAIL_ADDRESS = "https://mailinator.com"
# USER_NAME = "mktest1"
# USER_EMAIL = "mktest1@mailinator.com"
PHONE = 380639728933

CARD_NUBER = "4149 5070 2155 7861" # TOD    O: make a dict for 'card data'
CARD_MONTH = "07"
CARD_YEAR = "19"
CARD_NAME = "dmytro malovanyi"
CARD_CVV2 = "010"


LANDING_URL = "https://modnakasta.ua/landing/nike"

#BASKET

BASKET_ICO = "//a[@href='/basket/']"

#CAMPAIGN ELEMENTS

#--campaign data
LIST_CAMPAIGN_CURRENT = "//*[@id='current']//div/a"
LIST_CAMPAIGN = "//a[contains(@href,'/campaign/')]"
# LIST_CAMPAIGN = "//div[@class='row']/div[@class='column_item column_1']/a"
LIST_CAMPAIGN_LINK = "//div[@class='column_item column_1']/a/@href"
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

#popups
POP_STOCK_LIMIT = u"//div[contains(text(),'Ваш запрос превышает лимиты, установленные для заказа.')]"
POP_RESERVATION = ""
POP_SELECT_SIZE = u"//div[contains(text(),'Выберите сначала размер')]"
POP_SKU_ADDED = u"//div[contains(text(),'Ваш товар успешно добавлен в корзину')]"
POP_OPEN_BASKET_BTN = u"//div[@class='popup_notify_bottom']/a[contains(text(),'Оформить заказ')]"
POP_CONTINUE_SHOPING_BTN = u"//div[@class='popup_notify_bottom']/a[contains(text(),'Продолжить покупки')]"

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

def connect_db(self):
    CONN_STING = "host='10.38.0.122' dbname='modnakasta' user='modnakastauser' port='5433'"
    CONN = psycopg2.connect(conn_string)
    CURSOR = conn.cursor()
    print "Connected!\n"


def query(self, query_sting):
    cursor.execute(query_sting)
    result = cursor.fetchall()
    return result

# #select all existed bots
# cursor.execute("select email from auth_user where email like 'user%' and email like '%\@mailinator.com';")
# RECORDS = cursor.fetchall()


# BOT_COUNT = len(RECORDS) + 1
# BOT_NAME = 'user'+str(BOT_COUNT)

# NEW_BOT_COUNT = len(RECORDS) + 2
# NEW_BOT_NAME = 'user'+str(NEW_BOT_COUNT)
