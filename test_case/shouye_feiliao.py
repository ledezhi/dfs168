#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time

class feiliao(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(8)
		self.base_url="http://www.dfs168.com"
		self.verificationErrors=[]
		self.accept_next_alert =True

	# def test_fl1(self):
	# 	u"""首页，点击肥料楼层下的查看更多按钮，验证可正常跳转至肥料首页"""
	# 	driver=self.driver
	# 	driver.get(self.base_url)
	# 	driver.find_element_by_xpath("html/body/div[10]/div/div[1]/div/a").click() #商品页面
	# 	current_url=driver.current_url
	# 	title_name=driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div[1]/div[1]/span").text
	# 	if current_url =="http://www.dfs168.com/goods/category-2382-10.html":
	# 		print "跳转肥料页面"
	# 	else:
	# 		raise NameError("链接错误")
	# def test_fl2(self):
	# 	u"""肥料首页，获取商品列表总页数"""
	# 	driver=self.driver
	# 	driver.get(self.base_url)
	# 	driver.maximize_window()
	# 	driver.find_element_by_xpath("html/body/div[10]/div/div[1]/div/a").click() #商品页面
	# 	time.sleep(3)
	# 	#对象组个数
	# 	total_pages=len(driver.find_elements_by_tag_name("a")) 
	# 	print "total pages is %s" %(total_pages)
	# 	time.sleep(3)
	# def test_fl3(self):
	# 	u"""翻页功能"""
	# 	driver=self.driver
	# 	driver.get(self.base_url)
	# 	driver.maximize_window()
	# 	driver.find_element_by_xpath("html/body/div[10]/div/div[1]/div/a").click()
	# 	time.sleep(2)
	# 	driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div[4]/div/ul/li[13]/span/a").click()
	# 	current_url=driver.current_url
	# 	if current_url == "http://www.dfs168.com/goods/category-2382-10.html?page=2&per-page=16":
	# 		print "下一页按钮功能正常"
	# 	else:
	# 		raise NameError('error')
	def test_fl4(self):
		u"""末页按钮功能正常"""
		driver=self.driver
		driver.get(self.base_url)
		driver.maximize_window()
		driver.find_element_by_xpath("html/body/div[10]/div/div[1]/div/a").click()
		time.sleep(2)
		driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div[4]/div/ul/li[14]/span/a").click()
		current_page=driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div[4]/div/ul/li[12]/span/a").text
		print current_page
		if current_page == '42':
			print "末页数为42"
		else:
			raise NameError('error')
	def test_fl5(self):
		u"""首页及上一页按钮功能正常"""
		driver=self.driver
		driver.get(self.base_url)
		driver.maximize_window()
		driver.find_element_by_xpath("html/body/div[10]/div/div[1]/div/a").click()
		time.sleep(2)
		driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div[4]/div/ul/li[14]/span/a").click()  #末页按钮
		current_page=driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div[4]/div/ul/li[12]/span/a").text #末页数
		driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div[4]/div/ul/li[2]/span/a").click()  #上一页按钮
		current_page1=int(current_page) - 1
		print current_page1
		if current_page1 == 41:
			print "上一页按钮功能正常"
		else:
			raise NameError('error')


	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()


