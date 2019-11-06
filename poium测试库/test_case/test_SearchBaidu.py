#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/06 14:39
# @Author  : zc
# @File    : test_SearchBaidu.py

import unittest
from poium测试库.page_object.baidu_page import BaiduPage
from selenium import webdriver
import time

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "/Users/zhangc/Desktop/mine/PycharmProjects/PY项目/PyProject/project_Buger(2)/poium测试库/tools/chromedriver"
        cls.driver = webdriver.Chrome(chromedriver)
        cls.driver.get("https://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_searchBaidu(self):
        page = BaiduPage(self.driver)
        # page.search_input = "selenium"
        # page.search_button.click()
        page.search_action("selenium")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()

