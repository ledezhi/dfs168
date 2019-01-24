#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from login import lo 
import unittest,time,re

class Person(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.base_url = "http://www.dfs168.com"
		self.verificationErrors=[]
		self.accept_next_alert = True
		self.driver.get(self.base_url + "/member/login.html")
		lo(self.driver).login()

	def test_person1(self):
		u"""用户登录，点击用户名进入个人中心"""
		driver=self.driver
		driver.find_element_by_class_name('member-name').click()
		current_url=driver.current_url #当前页面
		title_name=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div/div[1]/ul/li[1]/a").text
		self.assertEqual(current_url,'http://www.dfs168.com/usercenter/agent/center-info')  #服务中心页面
		self.assertEqual(title_name,u"服务中心信息")
	def test_person2(self):
		u"""点击左侧导航【代购员】，进入代购员页面：填写框都为空，点击提交审核，提示：请输入您的真实姓名"""
		driver=self.driver
		driver.find_element_by_class_name('member-name').click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[1]/a").click()  #代购员链接
		current_url=driver.current_url
		self.assertEqual(current_url,'http://www.dfs168.com/usercenter/agent/rebate-apply') #代购员申请页面
		driver.find_element_by_class_name('rebate-submit').click()  #提交审核
		error=driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[1]/label").text
		self.assertEqual(error,u"请输入您的真实姓名")
	def test_person3(self):
		u"""代购员申请，输入正确用户名，其它为空，点击【提交审核】，提示：请先阅读并勾选条款"""
		driver=self.driver
		driver.find_element_by_class_name('member-name').click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[1]/a").click() #代购员链接
		driver.find_element_by_id("rebate_cardnum").send_keys(u'李德志')
		driver.find_element_by_class_name('rebate-submit').click()
		error=driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[6]/label").text  #未勾选条款
		self.assertEqual(error,u'请先阅读并勾选条款')
	def test_person4(self):
		u"""代购员代购区域自动拉取个人中心所设置地址"""
		driver=self.driver
		driver.find_element_by_class_name('member-name').click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[1]/a").click()
		area_name=driver.find_element_by_xpath("html/body/div[3]/div/div[1]/span").text  #定位所在地名称
		sell_area=driver.find_element_by_xpath(".//*[@id='rebateAddress_address_id_address_area_id']/div[3]/div").text #代购员自动拉取地址
		if area_name == sell_area:
			print u"代购员代购区域可以自动拉取用户所在地址"
		else:
			raise NameError('area error')
	def test_person5(self):
		u"""用户角色已是服务中心，用户在代购员申请页面，填写完整正确信息，提交后，提示您已是服务中心，
		点击返回上一级，链接正常"""
		driver=self.driver
		driver.find_element_by_class_name('member-name').click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[1]/a").click()
		driver.find_element_by_id('rebate_name').send_keys(u'李德志')
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[2]/span[2]/i").click()  #性别
		driver.find_element_by_id('rebate_cardnum').send_keys('460003199211182437')  #身份证
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[6]/i").click() #
		driver.find_element_by_class_name('rebate-submit').click() #提交申请
		error_tishi=driver.find_element_by_xpath("html/body/div[8]/div[1]/span").text #错误提示
		self.assertEqual(error_tishi,u"您已经是服务中心,不能再申请为代购员")

		driver.find_element_by_xpath("html/body/div[8]/div[2]/a[2]").click() #返回上一级
		current_url=driver.current_url
		self.assertEqual(current_url,"http://www.dfs168.com/usercenter/agent/rebate-apply")
  

	def test_person6(self):
		u"""用户角色已是服务中心，用户在代购员申请页面，填写完整正确信息，提交后，点击返回首页，链接正常"""
		driver=self.driver
		driver.find_element_by_class_name('member-name').click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[1]/a").click()
		driver.find_element_by_id('rebate_name').send_keys(u'李德志')
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[2]/span[2]/i").click()  #性别
		driver.find_element_by_id('rebate_cardnum').send_keys('460003199211182437')  #身份证
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[6]/i").click() #
		driver.find_element_by_class_name('rebate-submit').click() #提交申请
		driver.find_element_by_xpath("html/body/div[8]/div[2]/a[1]").click()  #返回首页
		current_url=driver.current_url 
		self.assertEqual(current_url,"http://www.dfs168.com/")

	def test_person7(self):
		u"""申请页面，点击代购区域下拉框，可选择区域名"""
		driver=self.driver
		driver.find_element_by_class_name('member-name').click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[1]/a").click() #代购员
		driver.find_element_by_id('rebate_name').send_keys(u'李德志')
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[2]/span[2]/i").click()  #性别
		driver.find_element_by_id('rebate_cardnum').send_keys('460003199211182437')  #身份证

		driver.find_element_by_xpath(".//*[@id='rebateAddress_address_id_address_area_id']/div[1]").click()
		time.sleep(2)
		driver.find_element_by_xpath(".//*[@id='rebateAddress_address_id_address_area_id']/div[1]/ul/li[4]").click() #山西
		#ActionChains(driver).move_to_element(targe1).perform()
		time.sleep(1)
		# driver.find_element_by_xpath(".//*[@id='rebateAddress_address_id_address_area_id']/div[2]/div").click()
		driver.find_element_by_xpath(".//*[@id='rebateAddress_address_id_address_area_id']/div[2]/ul/li[4]").click()  #长治
		# ActionChains(driver).move_to_element(targe2).perform()
		time.sleep(1)
		# driver.find_element_by_xpath(".//*[@id='rebateAddress_address_id_address_area_id']/div[3]/div").click()
		driver.find_element_by_xpath(".//*[@id='rebateAddress_address_id_address_area_id']/div[3]/ul/li[1]").click() #城区
		# ActionChains(driver).move_to_element(targe3).perform()
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[6]/i").click()   #单击协议
		driver.find_element_by_class_name('rebate-submit').click() #提交申请




	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


