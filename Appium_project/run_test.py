#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 11:50
# @Author  : zc
# @File    : run_test.py

import os
import time
import unittest
import yagmail
from os.path import dirname,abspath
from BSTestRunner import BSTestRunner


def send_mail(report):
    '''发送邮件方法'''
    yag = yagmail.SMTP(user="zhangchanget@126.com",
                 password="Dayuzhou66",
                 host="smtp.126.com")

    subject = "邮件标题：人力APP自动化测试报告"
    contents = "邮件正文：测试报告在邮件附件中"
    receive = "943102912@qq.com"
    yag.send(receive,subject,contents,report)
    print("发送邮件成功！")



if __name__ == '__main__':

    # 基础路径
    path = dirname(abspath(__file__))
    # 测试用例路径
    test_path = path + "/test_case/"
    # 时间
    now = time.strftime("%Y-%M-%d_%H-%M-%S")
    # 报告名称
    report_name = now + "_report.html"
    # 报告路径
    report_path = path + "/test_report/" + report_name

    fp = open(report_path,'wb')


    # 运行测试用例
    discover = unittest.defaultTestLoader.discover(start_dir=test_path,pattern="test*.py")

    # 用例放到报告中
    runner = BSTestRunner(stream=fp,
                          title="人力APP自动化测试：",
                          description="执行下面的测试用例：")

    runner.run(discover)
    fp.close()


    # 发送邮件
    send_mail(report_path)
