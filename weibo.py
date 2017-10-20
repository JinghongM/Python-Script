# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time



cook = {"Cookie":"_T_WM=06191b79cf2bdf2f30c18397cbf358cc "} #放入你的cookie信息。

for i in range(1,20):

    #爬取"头条新闻"的前二十页微博
    url = "http://weibo.cn/breakingnews?page=%d"%(i)

    html = requests.get(url,cookies=cook).content

    #使用Beautiful来解析网页内容。
    soup =BeautifulSoup(html,"html.parser")

    r = soup.findAll('span',attrs={"class" : "ctt"})
    file_object=open("thefile.txt",'w')
	for e in r:
	    print "abc"
	#	file_object.writelines(e.text)

	#    print(e.text)

    #设置时间间隔
    time.sleep(3)