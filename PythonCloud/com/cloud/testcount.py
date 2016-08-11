# -*- coding:utf-8 -*-
from calculator import count
from HTMLTestRunner import HTMLTestRunner
import unittest,os


class testcount(unittest.TestCase):
    
    def setUp(self):
        print("test start")
        
    def test_add(self):
        j=count(6,3)
        self.assertEqual(j.add(),9)
        
    def test_subtract(self):
        j=count(6,3)
        self.assertEqual(j.subtract(),3)
        
    def test_multiply(self):
        j=count(6,3)
        self.assertEqual(j.multiply(),18)
        
    def test_divide(self):
        j=count(6,3)
        self.assertEqual(j.divide(),2)
    def tearDown(self):
        print("test end")

suite=unittest.TestSuite()
suite.addTest(testcount('test_add'))
suite.addTest(testcount('test_subtract'))
suite.addTest(testcount('test_multiply'))
suite.addTest(testcount('test_divide'))
        
if __name__=='__main__':
#HTML文件路径
    filename='D:\\Project\\HtmlReport\\report3.html'
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