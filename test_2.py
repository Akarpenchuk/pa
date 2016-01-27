# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from data.main_page.main_page import Registration
from data.mail.mail import Mail
from data.cabinet.cabinet import PersonalInfo
from data.config import *

class Test(unittest.TestCase):


   def test_case(self):

      driver = webdriver.Chrome()

      # Registration(driver).preconditions()
      Registration(driver).send_registration_email()
      Mail(driver).verify_registration_email()
      Registration(driver).fill_personal_info_popup()
      PersonalInfo(driver).verify_user_email()

      driver.quit()
   
if __name__ == "__main__":
    print 'running'
    unittest.main()
