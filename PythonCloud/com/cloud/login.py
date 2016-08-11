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
        driver.switch_to_frame("menuFrame")
        driver.find_element_by_link_text(u"机构编制人员管理").click()
        driver.switch_to_default_content()
        driver.switch_to_frame("leftFrame")
        driver.find_element_by_id("treeNameSpan120000").click()
        driver.find_element_by_id("treeNameSpan120000-02").click()
        driver.find_element_by_id("treeNameSpan120000-02-10001").click()
        driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.switch_to_frame("top1Frame")
        driver.find_element_by_link_text(u"人员管理").click()
        driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.switch_to_frame("main1Frame")
        driver.find_element_by_xpath("html/body/form/table[2]/caption/div/div/strong/div/input[3]").click()
        driver.find_element_by_name("p_Gongwy_dsh_gongwy_name").clear()
        driver.find_element_by_name("p_Gongwy_dsh_gongwy_name").send_keys(u"王勇")
        driver.find_element_by_name("p_Gongwy_dsh_gongwy_sfzh").clear()
        driver.find_element_by_name("p_Gongwy_dsh_gongwy_sfzh").send_keys("130104198506020073")
        Select(driver.find_element_by_name("p_Gongwy_dsh_gongwy_xb")).select_by_visible_text(u"男")
        driver.find_element_by_css_selector("option[value=\"1\"]").click()
        
        #编制类型
        driver.find_element_by_xpath(".//*[@id='gongwydshfrm']/table[2]/tbody/tr[1]/td[2]/input[3]").click()
        driver.implicitly_wait(30)
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                driver.find_element_by_css_selector("#unitlist_txt0_2 > font.tree_item").click()
                driver.find_element_by_name("button").click()
        print now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口
        driver.implicitly_wait(30)
         
        #driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.switch_to_frame("main1Frame")
        #人员分类
        driver.find_element_by_xpath(".//*[@id='gongwydshfrm']/table[2]/tbody/tr[2]/td[1]/input[3]").click()
        #driver.find_element_by_css_selector("td.troneleft.th > input[onclick=\"choosezw('dt70','frm.p_Gongwy_dsh_gongwy_ryfl','frm.p_Gongwy_dsh_gongwy_ryfl_txt');\"]").click()
        driver.implicitly_wait(30)
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print 'first handle is',now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print 'second handle is',handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                driver.find_element_by_css_selector("#unitlist_txt0_11 > font.tree_item").click()
                #driver.find_element_by_id("status").click()
                driver.find_element_by_name("button").click()
        print 'third handle is',now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口
        driver.implicitly_wait(30)
        
        #driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.switch_to_frame("main1Frame")
        #人员状态
        driver.find_element_by_xpath(".//*[@id='gongwydshfrm']/table[2]/tbody/tr[2]/td[2]/input[3]").click()
        driver.implicitly_wait(30)
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                driver.find_element_by_css_selector("#unitlist_txt0_1 > font.tree_item").click()
                driver.find_element_by_name("button").click()
        print now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口
        driver.implicitly_wait(30)
         
        #driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.switch_to_frame("main1Frame")
        #领导职务层次
        driver.find_element_by_xpath(".//*[@id='gongwydshfrm']/table[2]/tbody/tr[4]/td[1]/input[3]").click()
        driver.implicitly_wait(30)
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                driver.find_element_by_css_selector("#unitlist_txt0_2 > font.tree_item").click()
                driver.find_element_by_name("button").click()
        print now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口
        driver.implicitly_wait(30)
         
        #driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.switch_to_frame("main1Frame")
        #非领导职务
        driver.find_element_by_xpath(".//*[@id='gongwydshfrm']/table[2]/tbody/tr[4]/td[2]/input[3]").click()
        driver.implicitly_wait(30)
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                driver.find_element_by_css_selector("#unitlist_txt0_2 > font.tree_item").click()
                driver.find_element_by_name("button").click()
        print now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口
        driver.implicitly_wait(30)
         
        #driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.switch_to_frame("main1Frame")
        #进入本单位形式
        driver.find_element_by_xpath(".//*[@id='gongwydshfrm']/table[2]/tbody/tr[6]/td[1]/input[3]").click()
        driver.implicitly_wait(30)
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                driver.find_element_by_css_selector("#unitlist_txt0_2 > font.tree_item").click()
                driver.find_element_by_name("button").click()
        print now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口
        driver.implicitly_wait(30)
         
        #driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.switch_to_frame("main1Frame")
        #政府机构人员分类
        driver.find_element_by_xpath(".//*[@id='gongwydshfrm']/table[2]/tbody/tr[8]/td[2]/input[3]").click()
        driver.implicitly_wait(30)
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                driver.find_element_by_css_selector("#unitlist_txt0_2 > font.tree_item").click()
                driver.find_element_by_name("button").click()
        print now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口
        driver.implicitly_wait(30)
              
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                driver.find_element_by_xpath(".//*[@id='gongwydshfrm']/table[3]/tfoot/tr/td/input[1]").click()
                #driver.find_element_by_css_selector(".formtable>tfoot>tr>td > input[onclick =\"doSave();\" ]").click()
        print now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口        
        driver.implicitly_wait(30)
        
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print 'fourth handle is',now_handle   #输出当前获取的窗口句柄
        all_handles = driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print 'fifth handle is', handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                self.assertEqual(u"数据项[人员分类]不能为空，请填写！", self.close_alert_and_get_its_text())
                #self.assertEqual(u"新增人员成功", self.close_alert_and_get_its_text())
                driver.find_element_by_xpath("//*[@id='btnOk']").click()      
        print 'sixth handle is',now_handle   #输出主窗口句柄
        driver.switch_to_window(now_handle) #返回主窗口
        
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
