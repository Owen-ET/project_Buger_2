#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 17:21
# @Author  : zc
# @File    : v2ex_api_test.py

import yaml


class TestV2exApi(object):

    with open("./data/request.yaml",'r',encoding='utf-8') as file:
        data = yaml.load(file)


