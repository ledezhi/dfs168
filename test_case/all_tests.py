#coding=utf-8
import unittest
import dfs_login,shouye_dingwei
import HTMLTestRunner

testunit=unittest.TestSuite()


testunit.addTest(unittest.makeSuite(dfs_login.Denglu))
testunit.addTest(unittest.makeSuite(shouye_dingwei.Shouye))

filename = r'D:\dfs168\report.html'
fp = file(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title=u'大丰收测试报告',
	description=u'用例执行情况：')
runner.run(testunit)