# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from data.main_page.main_page import Anonym

class Test_1(unittest.TestCase):

    driver = webdriver.Chrome()

    def test_open_modnakasta(self, url):

        Anonym(driver).anonym_verify_auth()