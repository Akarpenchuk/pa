# !/usr/bin/env python
# -*- coding: utf-8 -*-

DELETE_BTN = "//div[@class='cart_product-delete']"
EMPTY_BASKET_ICO = "//div[@class='empty-cart']/img"
EMPTY_BASKET_MSG = "//p[contains(text(),'Ваша корзина пуста.')]"
BASKET_ICO = "//a[@class='header-top_basket']"
PRODUCT_NAME = "//a[@class='cart_product-category']"
PRODUCT_BRAND = "//a[@class='cart_product-name']"
PRODUCT_NEW_PRICE = "//div[@class='cart_product-price']"
MIN_BASKET_MSG = "//div[contains(text(),'Сумма заказа должна быть не менее 99 грн.')]"
# MIN_BASKET_MESSAGE = "//div[@class='messages__message error-msg']"

BASKET_CART = "//div[@class='cart']"
CHECKOUT_BTN = "//button[contains(text(),'Оформить заказ')]"
BASKET_SUM = "//"
PRODUCT_COUNT = "//"
PRODUCT_COUNTER = "//"
INCREASE_ON_TWO = "//"

#CART
FST_CART = "//div[@class='cart']"
FST_NAME = "//div[@class='cart_product-info']/a[1][text()]"
FST_BRAND = "//div[@class='cart_product-info']/a[2][text()]"
FST_SIZE = "//div[@class='cart_product-info']/span[text()]"
FST_COUNT = "//div[@class='cart_product-item']//select"
FST_NEW_PRICE = "//div[@class='cart_product-item']//div[@class='cart_product-price']"
