#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select 
from login import lo
import unittest,time,re


class person_mj(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.base_url="http://.www.dfs168.com"
		self.verficationError=[]
		self.accept_next_alert=True
		self.driver.get(self.base_url)
		lo(self.driver).pop_login()
		self.driver.find_element_by_class_name("member-name").click() #个人中心
		self.driver.find_element_by_xpath(".//*[@id='header']/div/nav/ul/li[1]/a").click()  #买家首页

	# def test_mj1(self):
	# 	driver=self.driver
	# 	time.sleep(2)
	# 	member_name=driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/dl/dd[2]/ul/li[1]/a").text
	# 	pack_price=driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/dl/dd[2]/ul/li[3]/span").text
	# 	self.assertEqual(member_name,'18620369112')  #用户名称
	# 	self.assertEqual(pack_price,'4212.04')  #用户钱包
	# def test_mj2(self):
	# 	u"""个人中心-买家首页，左侧导航点击【我的购物车】，验证正常跳转购物车页面"""
	# 	driver=self.driver 
	# 	time.sleep(2)
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/div[1]/a").click()  #购物车链接
	# 	current_url=driver.current_url
	# 	self.assertEqual(current_url,"http://www.dfs168.com/cart/info.html") #购物车页面
	# def test_mj3(self):
	# 	u"""个人中心-买家首页，左侧导航点击【已买到商品】，链接正常"""
	# 	driver=self.driver
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/div[2]/a").click() #已买到商品
	# 	current_url=driver.current_url
	# 	self.assertEqual(current_url,"http://www.dfs168.com/usercenter/profile/index?orderState=40") 

	# def test_mj4(self):
	# 	u"""个人中心-买家首页，左侧导航点击【丰收币明细】，链接正常"""
	# 	driver=self.driver
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dt/a").click()  #我的丰收币
	# 	time.sleep(1)
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dd[1]/a").click()  #丰收币明细
	# 	time.sleep(2)
	# 	current_url=driver.current_url
	# 	self.assertEqual(current_url,"http://www.dfs168.com/usercenter/profile/member-points")

	# def test_mj5(self):
	# 	u"""个人中心-买家首页，左侧导航点击【丰收币明细】，验证丰收币明细中丰收币总数与个人中心的丰收币数量一致"""
	# 	driver=self.driver
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dt/a").click()  #我的丰收币
	# 	time.sleep(1)
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dd[1]/a").click()  #丰收币明细
	# 	point1=driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/dl/dd[2]/ul/li[2]").text
	# 	a=list(point1)[4:]

	# 	point2=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[1]").text #丰收币明细丰收币总数
	# 	b=list(point2)[6:]

	# 	self.assertEqual(a,b)

	def test_mj6(self):
		u"""个人中心-买家首页，丰收币明细，操作选择抽奖，点击搜索，验证只能搜索到抽奖获得的丰收币"""
		driver=self.driver
		driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dt/a").click()  #我的丰收币
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dd[1]/a").click()  #丰收币明细
		driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/form/table/tbody/tr/td[1]/div/select").click()
		time.sleep(2)
		driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/form/table/tbody/tr/td[1]/div/select/option[2]").click() #抽奖
		time.sleep(2)
		driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/form/table/tbody/tr/td[4]/input").click() #搜索
		time.sleep(1)	
		caozuo1=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]").text
		caozuo2=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]").text
		caozuo3=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]").text
		print caozuo1,caozuo2,caozuo3

		if caozuo1==caozuo2==caozuo3==u"抽奖":
			print '搜索结果正确！'
		else:
			raise NameError('error')
	# def test_mj7(self):

	# 	u"""个人中心-买家首页，丰收币明细，添加时间，验证搜索到添加时间段获取的的丰收币"""
	# 	driver=self.driver
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dt/a").click()  #我的丰收币
	# 	time.sleep(1)
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dd[1]/a").click()  #丰收币明细
	# 	driver.find_element_by_id("stime").click()
	# 	time.sleep(1)
	# 	driver.find_element_by_xpath(".//*[@id='laydate_table']/tbody/tr[4]/td[3]").click() #20号
	# 	driver.find_element_by_id("etime").click()
	# 	time.sleep(1)
	# 	driver.find_element_by_xpath(".//*[@id='laydate_table']/tbody/tr[4]/td[7]").click() #24号
	# 	time.sleep(1)
	# 	driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/form/table/tbody/tr/td[4]/input").click()  #搜索
	# 	time.sleep(2)
	# 	# time1=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[1]").text  #20
	# 	# self.assertEqual(time1,"2016-12-20")
	# 	time2=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[1]").text  #22 号

	# 	self.assertEqual(time2,"2016-12-22")
	# def test_mj8(self):
	# 	u""""""
	# 	driver=self.driver





		
			

		



	# def test_mj5(self):
	# 	u"""个人中心-买家首页，左侧导航点击【兑换的商品列表】，链接正常"""
	# 	driver=self.driver
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dt/a").click()
	# 	time.sleep(1)
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/dl/dd[2]/a").click() #兑换的商品列表
	# 	time.sleep(2)
	# 	current_url=driver.current_url
	# 	self.assertEqual(current_url,"http://www.dfs168.com/usercenter/profile/member-points-order")
	# def test_mj6(self):
	# 	u"""个人中心-买家首页，左侧导航点击【我的代金卷】，链接正常"""
	# 	driver=self.driver
	# 	driver.find_element_by_xpath(".//*[@id='my_menu']/div[3]/a").click()  #点击我的代金卷
	# 	time.sleep(1)
	# 	current_url=driver.current_url
	# 	self.assertEqual(current_url,"http://www.dfs168.com/usercenter/profile/voucher-list")
		






	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verficationError)

if __name__=='__main__':
	unittest.main()

