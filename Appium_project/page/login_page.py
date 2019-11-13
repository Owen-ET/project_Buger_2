#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 14:03
# @Author  : zc
# @File    : login_page.py

from Appium_project.page.base_page import AppPage
from selenium.webdriver.common.by import By
from time import sleep


class LoginHR(AppPage):


    # 元素定位
    username_loc = (By.ID,"com.csksc2b.invertory:id/edt_name_phone")
    password_loc = (By.ID,"com.csksc2b.invertory:id/edt_pass")
    button_loc = (By.ID,"com.csksc2b.invertory:id/tv_login")
    # toast信息
    # toast_loc = (By.XPATH,"//*[contains(@text,'用户名或密码错误')]")
    toast_loc = (By.XPATH,"//*[@text='用户名或密码错误']")



    def input_username(self,text):
        '''app输入用户名'''
        self.send_keys(self.username_loc,text)


    def input_password(self,text):
        '''app输入密码'''
        self.send_keys(self.password_loc,text)


    def click_button(self):
        '''点击app登录按钮'''
        self.click(self.button_loc)


    def getToast(self):
        '''获取appToast信息'''
        return self.getText(self.toast_loc)


    def login_action(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_button()



# if __name__ == '__main__':
#     LoginHR().login_action(
#         username= "13642040631",
#         password= "886001"
#     )