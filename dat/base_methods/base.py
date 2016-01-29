# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest


class BaseClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def url_open(self, url):
        self.driver.get(url)