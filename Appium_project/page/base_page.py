#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 14:07
# @Author  : zc
# @File    : base_page.py

from Appium_project.common.app_config import des_caps

class AppPage(object):


    def __init__(self,webdriver):
        self.driver = webdriver


    def find_element(self,*loc):
        return self.driver.find_element(*loc)


    def click(self,loc):
        self.find_element(*loc).click()


    def send_keys(self,loc,text):
        self.find_element(*loc).send_keys(text)


    def getText(self,loc):
        return self.find_element(*loc).text

