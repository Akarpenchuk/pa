# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from data.config import *
from data.main_page.main_page import Recovery, Auth
from data.mail.mail import Mail

class Test(unittest.TestCase):
'''recovery email'''

    def test_case(self):

        driver = webdriver.Firefox()

        Recovery(driver).preconditions()
        Recovery(driver).send_recovery_email()
        Mail(driver).verify_recovery_email()
        Recovery(driver).set_new_password()
        Recovery(driver).auth_recovery_page()
        Auth(driver).logout()
        Auth(driver).auth_form()
        Auth(driver).logout()

        driver.quit()


if __name__ == "__main__":
    print 'running'
    unittest.main()