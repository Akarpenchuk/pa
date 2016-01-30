# !/usr/bin/env python
# -*- coding: utf-8 -*-
from .config import *
from selenium import webdriver

class KastaClass:

    def __init__(self, driver):
        self.driver = driver

    def openKasta(self, url):
        self.driver.get(url)

class GoogleClass:

    def __init__(self, driver):
        self.driver = driver

    def openGoogle(self, url):
        self.driver.get(url)
