#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from login import lo
import unittest,time,re
class Service(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.base_url="http://www.dfs168.com"
		self.verificationError=[]
		self.accept_next_alert=True
		self.driver.get(self.base_url + "/member/login.html")

	def test_service1(self):
		u"""用户登录，进入个人中心，点击服务站，进入申请页面，申请内容为空，点击提交按钮，验证错误提示正确"""
		driver=self.driver
		lo(driver).login()
		driver.find_element_by_class_name("member-name").click()
		driver.find_element_by_xpath(".//*[@id='header']/div/nav/ul/li[4]/a").click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[2]/a").click() #服务站申请页面
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[1]/div").click() #点击地址
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[1]/ul/li[14]").click() #江西
		time.sleep(4)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[2]/ul/li[7]").click()  #赣州
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[3]/ul/li[2]").click() #于都县
		time.sleep(1)
		driver.find_element_by_class_name("rebate-submit").click() #提交申请按钮
		time.sleep(2)
		error1=driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[1]/label").text
		self.assertEqual(error1,u"请输入服务站名称")
		error2=driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[2]/label").text
		self.assertEqual(error2,u"请输入您的真实姓名")
		error3=driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[3]/label").text
		self.assertEqual(error3,u"身份证号码不能为空")
		error4=driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[5]/label").text
		self.assertEqual(error4,u"请输入详细的地址")
		error5=driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[7]/label").text
		self.assertEqual(error5,u"请先阅读并勾选条款")

	def test_service2(self):
		u"""服务站申请页面，用户填写所在地区没有经销商，其它信息填写正确，点击提交按钮，验证弹窗提示：该地区没有经销商"""
		driver=self.driver
		lo(driver).login1()
		driver.find_element_by_class_name("member-name").click()
		driver.find_element_by_xpath(".//*[@id='header']/div/nav/ul/li[4]/a").click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[2]/a").click() #服务站申请页面
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[1]/div").click() #点击地址
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[1]/ul/li[1]").click() #北京
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[2]/ul/li").click() #北京市
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[3]/ul/li[2]").click() #西城区
		time.sleep(1)
		driver.find_element_by_class_name("rebate-submit").click() #提交申请按钮
		time.sleep(2)
		driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a").click()

		
	def test_service3(self):
		u"""用户已申请过服务中心，用户代购员申请页面，用户填写完整正确申请信息，点击提交申请按钮，验证提示不能申请服务站"""
		driver=self.driver
		lo(driver).login()
		driver.find_element_by_class_name("member-name").click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[2]/a").click() #服务站申请页面
		driver.find_element_by_id("service_name").send_keys(u"大丰收服务站") #服务站名称
		driver.find_element_by_id("true_name").send_keys(u"李德志") #真是姓名
		driver.find_element_by_id("service_cardnum").send_keys("460003199211182437") #身份证
		driver.find_element_by_id("service_addr").send_keys(u"二屯")
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[6]/ul/li/i").click()
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[7]/i").click()
		driver.find_element_by_class_name("rebate-submit").click() #提交申请按钮
		error=driver.find_element_by_xpath("html/body/div[8]/div[1]/span").text #错误提示
		time.sleep(1)
		self.assertEqual(error,u"您已经是服务中心,不能再申请为服务站")
	def test_service4(self):
		u"""服务站申请页面，用户名填写英文名，错误提示：姓名必须为汉字"""
		driver=self.driver
		lo(driver).login()
		driver.find_element_by_class_name("member-name").click()
		driver.find_element_by_xpath(".//*[@id='header']/div/nav/ul/li[4]/a").click() #服务中心
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[2]/a").click() #服务站申请页面
		driver.find_element_by_id("service_name").send_keys(u"大丰收服务站") #服务站名称
		driver.find_element_by_id("true_name").send_keys("leon") #真是姓名
		driver.find_element_by_id("service_cardnum").send_keys("460003199211182437") #身份证
		driver.find_element_by_id("service_addr").send_keys(u"二屯")
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[6]/ul/li/i").click()
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[7]/i").click()
		driver.find_element_by_class_name("rebate-submit").click() #提交申请按钮
		error=driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[2]/label").text #错误提示
		time.sleep(1)
		self.assertEqual(error,u"姓名必须为汉字")
	def test_service5(self):
		u"""服务站申请页面，填写完整正确的信息，提交申请信息，验证提交成功"""
		driver=self.driver
		lo(driver).login1()
		driver.find_element_by_class_name("member-name").click()
		driver.find_element_by_xpath(".//*[@id='header']/div/nav/ul/li[4]/a").click()
		driver.find_element_by_xpath(".//*[@id='container']/div/div[1]/div/ul/li[2]/a").click() #服务站申请页面
		time.sleep(1)
		driver.find_element_by_id("service_name").send_keys(u"大丰收服务站") #服务站名称
	 	driver.find_element_by_id("true_name").send_keys(u"李德志") #真是姓名
	 	driver.find_element_by_id("service_cardnum").send_keys("460003199211182437") #身份证
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[1]/div").click() #点击地址
		time.sleep(1)
		driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[1]/ul/li[14]").click() #江西
	 	time.sleep(1)
	 	driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[2]/div").click()  #赣州市
	 	time.sleep(1)
	 	driver.find_element_by_xpath(".//*[@id='_address_id_address_area_id']/div[3]/div").click() # 会昌县
		time.sleep(2)
		driver.find_element_by_id("service_addr").send_keys(u"建安先地方")
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[6]/ul/li/i").click() #选择店铺
		time.sleep(2)
		driver.find_element_by_xpath(".//*[@id='dgapply_form']/div/div[7]/i").click() #协议勾选
		driver.find_element_by_class_name("rebate-submit").click() #提交申请按钮
		time.sleep(1)
		targe_title=driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/div/div/div[2]/div[1]/div[1]/p[1]").text
		self.assertEqual(targe_title,u"您的资料已成功提交")

		#清理测试数据
		

		
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationError)
if __name__=="__main__":
	unittest.main()




