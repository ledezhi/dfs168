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
       
    def test1_dingwei(self):
        u"""用户正常登录进入网站，所在地定位是否正常"""
        driver = self.driver 
        driver.get(self.base_url + "/member/login.html")
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("18620369112")
        driver.find_element_by_id("password").send_keys("1234567")
        driver.find_element_by_id("normal-login").click()
        time.sleep(2)       
        now_name = driver.find_element_by_class_name("address-cur").text
        if now_name == u"东湖区":
            print "定位成功！"
        else:
            raise NameError("member name error!")
    # def test2_shoucang(self):
    #     u"""点击首页顶部的收藏大丰收，弹窗提示收藏操作"""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     time.sleep(3)
    #     driver.find_elemnet_by_xpath(".//*[@id='collect']").click()
        # now_name=driver.find_element_by_class_name("layui-layer-title").text
        # if now_name ==u"大丰收168温馨提醒":
        #     print "弹窗正常"
        # else:
        #     raise NameError("name error")
        # driver.find_element_by_class_name("layui-layer-btn0").click()
    def test3_wugu(self):
        u"""点击【五谷官网】,正常跳转五谷科技首页——>点击【服务-农业一站式解决方案】，跳转正常"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
        driver.switch_to_window(driver.window_handles[1])
        targe=driver.find_element_by_xpath("html/body/div[1]/ul/li[1]/a")
        ActionChains(driver).move_to_element(targe).perform()
        driver.find_element_by_xpath("html/body/div[1]/ul/li[1]/div/a[1]").click()
        time.sleep(2)
        title=driver.find_element_by_xpath("html/body/div[2]/div[1]/div[2]/h2").text
        if title ==u"农业一站式解决方案":
            print "跳转正常"
        else:
            raise NameError("链接错误")
    def test4_wugu(self):
        u"""点击【五谷官网】,正常跳转五谷科技首页——>点击【服务-私人订制】，跳转正常"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(2)
        targe=driver.find_element_by_xpath("html/body/div[1]/ul/li[1]/a")
        ActionChains(driver).move_to_element(targe).perform()
        time.sleep(2)
        driver.find_element_by_xpath("html/body/div[1]/ul/li[1]/div/a[2]").click()
        time.sleep(2)
        title2=driver.find_element_by_xpath("html/body/div[2]/div[1]/div[2]/h2").text
        if title2 ==u"私人订制高端饮食":
            print "跳转正常"
        else:
            raise NameError("链接错误")
    def test5_wugu(self):
        u"""点击【五谷官网】,正常跳转五谷科技首页——>点击【产品】，跳转正常"""
        driver =self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_xpath("html/body/div[1]/ul/li[2]/a").click()
        time.sleep(2)
        title_name=driver.find_element_by_xpath("html/body/div[2]/div[1]/div[2]/h2").text
        if title_name == u"农资电商平台":
            print "跳转正常"
        else:
            raise NameError("链接错误！")

    def test6_wugu(self):
        u"""点击【五谷官网】,正常跳转五谷科技首页——>点击【洞见】，跳转正常"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_xpath("html/body/div[1]/ul/li[3]/a").click()
        time.sleep(2)
        title_name=driver.find_element_by_xpath("html/body/div[2]/div[1]/div[2]/h2").text
        time.sleep(3)
        if title_name == u"洞见":
            print "跳转正常"
        else:
            raise NameError("title name error")

    def test7_wugu(self):
        u"""点击【五谷官网】,正常跳转五谷科技首页——>点击【公益—五谷公益介绍】，跳转正常"""
        driver=self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
        driver.switch_to_window(driver.window_handles[1])
        targer=driver.find_element_by_xpath("html/body/div[1]/ul/li[4]/a")
        ActionChains(driver).move_to_element(targer).perform()
        driver.find_element_by_xpath("html/body/div[1]/ul/li[4]/div/a[1]").click()
        time.sleep(2)
        title=driver.find_element_by_xpath("html/body/div[2]/div[1]/div[2]/h2").text
        if title == u"公益":
            print "跳转正常"
        else:
            raise NameError("链接错误")
    def test8_wugu(self):
        u"""点击【五谷官网】,正常跳转五谷科技首页——>点击【公益—江池镇小学项目】，跳转正常"""
        driver=self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
        driver.switch_to_window(driver.winow_handles[1])
        targe=driver.find_element_by_xpath("html/body/div[1]/ul/li[4]/a")
        ActionChains(driver).move_to_element(targe).perform()
        driver.find_element_by_xpath("html/body/div[1]/ul/li[4]/div/a[2]").click()
        time.sleep(2)
        current_url=driver.current_url
        if current_url == "http://www.wego-group.com/index.php?m=home&c=welfare&a=jiangchi":
            print "跳转正常"
        else:
            raise NameError("链接错误")

        

    def test9_wugu(self):
        u"""点击【五谷官网】,正常跳转五谷科技首页——>点击【合作】，跳转正常"""
        driver =self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("html/body/div[3]/div/a[2]").click()
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_xpath("html/body/div[1]/ul/li[5]/a").click()
        time.sleep(2)
        title_name=driver.find_element_by_xpath("html/body/div[2]/div[1]/div[2]/h2").text
        time.sleep(2)
        if title_name == u"战略合作":
            print "跳转正常"
        else:
            raise NameError("链接错误！")
    def test10_wugu(self):
        u"""点击【五谷官网】,正常跳转五谷科技首页——>点击【合作】-【商城】，跳转正常"""
        driver =self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("html/body/div[3]/div/a[2]").click() #点击五谷官网
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_xpath("html/body/div[1]/ul/li[5]/a").click() #合作
        driver.find_element_by_xpath("html/body/div[1]/ul/li[6]/a").click() #商城
        driver.switch_to_window(driver.window_handles[2])
        time.sleep(2)
        title_name = driver.find_element_by_xpath("html/body/div[3]/div/div[3]/span").text
        time.sleep(2)
        if title_name == u"欢迎光临大丰收农资商城！":
            print "跳转正常"
        else:
            raise NameError("链接错误！")
    
                     
    def tearDown(self):     
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__== '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Shouye("test_search1"))
    # testunit.addTest(Shouye("test1_dingwei"))
    # testunit.addTest(Shouye("test2_shoucang"))
    # testunit.addTest(Shouye("test3_wugu"))
    # testunit.addTest(Shouye("test4_wugu"))
    # testunit.addTest(Shouye("test5_wugu"))
    # testunit.addTest(Shouye("test6_wugu"))
    # testunit.addTest(Shouye("test7_wugu"))
    # testunit.addTest(Shouye("test8_wugu"))
    # testunit.addTest(Shouye("test9_wugu"))
    # testunit.addTest(Shouye("test10_wugu"))
    filename = r"D:\dfs168\report.html"
    fn = file(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fn,
        title = u"首页测试报告",
        description = u"用例执行情况：")
    runner.run(testunit)



