#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 11:50
# @Author  : zc
# @File    : app_config.py

from appium import webdriver
import yaml
import os

def des_caps():

    # Cap = {
    #     "deviceName":"vivo",
    #     "platformName":"Android",
    #     "platformVersion":"8.1",
    #     "appPackage":"com.csksc2b.invertory",
    #     "appActivity":"com.csks.login.SplashAty",
    #     # "noReset":True
    #     "automationName":"UiAutomator2"
    # }

    # 基础路径
    base_dir = os.path.dirname(os.path.dirname(__file__))
    # yaml路径
    yaml_path = base_dir + "/data/ddt_data_file.yaml"
    # 获取yaml的数据
    with open(yaml_path,'r',encoding='utf-8') as file:
        data = yaml.load(file)
    start = data['start_HRApp']
    Cap = start['caps']['android']

    driver = webdriver.Remote("http://"+ str(start['ip']) +":"+ str(start['port']) +"/wd/hub",Cap)
    driver.implicitly_wait(10)

    return driver


des_caps()