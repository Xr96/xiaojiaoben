# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 10:43
# @Author  : Fighter.Wu
from selenium import webdriver
import allure,time

class Test002:

    def setup(self):
        # 声明驱动对象
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        time.sleep(2)

    @allure.step("输入用户名")
    def input_name(self,name):
        pass

    @allure.step("输入密码")
    def input_password(self,pwd):
        pass

    @allure.step("登录步骤")
    def test_001(self):
        self.input_name("wudada")
        self.input_password("123210")
        # 添加文字到测试报告
        allure.attach("这是登录方法","标题1",allure.attachment_type.TEXT)
        # 添加截图图片到测试报告
        allure.attach(self.driver.get_screenshot_as_png(),"百度截图",allure.attachment_type.PNG)

        self.driver.quit()