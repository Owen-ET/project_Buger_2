#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/08 14:40
# @Author  : zc
# @File    : desired_capabilities.py


from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def appium_desired():
    # 定义安卓运行环境
    desired_cap = {
        "deviceName":"vivo",                        # 真机名称
        "platformName":"android",                   # 使用的移动端：android、ios
        "platformVersion":"8.1",                  # 移动端版本
        "appPackage":"com.csksc2b.invertory",       # 被测试软件Package名
        "appActivity":"com.csks.login.SplashAty",   # 被测试软件Activity名
        # "noReset":True,                              # 重置应用状态:True，不重置，false重置清空登录
        "automationName":"UiAutomator2"

    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

    # id定位
    driver.find_element(By.ID,"com.csksc2b.invertory:id/edt_name_phone").send_keys("13642040631")
    driver.find_element(By.ID,"com.csksc2b.invertory:id/edt_pass").send_keys("886000")
    driver.find_element(By.ID,"com.csksc2b.invertory:id/tv_login").click()
    sleep(2)
    driver.implicitly_wait(10)
    # class name定位
    # driver.find_element(By.CLASS_NAME,"")->class属性
    # xpath定位
    driver.find_element(By.XPATH,"//*[@text='请假']").click()
    # driver.find_element(By.XPATH,"//*[contains(@text,'请假')]").click()
    # accessibility_id
    # driver.find_element_by_accessibility_id(),->content-desc属性
    # uiaotomator定位
    # driver.find_element_by_android_uiautomator('new UiSelector().text("请假")').click()
    # new UiSelector().text()->text属性
    # new UiSelector().description()->content-desc属性
    # new UiSelector().resourceId()->id属性
    # new UiSelector().className()->class属性





if __name__ == '__main__':
    appium_desired()
