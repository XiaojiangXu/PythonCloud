#-*- coding:utf-8 -*-
#引入相关包
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest,os
from selenium.webdriver.support.wait import WebDriverWait
#创建百度测试类
class baidu(unittest.TestCase):
#初始化工作
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get('http://www.baidu.com')
#创建百度搜索用例   
    def testcase_search(self):
        driver=self.driver
        kw=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id('kw'))
        su=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id('su'))
        kw.send_keys('selenium')
        su.click()
        title=WebDriverWait(driver,10).until(lambda driver:driver.title)
        self.assertEqual(title,u'selenium_百度搜索')
#结束工作
    def tearDown(self):
        self.driver.quit()

#创建测试用例集
suite=unittest.TestSuite()
suite.addTest(baidu('testcase_search'))


if __name__=='__main__':
#HTML文件路径
    filename='D:\\Project\\HtmlReport\\report1.html'
#以写模式打开文件
    fp=open(filename,'wb')
#传入HTMLTestRunner相关参数
    runner=HTMLTestRunner(stream=fp,title='TestReport',description='TestCase')
#执行用例集
    runner.run(suite)
#关闭文件操作
    fp.close()
#打开网页测试报告
    os.system(filename)