#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 17:38
# @Author  : zc
# @File    : test_login.py


from Appium_project.page.login_page import LoginHR
from Appium_project.common.my_test import MyTest
from ddt import ddt,data,file_data,unpack
import unittest



@ddt
class TestLogin(MyTest):



    @file_data("../data/ddt_data_file.yaml")
    @unpack
    def test_login01(self):
        '''测试用例01：验证登录失败信息'''
        LoginHR(self.driver).login_action(
            username="13642040631",
            password="886001"
        )

        po = LoginHR(self.driver).getToast()
        self.assertEqual(po,"用户名或密码错误")


if __name__ == '__main__':
    unittest.main()