#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import unittest,time,re
import HTMLTestRunner

class Denglu(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "http://www.dfs168.com"
        self.verificationErrors = []
        self.accept_next_alert =True

    # 正常登录
    def test1_denglu(self):
        u"""正常登录"""
        driver = self.driver
        driver.get(self.base_url + "/member/login.html")
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("18620369112")
        driver.find_element_by_id("password").send_keys("1234567")
        driver.find_element_by_id("normal-login").click()
        time.sleep(2)
        now_name = driver.find_element_by_class_name("member-name").text
        if now_name == "18620369112":
            print "登录成功！"
        else:
            raise NameError("member name error!")

        driver.find_element_by_link_text("退出").click()
        driver.close()
    #异常登录
    def test2_denglu(self):
        u"""用户名及密码为空，点击登录"""
        driver = self.driver
        driver.get(self.base_url + "/member/login.html")
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("")
        driver.find_element_by_id("password").send_keys("")
        driver.find_element_by_id("normal-login").click()
        time.sleep(2)
        tishi_error = driver.find_element_by_xpath("html/body/div[7]/div/div[2]/div/div/div[1]/div[1]/label").text
        time.sleep(2)

        if tishi_error == u"用户名不能为空":
            print "错误提示正常"
        else:
            raise NameError('tishi name error!')
    def test3_denglu(self):
        u"""用户名正常，密码为空，点击登录"""
        driver = self.driver
        driver.get(self.base_url + "/member/login.html")
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("18620369112") 
        driver.find_element_by_id("password").send_keys("")
        driver.find_element_by_id("normal-login").click()
        time.sleep(1)
        tishi_error = driver.find_element_by_xpath("html/body/div[7]/div/div[2]/div/div/div[1]/div[1]/label").text
        time.sleep(2) 
        if tishi_error == u"密码不能为空":
            print "错误提示正常"
        else:
            raise NameError('tishi name error!')
    def test4_denglu(self):
        u"""用户名为空，密码正确，点击登录"""
        driver = self.driver
        driver.get(self.base_url + "/member/login.html")
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("")
        driver.find_element_by_id("password").send_keys("1234567")
        driver.find_element_by_id("normal-login").click()
        time.sleep(2)
        tishi_error = driver.find_element_by_xpath("html/body/div[7]/div/div[2]/div/div/div[1]/div[1]/label").text

        if tishi_error == u"用户名不能为空":
            print "错误提示正常"
        else:
            raise NameError('tishi name error!')
    def test5_denglu(self):
        u"""用户名错误，密码正确，点击登录"""
        driver = self.driver
        driver.get(self.base_url + "/member/login.html")
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("18620369110")
        driver.find_element_by_id("password").send_keys("1234567")
        driver.find_element_by_id("normal-login").click()
        time.sleep(2)
        tishi_error = driver.find_element_by_xpath("html/body/div[7]/div/div[2]/div/div/div[1]/div[1]/label").text

        if tishi_error == u"用户名或密码错误":
            print "错误提示正常"
        else:
            raise NameError("tishi name error!")
    def test6_denglu(self):
        u"""用户名正确，密码错误，点击登录"""
        driver = self.driver
        driver.get(self.base_url + "/member/login.html")
        driver.find_element_by_id("user_name").send_keys("18620369112")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("normal-login").click()
        time.sleep(2)
        tishi_error = driver.find_element_by_xpath("html/body/div[7]/div/div[2]/div/div/div[1]/div[1]/label").text

        if tishi_error == u"用户名或密码错误":
            print "错误提示正确"
        else:
            raise NameError("tishi name error!")




    def tearDown(self):     
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__=="__main__":
    testunit=unittest.TestSuite()

    testunit.addTest(Denglu("test1_denglu")) 
    testunit.addTest(Denglu("test2_denglu"))
    testunit.addTest(Denglu("test3_denglu"))
    testunit.addTest(Denglu("test4_denglu"))
    testunit.addTest(Denglu("test5_denglu"))
    testunit.addTest(Denglu("test6_denglu"))

    filename = r"D:\dfs168\loginrep.html"
    fn = file(filename,'wb')

    runner= HTMLTestRunner.HTMLTestRunner(
        stream = fn,
        title=u'登录模块测试报告',
        description=u'用例执行情况：')
    runner.run(testunit)
        
