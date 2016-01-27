# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from data.config import *

class Test(unittest.TestCase):


   def test_case(self):

      driver = webdriver.Chrome()

      Anonym(driver).preconditions(BASE_URL)
      Anonym(driver).anonym_verify_reg()
      Anonym(driver).anonym_verify_auth()
      Anonym(driver).anonym_verify_recovery()
      Menu(driver).verify_help_menu()
      Menu(driver).verify_main_menu()
      Anonym(driver).anonym_buy_modnakarta()

      driver.close()

if __name__ == "__main__":
    print 'running'
    unittest.main()


