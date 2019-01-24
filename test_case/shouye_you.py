#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import unittest,time,re
import HTMLTestRunner

class Shouye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.dfs168.com"
        self.verificationErrors=[]
        self.accept_next_alert = True

    def test8_ditu1_1(self):
        u"""鼠标移动至网站地图，点击地图下的名店街，可以跳转名店街页面"""
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        targe = driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl/dt") #网站地图元素
        
        ActionChains(driver).move_to_element(targe).perform()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[1]/a[1]").click() #名店街
        time.sleep(2)
        current_url=driver.current_url
        if current_url == "http://www.dfs168.com/store.html":
            print "url is ok"
        else:
            raise NameError("url error")

        
    # def test9_ditu1_2(self):
    #     u'''鼠标移动至网站地图，点击地图下的丰收金融，可以跳转丰收金融页面'''
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     time.sleep(2)
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[1]/a[2]").click() #丰收金融
    #     time.sleep(2)
    #     current_url=driver.current_url
    #     if current_url == "http://www.dfs168.com/finance.html":
    #         print "url is ok"
    #     else:
    #         raise  NameError("url error")

    def test10_ditu1_3(self):
        u"""鼠标移动至网站地图，点击地图下的兑换中心，可以跳转兑换中心页面"""
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
        ActionChains(driver).move_to_element(targe).perform()
        driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[1]/a[2]").click() #兑换中心
        time.sleep(2)
        current_url=driver.current_url
        if current_url =="http://www.dfs168.com/exchange.html":
            print "url is ok"
        else:
            raise NameError("url error")

    # def test11_ditu1_4(self):
    #     u'''鼠标移动至网站地图，点击地图下的关于大丰收，可以跳转关于大丰收页面'''
    #     driver = self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[1]/a[4]").click() #关于大丰收
    #     time.sleep(2)
    #     current_url=driver.current_url
    #     if current_url == "http://www.dfs168.com/about.html":
    #         print "url is ok"
    #     else:
    #         raise NameError("url error")
    # def test12_ditu1_5(self):
    #     u'''鼠标移动至网站地图，点击地图下的农技中心，可以跳转农技中心页面'''
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[1]/a[5]").click() #农技中心
    #     time.sleep(2)
    #     current_url= driver.current_url
    #     if current_url == "http://www.dfs168.com/agricultural.html":
    #         print "url is ok"
    #     else:
    #         raise NameError("url error")
    # def test13_ditu2_1(self):
    #     u'''鼠标移动至网站地图，点击地图下的复合肥，可以跳转复合肥页面'''
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[2]/a[1]").click() #复合肥
    #     time.sleep(2)
    #     current_url= driver.current_url
    #     if current_url == "http://www.dfs168.com/goods/category-2383-20.html":
    #         print "url is ok"
    #     else:
    #         raise NameError("url error")
    # def test14_ditu2_2(self):
    #     u'''鼠标移动至网站地图，点击地图下的微生物肥，可以跳转微生物肥页面'''
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[2]/a[2]").click() #微生物肥
    #     time.sleep(2)
    #     current_url= driver.current_url
    #     if current_url == "http://www.dfs168.com/goods/category-2445-20.html":
    #         print "url is ok"
    #     else:
    #         raise NameError("url error")
    # def test15_ditu2_3(self):
    #     u"""鼠标移动至网站地图，点击地图下的有机肥肥，可以跳转有机肥页面"""
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[2]/a[3]").click() #有机肥
    #     time.sleep(2)
    #     current_url= driver.current_url
    #     if current_url == "http://www.dfs168.com/goods/category-2432-20.html":
    #         print "url is ok"
    #     else:
    #         raise NameError("url error")
    # def test16_ditu2_4(self):
    #     u"""鼠标移动至网站地图，点击地图下的微量元素肥，可以跳转微量元素页面"""
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[2]/a[4]").click() #微量元素肥
    #     time.sleep(2)
    #     current_url= driver.current_url
    #     if current_url == "http://www.dfs168.com/goods/category-2442-20.html":
    #         print "url is ok"
    #     else:
    #         raise NameError("url error")
    # def test17_ditu2_5(self):
    #     u"""鼠标移动至网站地图，点击地图下的水溶肥，可以跳转水溶肥页面"""
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[2]/a[5]").click() #水溶肥
    #     time.sleep(2)
    #     current_url= driver.current_url
    #     if current_url == "http://www.dfs168.com/goods/category-2423-20.html":
    #         print "url is ok"
    #     else:
    #         raise NameError("url error")
    # def test18_ditu2_6(self):
    #     u"""鼠标移动至网站地图，点击地图下氮肥，可以跳转氮肥页面"""
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(self.base_url)
    #     targe=driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dt")
    #     ActionChains(driver).move_to_element(targe).perform()
    #     driver.find_element_by_xpath("html/body/div[3]/div/div[2]/dl[1]/dd/div[2]/a[6]").click() #氮肥
    #     time.sleep(2)
    #     current_url= driver.current_url
    #     if current_url == "http://www.dfs168.com/goods/category-2392-20.html":
    #         print "url is ok"
    #     else:
    #         raise NameError("url error")
                     
    def tearDown(self):     
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__== '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Shouye("test8_ditu1_1"))
    # testunit.addTest(Shouye("test9_ditu1_2"))
    testunit.addTest(Shouye("test10_ditu1_3"))
    # testunit.addTest(Shouye("test11_ditu1_4"))
    # testunit.addTest(Shouye("test12_ditu1_5"))
    # testunit.addTest(Shouye("test13_ditu2_1"))
    # testunit.addTest(Shouye("test14_ditu2_2"))
    # testunit.addTest(Shouye("test15_ditu2_3"))
    # testunit.addTest(Shouye("test16_ditu2_4"))
    # testunit.addTest(Shouye("test17_ditu2_5"))
    # testunit.addTest(Shouye("test18_ditu2_6"))
    filename = r"D:\dfs168\report.html"
    fn = file(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fn,
        title = u"首页测试报告",
        description = u"用例执行情况：")
    runner.run(testunit)


