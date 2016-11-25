#coding = utf-8
from selenium import webdriver
import unittest,time,re
def login(self):
    driver = self.driver
    driver.get(self.base + "/member/login.html")
    driver.find_element_by_id("user_name").clear()
    driver.find_element_by_id("user_name").send_keys("18620369112")
    driver.find_element_by_id("password").send_keys("1234567")
    driver.find_element_by_id("normal-login").click()
    time.sleep(2)




