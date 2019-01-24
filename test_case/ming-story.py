#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select 

from login import lo
import unittest,time,HTMLTestRunner

class Mdstore(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.base_url = "http://www.dfs168.com/"
		self.verificationErrors=[]
		self.accept_next_alert=True
		self.driver.get(self.base_url)
		lo(self.driver).pop_login()
	def test_store1(self):
		u"网站首页，点击名店街，可正常进入名店街首页"
		driver=self.driver
		driver.find_element_by_xpath("html/body/div[6]/div/nav/div/ul/li[2]/a").click()
		time.sleep(2)
		current_url=driver.current_url
		self.assertEqual(current_url,"http://www.dfs168.com/store.html")
	def test_store2(self):
		u""
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)
if __name__ == "__main__":
	# unittest.main()
	testunit=unittest.TestSuite()
	testunit.addTest(Mdstore("test_store1"))
	filename=r"D:\dfs168\Mdjreport.html"
	fn=file(filename,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(
		stream=fn,
		title=u"名店街测试报告",
		description=u"用例执行情况：")
	runner.run(testunit)




