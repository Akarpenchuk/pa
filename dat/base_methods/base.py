# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from selenium import webdriver
import unittest
from wait import Wait


class BaseClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def open_url(self, url):
        self.driver.get(url)