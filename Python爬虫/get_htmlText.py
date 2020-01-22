#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/01/22 10:18
# @Author  : zc
# @File    : get_htmlText.py

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image


# 重定向爬虫h4
url = "http://www.itest.info/courses"
soup = BeautifulSoup(requests.get(url).text,'html.parser')

for courses in soup.find_all('p'):
    print(courses.text)
    print("\r")



# v2ex爬虫标题
url = "https://www.v2ex.com"
v2ex = BeautifulSoup(requests.get(url).text,'html.parser')

for span in v2ex.find_all('span',class_='item_hot_topic_title'):
    print(span.find('a').text,span.find('a')['href'])

for title in v2ex.find_all("a",class_="topic-link"):
    print(title.text,url+title["href"])



# 煎蛋爬虫图片
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def download_file(url):
    '''下载图片'''
    print('Downding %s' %url)
    local_filename = url.split('/')[-1]
    img_path = "/Users/zhangc/Desktop/GitTest/project_Buger_2/Python爬虫/img/" + local_filename
    print(local_filename)
    r = requests.get(url, stream=True, headers=headers)
    with open(img_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return img_path

url = 'http://jandan.net/drawings'
soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

def valid_img(src):
    '''判断地址符不符合关键字'''
    return src.endswith('jpg') and '.sinaimg.cn' in src

for img in soup.find_all('img', src=valid_img):
    src = img['src']
    if not src.startswith('http'):
        src = 'http:' + src
    download_file(src)


# 知乎热门
headers ={
    "user-agent":"user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
url = "https://www.zhihu.com/explore"
zhihu = BeautifulSoup(requests.get(url,headers=headers).text,"html.parser")
for title in zhihu.find_all('a',class_="ExploreSpecialCard-contentTitle"):
    print(title.text)


# selenium爬虫
url = "https://www.zhihu.com/explore"
driver = webdriver.Chrome("/Users/zhangc/Desktop/GitTest/project_Buger_2/poium测试库/tools/chromedriver")
driver.get(url)

info = driver.find_element(By.CSS_SELECTOR,"div.ExploreHomePage-specials")
for title in info.find_elements(By.CSS_SELECTOR,"div.ExploreHomePage-specialCard > div.ExploreSpecialCard-contentList > div.ExploreSpecialCard-contentItem > a.ExploreSpecialCard-contentTitle"):
    print(title.text,title.get_attribute('href'))