#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 11:50
# @Author  : zc
# @File    : app_config.py

from appium import webdriver

def des_caps():

    Cap = {
        "deviceName":"vivo",
        "platformName":"Android",
        "platformVersion":"8.1",
        "appPackage":"com.csksc2b.invertory",
        "appActivity":"com.csks.login.SplashAty",
        # "noReset":True
        "automationName":"UiAutomator2"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub",Cap)
    driver.implicitly_wait(10)

    return driver