#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 13:49
# @Author  : zc
# @File    : my_test.py

import unittest
from Appium_project.common.app_config import des_caps


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("=======开始启动appium服务=======")


    def setUp(self):
        self.driver = des_caps()
        print("=======运行测试用例=======")


    def tearDown(self):
        print("=======测试用例结束=======")
        self.driver.close_app()
        pass



    @classmethod
    def tearDownClass(cls):
        print("=======已经结束=======")