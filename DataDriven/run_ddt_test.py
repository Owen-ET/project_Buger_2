#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/05 16:32
# @Author  : zc
# @File    : run_ddt_test.py

import time
import yagmail
import unittest
from BSTestRunner import BSTestRunner


def send_mail(report):
    yag = yagmail.SMTP(user='xxx@126.com',
                       password='xxx',
                       host='smtp.126.com'
                       )
    subject = '邮件标题：自动化测试报告'
    contents = '正文，请查看附件'
    yag.send('943102912@qq.com',subject,contents,report)
    print("邮件发送成功！")





if __name__ == '__main__':

    case_path = "./test_case/"
    time = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = time + "_report.html"
    report_path = "./report/" + report_name

    fp = open(report_path,'wb')

    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
    runner = BSTestRunner(stream = fp,
                          title = '数据驱动测试用例：',
                          description = '执行下面的用例：')

    runner.run(discover)
    fp.close()

    send_mail(report_path)





