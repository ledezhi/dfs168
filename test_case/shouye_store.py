#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re

class Store(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.base_url="https://www.dfs168.com"
		self.driver.maximize_window()
		self.verificationErrors=[]
		self.accept_next_alert=True
		
	def test_store1(self):
		driver=self.driver
		driver.get(self.base_url)
		driver.find_element_by_xpath("html/body/div[9]/div[1]/div/a").click()
		current_url=driver.current_url
		if current_url == "http://www.dfs168.com/store/index.html":
			print "农资店链接OK"
		else:
			raise NameError("链接错误")

	def test_store2(self):
		driver=self.driver
		driver.get(self.base_url)
		driver.find_element_by_xpath("html/body/div[9]/div[1]/div/a").click()
		driver.find_element_by_xpath(".//*[@id='store-local']/div[1]/div[2]/a[1]/img").click()
		store_name=driver.find_element_by_xpath("html/body/div[7]/div/div[3]/h3").text
		if store_name == u"大丰收农资商城官方旗舰店":
			print "正常跳转至大丰收农资商城官方旗舰店店铺首页"
		else:
			raise NameError("链接错误")
	def test_store3(self):
		u"""大丰收农资商城官方旗舰店首页-店铺简介"""
		driver=self.driver
		driver.get(self.base_url)
		driver.find_element_by_xpath("html/body/div[9]/div[1]/div/a").click()  #农资店
		driver.find_element_by_xpath(".//*[@id='store-local']/div[1]/div[2]/a[1]/img").click()  #大丰收官方
		driver.find_element_by_xpath("html/body/nav/div/ul/li[2]/a").click()  #店铺简介
		title_name=driver.find_element_by_xpath("html/body/div[9]/article/section[1]/div/div[1]/h4").text  #简介页面
		if title_name == u"店铺简介":
			print "店铺首页"
		else:
			raise NameError("error")

	def test_store4(self):
		driver=self.driver
		driver.get(self.base_url)
		driver.find_element_by_xpath("html/body/div[9]/div[1]/div/a").click()
		driver.find_element_by_xpath(".//*[@id='store-local']/div[1]/div[2]/a[2]/img").click()
		store_name=driver.find_element_by_xpath("html/body/div[7]/div/div[3]/h3").text
		if store_name == u"大丰收日用百货专营店":
			print "正常跳转至大丰收日用百货店铺首页"
		else:
			raise NameError("链接错误")

	# def test_store5(self):
	# 	driver=self.driver
	# 	driver.get(self.base_url + '/store.html')
	# 	driver.

	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)


if __name__ == '__main__':
	unittest.main()