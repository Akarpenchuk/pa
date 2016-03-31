# !/usr/bin/env python 
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base_methods.config import *
from base_methods.base import BaseClass

class Campaign:

    def category_filter(self):
        pass

    def price_filter(self):
        pass

    def color_filter(self):
        pass

    def size_filter(self):
        pass

    def brand_filter(self):
        pass

    def hide_sold_filter(self):
        hide_sold = self.find(u"//div[contains(text(),'Скрыть проданные')]").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//a[contains(@href,'/product/')]").is_displayed())
        applied_hide_sold_url = self.driver.get.current_url
        assert u"sold=Скрыть проданные" in applied_hide_sold_url

    # def campaign_filters(self):
        #check category filter
        select_campaign = self.driver.find_element_by_xpath("//div[@class='row margin-top']/div[@class='column_item column_1']/a").click()
        self.wait
        try:
            if self.driver.find_element_by_xpath("//div[@class='column_item column_2 column_outlet']").is_displayed():
                print 'outlet'
                select_category = self.driver.find_element_by_xpath("//div[@class='column_item column_2 column_outlet']/a[contains(@href,'/campaign/')]").click()
                self.wait.until(lambda self: self.driver.find_element_by_xpath("//div[@class='row']/div[@class='shop_item']").is_displayed())
            else:
                print 'not outlet'
        except:
            pass
        
        common_product_count = self.driver.find_elements_by_xpath("//div[@class='row']/div[@class='shop_item']")
        print 'common_product_count', len(common_product_count)
        select_category_list = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div/a").click()
        self.wait
        select_category = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[1]//ul//li[3]").click()
        self.wait
        category_product_count = self.driver.find_elements_by_xpath("//div[@class='row']/div[@class='shop_item']")
        print 'category_product_count', len(category_product_count)
        
        current_url = self.driver.current_url
        print current_url 
        
        assert '?category=' in current_url
        
        assert len(common_product_count) != len(category_product_count)
        print 'category is changing'

        #switch category back
        select_category_menu = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div/a").click()
        self.wait
        select_category = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[1]//ul//li[1]").click()
        self.wait
        common_product_count = self.driver.find_elements_by_xpath("//div[@class='row']/div[@class='shop_item']")

        assert len(common_product_count) != len(category_product_count)
        print 'category is switching back'

        #check brand filter
        try:
            select_brand_menu = self.driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]/a").click()
            self.wait
            print 'select simple category'
        except:
            self.driver.find_element_by_xpath("//div[@class='column_item column_2 column_outlet'][1]/a").click()
            self.wait.until(lambda self: self.driver.find_element_by_xpath("//div[@class='row']/div[@class='shop_item']").is_displayed())
            print 'select outlet category'
        self.wait
        brand_name = self.driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]//ul//li[2]").text
        print 'brand_name', brand_name.encode('utf-8')
        select_brand = self.driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]//ul//li[2]").click()
        self.wait
        #verify first and last product contains brand_name
        fst_product_brand = self.driver.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_name']/span[contains(text(),'%s')]" % brand_name)
        lst_product_brand = self.driver.find_element_by_xpath("//div[@class='row']/div[last()]//div[@class='shop_item_name']/span[contains(text(),'%s')]" % brand_name)
        #TODO: assert product_brand == any item of list

        #switch brand back
        select_brand_menu = self.driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]/a").click()
        self.wait
        select_brand = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[2]//ul//li[1]").click()
        self.wait
        default_brand = self.driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[2]/a/span").text
        assert u'Бренд' in default_brand

        #check size filter
        select_size_menu = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]/a").click()
        self.wait
        select_size = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]//ul//li[2]").click()
        self.wait
        size_name = self.driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[3]/a/span").text
        print 'size_name', size_name.encode('utf-8')

        fst_product = self.driver.find_element_by_xpath("//div[@class='row'][1]/div[1]/a").click()
        self.wait
        fst_product_size = self.driver.find_element_by_xpath(u"//div[@class='product_sizes']/div[contains(text(),'%s')]" % size_name)
        self.driver.back()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]/a").is_displayed())

        lst_product = self.driver.find_element_by_xpath("//div[@class='row']/div[last()]/a").click()
        self.wait.until(lambda self: self.find_element_by_xpath(u"//div[@class='product_sizes']/div[contains(text(),'%s')]" % size_name).is_displayed())
        lst_product_size = self.driver.find_element_by_xpath(u"//div[@class='product_sizes']/div[contains(text(),'%s')]" % size_name)
        self.driver.back()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]/a").is_displayed())
        
        #switch size back
        select_size_menu = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]/a").click()
        self.wait
        select_brand = self.driver.find_element_by_xpath("//div[@class='shop_views_settings']/div[3]//ul//li[1]").click()
        self.wait
        default_size = self.driver.find_element_by_xpath(u"//div[@class='shop_views_settings']/div[3]/a/span").text
        assert u'Размер' in default_size

        #check price sort by asc
        select_sortUp = self.driver.find_element_by_xpath("//div[@class='shop_sort']/a").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").is_displayed())
        fst_product_price = self.driver.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").text
        print 'fst_product_price', fst_product_price
        lst_product_price = self.driver.find_element_by_xpath("//div[@class='row'][last()]/div[last()]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").text
        print 'lst_product_price', lst_product_price
        assert int(fst_product_price) < int(lst_product_price)

        #check price sort by desc
        select_sortDown = self.driver.find_element_by_xpath("//div[@class='shop_sort']/a[2]").click()
        self.wait.until(lambda self: self.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").is_displayed())
        fst_product_price = self.driver.find_element_by_xpath("//div[@class='row'][1]/div[1]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").text
        print 'fst_product_price', fst_product_price
        lst_product_price = self.driver.find_element_by_xpath("//div[@class='row'][last()]/div[last()]//div[@class='shop_item_cost']/div[@class='shop_new_cost']/span").text
        print 'lst_product_price', lst_product_price
        assert int(fst_product_price) > int(lst_product_price)

        #check hide sold filter
        select_hide_sold = self.driver.find_element_by_xpath(u"//a[contains(text(),'Скрыть проданные')]").click()
        self.wait
        try:
            sold_is_present = self.driver.find_element_by_xpath("//div[@class='shop_sold']").is_displayed()
            assert sold_is_present == True
        except:
            print 'sold is not present'
        