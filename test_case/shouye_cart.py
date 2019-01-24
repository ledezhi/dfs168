#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from login import lo 
# import unittest,time,re
import HTMLTestRunner


class Cart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url = "http://www.dfs168.com"
        self.verificationErrors=[]
        self.accept_next_alert = True
        self.driver.get(self.base_url + "/member/login.html")
        lo(self.driver).login()

    def test_cart1(self):
    	u"""登录首页，购物车为空时，点击购物车按钮，正常跳转购物车首页，显示购物车为空的提示语"""
        driver= self.driver       
        time.sleep(2)
        driver.find_element_by_xpath("html/body/div[6]/div/div/div[1]/dl/dt").click()
        current_url=driver.current_url
        title=driver.find_element_by_xpath("html/body/div[7]/div/h1").text #标题：我的购物车
        tishi=driver.find_element_by_xpath("html/body/div[7]/div/div/div/div/p").text #购物车空空的哦~，去看看心仪的商品吧~
        if current_url == "http://www.dfs168.com/cart/info" and title ==u"我的购物车" and tishi== u"购物车空空的哦~，去看看心仪的商品吧~":
        	print "链接提示正常"
        else:
        	raise NameError("连接错误")
    def test_cart2(self):
    	u"""购物车为空时，在首页点击购物车按钮，购物车页面，点击【去购物】按钮，验证跳转页面中正常"""
    	driver=self.driver
    	driver.find_element_by_xpath("html/body/div[6]/div/div/div[1]/dl/dt").click() #购物车
    	driver.implicitly_wait(5)
    	driver.find_element_by_xpath("html/body/div[7]/div/div/div/div/a").click() #去购物
    	current_url = driver.current_url
    	if current_url == "http://www.dfs168.com/":
    		print "正常链接到首页"
    	else:
    		raise NameError("链接地址错误")
    def test_cart3(self):
    	u"""验证添加商品进购物车功能正常、购物车图标显示添加数量正常、总删除功能正常"""
    	driver=self.driver
    	driver.find_element_by_xpath(".//*[@id='goodsimg_2383']/div[1]/a/img").click() #商品
    	time.sleep(2)
    	driver.switch_to_window(driver.window_handles[1])
        time.sleep(1)
    	driver.find_element_by_class_name("addcart").click()
    	time.sleep(2)
    	cart_num=driver.find_element_by_xpath("html/body/div[7]/div/div/div[1]/dl/dt/span").text
    	if cart_num == "1":
    		print "添加成功！"
    		driver.find_element_by_xpath("html/body/div[7]/div/div/div[1]/dl/dt").click()  #购物车按钮
    		time.sleep(2)
    		driver.find_element_by_xpath(".//*[@id='cartForm']/dl[3]/dd[2]/span/label[2]/a").click() #总删除按钮
    		alert=driver.switch_to_alert()
    		time.sleep(2)
    		alert.dismiss()
    		driver.find_element_by_xpath(".//*[@id='cartForm']/dl[3]/dd[2]/span/label[2]/a").click() #总删除按钮
    		time.sleep(2)
    		alert=driver.switch_to_alert()
    		alert.accept()                     
    	else:
    		raise NameError("添加失败！")
    def test_cart4(self):
        u"""购物车页面，不选择商品，点击提交订单，验证弹窗提示语正常"""
        driver=self.driver
        driver.find_element_by_xpath(".//*[@id='goodsimg_2383']/div[1]/a/img").click() #点击商品进入详情页
        driver.switch_to_window(driver.window_handles[1])
        driver.implicitly_wait(3)
        driver.find_element_by_class_name("addcart").click()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("html/body/div[6]/div/div/div[1]/dl/dt").click() #购物车按钮
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='cartForm']/dl[3]/dd[1]/span").click() #全选按钮
        time.sleep(1)
        driver.find_element_by_id("next_submit").click()
        time.sleep(2)
        alert=driver.find_element_by_class_name("layui-layer-content").text
        if alert == u"请选择要结算的商品":
            print "提示正常"
        else:
            raise NameError("提示异常")

        driver.find_element_by_xpath(".//*[@id='cartForm']/dl[3]/dd[1]/span").click() 
        driver.find_element_by_xpath(".//*[@id='cartForm']/dl[3]/dd[2]/span/label[2]/a").click() #清除商品数据
        alert=driver.switch_to_alert()
        alert.accept()

    def test_cart5(self):
        u"""添加商品进购物车，并提交订单，验证可正常提交订单，跳转至支付页面"""
        driver=self.driver
        driver.find_element_by_xpath(".//*[@id='goodsimg_2383']/div[1]/a/img").click() #点击商品进入详情页
        driver.switch_to_window(driver.window_handles[1])
        driver.implicitly_wait(4)
        driver.find_element_by_class_name("addcart").click()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("html/body/div[6]/div/div/div[1]/dl/dt").click() #购物车按钮
        driver.find_element_by_id("next_submit").click()
        time.sleep(2)
        current_url=driver.current_url
        if current_url == "http://www.dfs168.com/order/preview.html":
            driver.find_element_by_id("submit_order_bt").click()
            driver.implicitly_wait(10)
            title=driver.find_element_by_xpath("html/body/div[7]/h4").text
            if title ==u"请你尽快支付，以便订单快速处理！":
                print "购物车可以提交订单并跳转支付页面"
            else:
                raise NameError("error")
        else:
            raise NameError("购物页面无法提交订单")

    def test_cart6(self):
    	driver=self.driver
        time.sleep(2)
    	driver.find_element_by_xpath(".//*[@id='goodsimg_2383']/div[1]/a/img").click() #添加第一件商品    	
    	driver.switch_to_window(driver.window_handles[1])  #切换
        time.sleep(2)
    	driver.find_element_by_class_name("addcart").click() #添加商品
        time.sleep(2)
    	driver.close()
    	driver.switch_to_window(driver.window_handles[0]) 
    	driver.find_element_by_xpath(".//*[@id='goodsimg_2472']/div[1]/a/img").click() #添加第二件商品
    	driver.switch_to_window(driver.window_handles[1])
    	driver.find_element_by_class_name("addcart").click()
        time.sleep(2)
    	driver.close()
    	driver.switch_to_window(driver.window_handles[0])
    	driver.find_element_by_xpath("html/body/div[6]/div/div/div[1]/dl/dt").click() #购物车按钮
        time.sleep(2)
        a=driver.find_element_by_id("goods_price_7196").text  #购物车a商品小计
        b=driver.find_element_by_id("goods_price_2392").text  #购物车b商品小计
        A=float(a.replace(',',''))
        B=float(b)      
        total= A + B
        carttotal=driver.find_element_by_id("cartTotal").text
        Carttotal = float(carttotal.replace(',',''))        
        if (Carttotal == total):
            print "总计金额计算正确"
        else:
            raise NameError("金额计算错误")
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='cartForm']/dl[4]/dd[2]/span/label[2]/a").click() #删除商品数据
        time.sleep(2)
        alert=driver.switch_to_alert()
        alert.accept()
     
    def tearDown(self):
    	self.driver.quit()    	
    	self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(Cart("test_cart1"))
    testunit.addTest(Cart("test_cart2"))
    testunit.addTest(Cart("test_cart3"))
    testunit.addTest(Cart("test_cart4"))
    testunit.addTest(Cart("test_cart5"))
    testunit.addTest(Cart("test_cart6"))
    filename=r'D:\dfs168\cart.html'
    fn=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fn,
        title=u"购物车测试报告",
        description=u"用例执行情况：")
    runner.run(testunit)


