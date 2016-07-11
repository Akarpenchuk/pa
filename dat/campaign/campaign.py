# !/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('/home/ace/Documents/git/autotests/dat')
from time import sleep
import random
import re

from selenium import webdriver

from base_methods.wait import Wait
from selenium.webdriver.common.keys import Keys
import unittest

import main_page.main_page_elements as mpe
import campaign_elements as ce

class Campaign():

    def open_rand_campaign(self):
        camp_count = self.count_elements(mpe.CAMPAIGN)
        select = "select count(id) from campaign_campaign where starts_at < now() and finishes_at > now();"
        result = self.db_select(select)
        re.search(str(camp_count), str(result))
        rand_count = random.randint(1, camp_count)
        while 'modnakarta' in self.driver.current_url:
            self.back()
            continue
        self.click('(' + mpe.CAMPAIGN + ')' + '[' + str(rand_count) + ']')
        self.change_to_catalogue()
        self.wait_element(ce.PRODUCT)
        camp_name = self.get_text(ce.CAMPAIGN_NAME)
        print 'camp_name', camp_name
        return camp_name.decode('utf-8')

        #check catalogue details
        self.find_text(ce.BREADCRUMBS, camp_name)
        self.find_text(ce.CAMPAIGN_NAME, camp_name)
        self.find_list_elements(ce.FILTER_ITEMS)
        self.find(ce.HIDE_SOLD)
        self.find(ce.PRODUCT)

    def change_to_catalogue(self):
        if 'campaign' in self.driver.current_url:
            catalogue = self.driver.current_url.replace('campaign', 'catalogue')
            self.driver.get(catalogue)
            # sleep(2)
            self.wait_element(ce.PRODUCT)
            return True

    def open_campaign_iter_with_affiliations (self):
        campaigns = self.find(mpe.CAMPAIGN)
        for i in xrange(len(campaigns)):
            i += n

            if self.find(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN): #!hover
                
                self.find(mpe.CAMPAIGN_WRAPPER + '[' + str(i) + ']' + mpe.CAMPAIGN).click()
                if self.check_if_outlet():
                    self.find(ce.OUTLET_CATEGORY).click()
                    break
                product_count = self.wait_element(ce.PRODUCT)
                assert product_count >= 1
            return True
        return False

    def open_product_iter(self):
        products = self.driver.find_elements_by_xpath(ce.PRODUCT)
        for i in xrange(1, len(products)):
            # i += 1
            try:
                self.find(ce.PRODUCT + '[' + str(i) + ']' + '/a').click()
                self.wait_element(pe.PRODUCT_BIG_IMG)
                return True
            except:
                self.driver.back()
                self.wait_element(ce.PRODUCT)
            continue

    def add_product_OCB(self):
        name = self.get_text(ce.PRODUCT_NAME)
        count = 1
        price = self.get_text(ce.PRODUCT_NEW_PRICE)
        products = self.count_elements(ce.PRODUCT)
        print 'name %s, price %s' % (name, price)
        self.hover(ce.PRODUCT)
        sleep(1)

        try:
            self.find(ce.PRODUCT_SIZE)
            size = self.get_text(ce.PRODUCT_SIZE)
            # self.product_values = (str(size), ) + (str(name), ) + (str(count), ) + (str(price), )
            # print 'product_values in loop ', self.product_values
            self.click(ce.PRODUCT_SIZE)
            self.find(ce.PRODUCT_SIZE_SELECTED)
            self.click(ce.OCB_ADD_PRODUCT)
            self.wait_element(ce.TOOLTIP_PRODUCT_NAME)
        except:    # try:
            self.wait_element(ce.PRODUCT_WITHOUT_SIZE)
            size = u"Размер: "
            print 'find(ce.PRODUCT_WITHOUT_SIZE)'
            self.click(ce.OCB_ADD_PRODUCT)
            print 'click(ce.OCB_ADD_PRODUCT)'
            self.wait_element(ce.TOOLTIP_PRODUCT_NAME)
        # except:
        #     raise Exception('no available products!')
        # except:
        #     pass
        self.find_text(ce.TOOLTIP_PRODUCT_NAME, name)
        self.find_text(ce.TOOLTIP_PRODUCT_NEW_PRICE, price)
        # print 'product_values at the end', self.product_values
        return (str(size), str(name), str(count), str(price))

    def check_product_less_99(self):
        count = 1
        first_product_price = self.find_text(ce.PRODUCT + '[' + str(count) + ']' + ce.PRODUCT_NEW_PRICE)
        first_product_price = first_product_price.replace(u' грн', '')
        print 'first_product_price ', first_product_price
        first_product_price = int(first_product_price)
        if first_product_price > 99:
            return False
        return True
        print "first_product_price ", first_product_price

    def hide_sold(self):
        self.click(ce.HIDE_SOLD)
        sleep(1)
        self.wait_element(ce.PRODUCT_NEW_PRICE)
        return True

    def sort_asc(self):
        self.click(ce.FILTER_SORT)
        self.wait_element(ce.SORT_ASC)
        self.click(ce.SORT_ASC)
        self.wait_element(ce.PRODUCT_NEW_PRICE)
        sleep(2)

        first_price = self.find_text(ce.PRODUCT_NEW_PRICE)
        first_price = first_price.encode("utf-8").replace('грн', '')
        first_price = first_price.replace(' ', '')
        first_price = int(first_price)
        print "first_price ", first_price
        
        self.scroll_down(ce.LAST_PRODUCT)

        self.wait_element(ce.LAST_PRODUCT + ce.PRODUCT_NEW_PRICE)

        # last_product_name = self.find_text(ce.LAST_PRODUCT + ce.PRODUCT_NAME)
        # print 'last_product_name ', last_product_name

        last_price = self.find_text_few_elements(ce.LAST_PRODUCT, ce.PRODUCT_NEW_PRICE)
        last_price = last_price.encode("utf-8").replace('грн', '')
        last_price = last_price.replace(' ', '')
        last_price = int(last_price)
        print "last_price ", last_price

        self.assertTrue(first_price <= last_price)
        return True
            # print 'first_price <= last_price'
        # print 'first_price > last_price!'

    def sort_desc(self):
        self.find(ce.FILTER_SORT).click()
        self.find(ce.SORT_DESC).click()
        self.wait_element(ce.PRODUCT)   
        
        first_price = self.find(ce.PRODUCT_NEW_PRICE).text
        first_price = int(first_price)
        print first_price

        #get last product
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

        last_price = self.find(ce.LAST_PRODUCT + ce.PRODUCT_NEW_PRICE).text
        last_price = int(last_price)
        print last_price

        assert first_price > last_price

    def affiliation_apply(self):
        self.click(ce.FILTER_ITEMS[0])
        self.wait_element(ce.FIRST_AFF_ITEM)
        aff_list = self.get_items_names_list(ce.AFF_ITEM, ce.AFF_NAME)

        count = 0
        for i in xrange(len(aff_list)):

            count += 1
            print 'i ', i
            self.click(ce.AFF_ITEM + '/div[text()=' + "'" + aff_list[i].decode('utf-8')  + "'" + ']')
            self.wait_element(ce.PRODUCT)
            pp_id = self.get_product_pp_id(ce.FIRST_PRODUCT_LINK)
            pp_id = pp_id.get_attribute("href")
            print 'pp_id ', pp_id
            color_id = self.get_color_id(ce.FIRST_PRODUCT_LINK)
            print 'color_id ', color_id

            code_name = self.get_campaign_code_name(ce.FIRST_PRODUCT_LINK)

            # link = self.find(item)
            # code_name = link.search(r'\w-.*')
            # print 'code_name', code_name
            # code_name = _.group(0)
            # print 'code_name _.group(0)', code_name
            # return 'code_name', code_name
            
            #check total count is changed

            #check url is changed

            #check css

            #check product aff in db
            self.connect_db()
            select = """select pp.affiliation from product_product pp
                            join product_sku ps on ps.product_id=pp.id
                            join campaign_campaign cc on ps.campaign_id=cc.id
                            where pp.pp_id=%d and pp.color_id=%d and cc.id=%s;""" % (pp_id, color_id, code_name)
            self.query()

            #check aff_list is hidden
            self.find
            
    # 2574307:702
    def get_product_pp_id(self, *item):
        sleep(1)
        link = self.find(item)
        link = link.get_attribute("href")
        pp_id = str(link)[9:16]
        print 'pp_id', pp_id
        return pp_id

    def get_color_id(self, item):
        link = self.find(item)
        color_id = str(link)[17:20]
        print 'color_id', color_id
        return color_id

    def get_campaign_code_name(self, item):
        link = self.find(item)
        code_name = link.search(r'\w-.*')
        print 'code_name', code_name
        code_name = _.group(0)
        print 'code_name _.group(0)', code_name
        return 'code_name', code_name

    def check_categories(self):
        pass

    def check_brand(self):
        pass

    def check_size(self):
        pass

    def check_sorting(self):
        pass

    def check_hide_sold(self):
        pass