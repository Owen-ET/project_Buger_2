#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/05 15:37
# @Author  : zc
# @File    : test.py


# list = [{
#   'case1':
#    { 'data1': [ { 'keys': 'yaml01' }, { 'keys': 'yaml02' } ],
#      'data2': [ { 'keys': 'yaml03' }, { 'keys': 'yaml04' } ] },
#   'case2':
#    { 'data1': [ { 'keys': 'yaml05' }, { 'keys': 'yaml06' } ],
#      'data2': [ { 'keys': 'yaml07' }, { 'keys': 'yaml08' } ] },
#   'case3':
#    { 'data1': [ { 'keys': 'yaml09' }, { 'keys': 'yaml10' } ],
#      'data2': [ { 'keys': 'yaml11' }, { 'keys': 'yaml12' } ] } }]
#
# text = list[0]['case1']['data2'][0]['keys']
# print(text)



# from selenium import webdriver
#
# driver = webdriver.Chrome("/Users/zhangc/Desktop/mine/PycharmProjects/PY项目/PyProject/project_Buger(2)/tools/chromedriver")
# driver.get("https://www.baidu.com")



# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+'*'+str(j)+'='+str(i*j),end="\t")
#     # print("1",end="\t")
#     # print("1")
#     print()


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(j) + str("*") + str(i)+"=" + str(i*j),end="\t")
#     print()




list = [{
    "start_HRApp":
   { "ip": '127.0.0.1',
     "port": 4723,
     "implicitly_wait": 10,
     "caps":
      { "android":
         { "platformName": 'Android',
           "platformVersion": 6,
           "deviceName": 'OPPO',
           "appPackage": 'com.csksc2b.invertory',
           "appActivity": 'com.csks.login.SplashAty',
           "noReset": True,
           "unicodeKeyboard": True,
           "resetKeyboard": True,
           "autoGrantPermissions": True,
           "automationName": 'uiautomator2'
        },
        "ios": None
      }
   }
}]


# print(list[0][])

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")