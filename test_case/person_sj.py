#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time
from login import lo
from mysqldb import DB

class zhanghu_sj(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.base_url='http://www.dfs168.com'
		self.verificationErrors=[]
		self.accept_next_alert=True
		self.driver.get(self.base_url)
		lo(self.driver).pop_login()
		self.driver.find_element_by_class_name("member-name").click()  #个人中心
		self.driver.find_element_by_xpath(".//*[@id='header']/div/nav/ul/li[2]/a").click()  #账户设置
	def test_sj1(self):
		u"""个人中心-账户设置，编辑头像，上传正常图片，验证可正常上传"""
		driver=self.driver
		driver.find_element_by_xpath(".//*[@id='profile_form']/dl[1]/dd/div/a").click()  #编辑头像
		driver.switch_to_frame("layui-layer-iframe1")  #切换都头像框架
		time.sleep(2)
		driver.find_element_by_xpath(".//*[@id='pic']").send_keys("D:\\test\\ldz.jpg")
		time.sleep(1)
		source=driver.find_element_by_xpath(".//*[@id='form_cut']/div/dl[1]/dd/div[3]/div[1]/div[2]/div[12]")
		targe=driver.find_element_by_xpath(".//*[@id='form_cut']/div/dl[1]/dd/div[3]/div[2]")

		ActionChains(driver).drag_and_drop(source,targe).perform()
		time.sleep(2)
		driver.find_element_by_id("ncsubmit").click()
	def test_sj2(self):
		u"""个人中心-账户设置，编辑头像，上传图片，点击取消，验证图片没上传成功"""
		driver=self.driver
		driver.find_element_by_xpath(".//*[@id='profile_form']/dl[1]/dd/div/a").click()
		driver.switch_to_frame("layui-layer-iframe1")
		time.sleep(2)
		driver.find_element_by_xpath(".//*[@id='pic']").send_keys("D:\\test\\ldz.jpg")
		time.sleep(1)
		driver.find_element_by_id("nccancle").click()
	def test_sj3(self):
		u"""个人中心-账户设置，真实姓名为空，其余信息填写完整正确，点击提交，验证错误提示“姓名不能为空”"""
		driver=self.driver
		driver.find_element_by_xpath(".//*[@id='profile_form']/dl[3]/dd/span/input").clear()
		driver.find_element_by_xpath(".//*[@id='profile_form']/dl[3]/dd/span/input").send_keys("")
		driver.find_element_by_xpath(".//*[@id='profile_form']/dl[16]/dd/input").click()  #保存修改
		time.sleep(2)
		error=driver.find_element_by_xpath(".//*[@id='profile_form']/dl[3]/dd/span/label").text
		self.assertEqual(error,u"姓名不能为空")
	def test_sj4(self):
		u"""个人中心-账户设置，验证账户名与顶层用户名一致"""
		db=DB()
		driver=self.driver
		time.sleep(2)
		name=driver.find_element_by_xpath(".//*[@id='profile_form']/dl[2]/dd/span").text
		NAME=db.getBySql_result_unique("select member_name from shopnc_member where member_phone='18620369112'")
		member_name=driver.find_element_by_class_name("member-name").text

		self.assertEqual(NAME,member_name)
		print NAME
	def test_sj5(self):
		u"""个人中心-账户设置，真实姓名为空，其余信息填写完整正确，点击提交，验证错误提示“姓名不能为空”"""
		driver=self.driver
		driver.find_element_by_xpath(".//*[@id='profile_form']/dl[3]/dd/span/input").clear()
		driver.find_element_by_xpath(".//*[@id='profile_form']/dl[3]/dd/span/input").send_keys(u"布瓜")
		driver.find_element_by_xpath(".//*[@id='profile_form']/dl[16]/dd/input").click()  #保存修改
		time.sleep(2)
		success=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div/div[1]/div[1]/span").text

		self.assertEqual(success,u"修改信息成功")





	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)



if __name__=='__main__':
	unittest.main()
