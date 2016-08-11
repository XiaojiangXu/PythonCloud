# -*- coding:utf-8 -*-
'''
Created on 2016年5月6日

@author: Administrator
'''
import selenium.webdriver as webdriver
import contextlib

@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()

with quitting(webdriver.Firefox()) as driver:
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')
    driver.get_screenshot_as_file('C:\\Users\\Administrator\\Desktop\\python_cloud\\baidu.png') 