# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from data.main_page.main_page import Registration
from data.mail.mail import Mail
from data.cabinet.cabinet import PersonalInfo
from data.config import *

class Test(unittest.TestCase):
# '''registration in loop'''

   def test_case(self):

      
      #run db
      conn_string = "host='10.38.0.122' dbname='modnakasta' user='modnakastauser' port='5433'"
      conn = psycopg2.connect(conn_string)
      cursor = conn.cursor()
      print  'Connnected from config to -> %s' % (conn_string)
      
      #select all existed bots
      cursor.execute("select email from auth_user where email like 'user%' and email like '%\@mailinator.com';")
      RECORDS = cursor.fetchall()

      BOT_COUNT = len(RECORDS) + 1
      a = 1

      while a <= 100000:     
         
         driver = webdriver.Chrome()

         Registration(driver).preconditions()

         BOT_COUNT += 1
         BOT_NAME = 'user'+str(BOT_COUNT)

         reg = Registration(driver).send_registration_email_bot(BOT_NAME)

         if not reg:
            continue

         Mail(driver).verify_registration_bot(BOT_NAME)
         Registration(driver).fill_bot_info_popup(BOT_NAME)
         PersonalInfo(driver).verify_bot_email(BOT_NAME)
         a += 1
         driver.quit()

if __name__ == "__main__":
    print 'running'
    unittest.main()
