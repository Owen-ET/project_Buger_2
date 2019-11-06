#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/06 14:16
# @Author  : zc
# @File    : baidu_page.py


from poium import Page,PageElement
from poium测试库.functions.driver import brower
from time import sleep


class BaiduPage(Page):
    url = 'https://www.baidu.com'
    # 定位元素
    search_input = PageElement(css = "#kw",describe="输入框")
    search_button = PageElement(xpath = "//input[@id='su']",describe="查询按钮")


    def search_action(self,keys):
        self.search_input = keys
        self.search_button.click()


# if __name__ == '__main__':
#     BaiduPage(brower(url='https://www.baidu.com')).search_action(keys="selenium")