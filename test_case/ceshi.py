#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from login import lo 
import unittest,time,re

from MYSQLdb import DB


class Person(unittest.TestCase):

	def test_sell(self):
		for i in range(2):
			self.driver = webdriver.Chrome()
			driver=self.driver
			driver.get("http://www.5gfd.com.cn")
			lo(self.driver).pop_login1()
			driver.find_element_by_xpath(".//*[@id='goodsimg_2396']/div[1]/a/img").click()
			driver.switch_to_window(driver.window_handles[1])
			driver.find_element_by_xpath(".//*[@id='content']/div[1]/div[1]/div[2]/div[6]/div[1]/a[1]").click()  #购买
			time.sleep(1)
			driver.find_element_by_xpath(".//*[@id='submit_order_bt']").click()  #提交订单
			time.sleep(1)
			driver.find_element_by_xpath(".//*[@id='pay-payment']/div[1]/div/div[1]/i").click()  #平台
			time.sleep(1)
			driver.find_element_by_xpath(".//*[@id='pay-payment']/div[1]/div/div[4]/div[2]/i").click()  #钱包
			time.sleep(1)
			driver.find_element_by_xpath(".//*[@id='member_paypasswd']").send_keys("li123456")  #支付密码
			driver.find_element_by_xpath(".//*[@id='selectPaymentForm']/div[3]/a").click()  #支付
			driver.quit()

if __name__=='__main__':
	unittest.main()


