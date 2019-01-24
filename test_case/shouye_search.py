#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time,re
import HTMLTestRunner
class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.dfs168.com"
        self.verificationErrors=[]
        self.accept_next_alert = True
    def test1_search(self):
		driver= self.driver
		driver.get(self.base_url)
		time.sleep(2)
		driver.find_element_by_id("keyword").send_keys(u"植物龙")
		driver.find_element_by_id("button").click()
		title=driver.find_element_by_xpath("html/body/div[8]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/ul/li[1]/a").text
		if title == u"植物龙":
			print "ok"
		else:
			raise NameError("error")
    def test2_search(self):
        driver=self.driver

    def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)

if __name__== '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Search("test1_search"))

    filename= r"D:\dfs168\search.html"
    fn=file(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
 	    stream= fn,
 		title= u"搜索模块测试用例",
 		description = u"用例执行情况: ")
    runner.run(testunit)




