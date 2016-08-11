# -*- coding:utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.60.252:8080"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/login.do")
        driver.find_element_by_id("j_username").clear()
        driver.find_element_by_id("j_username").send_keys("zy")
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("tfkj-123456")
        driver.find_element_by_name("submit1").click()
        driver.implicitly_wait(30)
        #driver.get_screenshot_as_file('D:\\workspace\\PythonCloud\\com\\cloudlogin.png')
        driver.get_screenshot_as_file('C:\\Users\\Administrator\\Desktop\\python_cloud\\cloudlogin.png')
        
    #对弹窗异常的处理
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    #关闭警告和对得到文本框的处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
#unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == "__main__":
    unittest.main()
