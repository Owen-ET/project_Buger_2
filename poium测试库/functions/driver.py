#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/06 15:32
# @Author  : zc
# @File    : driver.py

from selenium import webdriver


def brower(url):
    chromedriver = "/Users/zhangc/Desktop/mine/PycharmProjects/PY项目/PyProject/project_Buger(2)/tools/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(10)
    return driver.get(url)