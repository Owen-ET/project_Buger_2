#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/08 14:40
# @Author  : zc
# @File    : desired_capabilities.py


from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


def appium_desired():
    # 定义安卓运行环境
    desired_cap = {
        "deviceName":"vivo",                        # 真机名称
        "platformName":"android",                   # 使用的移动端：android、ios
        "platformVersion":"8.1",                  # 移动端版本
        "appPackage":"com.csksc2b.invertory",       # 被测试软件Package名
        "appActivity":"com.csks.login.SplashAty",   # 被测试软件Activity名
        # "noReset":True,                              # 重置应用状态:True，不重置，false重置清空登录
        # "automationName":"UiAutomator2"

    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
    driver.implicitly_wait(10)

    # id定位
    driver.find_element(By.ID,"com.csksc2b.invertory:id/edt_name_phone").send_keys("136420406311")
    driver.find_element(By.ID,"com.csksc2b.invertory:id/edt_pass").send_keys("886000")
    # driver.find_element(By.ID,"com.csksc2b.invertory:id/tv_login").click()
    sleep(2)
    # 安装app
    # driver.install_app("本地路径")
    # 卸载app
    # driver.remove_app("包名")
    # 关闭app
    # driver.close_app()
    # 重启app
    # driver.launch_app()
    # app包是否安装
    result = driver.is_app_installed("com.csksc2b.invertory")
    print(result)
    # 将应用置于后台
    # driver.background_app(10)
    # 重置
    # driver.reset()

    '''上下文操作'''
    # 获取可用上下文
    contexts1 = driver.contexts
    print(contexts1)
    # 当前上下文操作
    contexts2 = driver.current_context
    print(contexts2)
    # 切换上下文
    driver.switch_to.context(contexts2)


    '''键盘操作'''
    # 模拟按键
    # driver.find_element(By.ID, "com.csksc2b.invertory:id/edt_name_phone").click()
    # driver.keyevent(15)
    # 参考地址：https://developer.android.google.cn/reference/android/view/KeyEvent


    '''触摸操作'''
    # 单机控件
    # el = driver.find_element(By.XPATH,"//*[@text='审批']")
    el2 = driver.find_element(By.ID, "com.csksc2b.invertory:id/edt_name_phone")
    # TouchAction(driver).tap(el).release().perform()
    # 获取元素坐标：手机设置--开发者选项--指针位置
    #(540,2202):手机上的定位的坐标、(1073,2278):手机全屏的坐标
    # a1 = 540/1073
    # a2 = 2202/2278
    # width = driver.get_window_size()['width']
    # height = driver.get_window_size()['height']
    # TouchAction(driver).tap(x=a1*width,y=a2*height).perform()
    # print("坐标点击完成")
    # TouchAction(driver).tap(el2,count=5).perform()
    sleep(5)

    # 长按控件
    TouchAction(driver).long_press(el2).perform()
    TouchAction(driver).long_press(x='',y='').perform()
    TouchAction(driver).long_press(el2,duration=2000).perform()  # duration:按压时间


    # 移动



    driver.close_app()





if __name__ == '__main__':
    appium_desired()
