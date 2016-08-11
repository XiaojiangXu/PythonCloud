# -*- coding:utf-8 -*-
from selenium import webdriver
 
driver = webdriver.Firefox()
driver.get("http://www.so.com")
assert "360搜索".decode('utf-8') in driver.title

print driver.title

driver.close()