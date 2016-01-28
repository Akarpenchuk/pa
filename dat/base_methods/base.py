# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

        def __init__(self):

            self.driver = webdriver.Chrome()

        def openUrl(url):
            current_url = driver.get(url)
            try:
                current_url.is_displayed()
                print url + 'is displayed'
            except:
                print url + 'is not displayed'

        def closeBrowser():
            driver.close()
        

