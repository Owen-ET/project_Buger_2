#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/05 11:48
# @Author  : zc
# @File    : test_baidu_ddt.py


import unittest
from time import sleep
from selenium import webdriver
from poium import Page,PageElement
from ddt import ddt,data,file_data,unpack
from selenium.webdriver.common.by import By



@ddt
class TestBaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "/Users/zhangc/Desktop/mine/PycharmProjects/PY项目/PyProject/project_Buger(2)/tools/chromedriver"
        cls.driver = webdriver.Chrome(chromedriver)
        cls.url = "https://baidu.com"


    def baidu_search(self,keys):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys(keys)
        self.driver.find_element(By.CSS_SELECTOR,"#su").click()


        # poium库

        sleep(5)


    # # 参数化例1
    # @data(["case1","selenium3"],["case2","python3"],["case3","百度"])
    # @unpack
    # # @unittest.skip
    # def test_baiduSearch01(self,case,data_key):
    #     print("第一组测试用例："+case)
    #     self.baidu_search(data_key)
    #     self.assertEqual(self.driver.title,data_key + "_百度搜索",msg="标题不正确！")
    #
    #
    #
    #
    # # 参数化例2:json
    # @file_data("../data/ddt_data_file.data")
    # def test_baiduSearch02(self,keys):
    #     print("第二组测试用例：",keys)
    #     self.baidu_search(keys)
    #     self.assertEqual(self.driver.title, keys + "_百度搜索", msg="标题不正确！")


    # 参数化例3:yaml
    @file_data("../data/ddt_data_file.yaml")
    @unpack
    def test_baiduSearch03(self,**kwargs):
        keys = kwargs['data1'][1]['keys']
        print("第三组测试用例：",keys)
        self.baidu_search(keys)
        self.assertEqual(self.driver.title, keys + "_百度搜索", msg="标题不正确！")


    @classmethod
    def tearDownClass(cls):
        print("用例结束！")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)