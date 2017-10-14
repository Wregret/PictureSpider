#-*- coding:utf-8 -*-
import re
import requests
import sys
import os
from time import strftime

print "「百度图片爬虫 by Wregret」"

keyword=""
while keyword=="":
    keyword=raw_input("请输入您的搜索的图片关键词：")

number=raw_input("请输入您要搜索的图片数量（默认1张）：")
if number=="":
    number=1

if not (os.path.exists(keyword)):
    os.mkdir(keyword)



nowNumber=0

def getUrl(keyword,nowNumber):
    url="http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+keyword+"&pn="+str(nowNumber)+"&ct=&ic=0&lm=-1&width=0&height=0"
    return url

index=0
urlindex=0

html=requests.get(getUrl(keyword,nowNumber)).text
picurl=re.findall('"objURL":"(.*?)",',html,re.S)


while index<int(number):
    if(index>=60):
        urlindex=0
        nowNumber+=60
        html=requests.get(getUrl(keyword,nowNumber)).text
        picurl=re.findall('"objURL":"(.*?)",',html,re.S)
    print "["+str(index+1)+"]"+picurl[urlindex]
    try:
        pic=requests.get(picurl[urlindex],timeout=10)
    except requests.exceptions.ConnectionError:
        print '[ERROR]当前图片无法下载'
        index+=1
        urlindex+1
        continue
    path=keyword+'/'+str(index+1)+'.jpeg'
    with open(path,'wb') as file:
        file.write(pic.content)
    index+=1
    urlindex+=1

print "搜索和下载完成"
sys.exit()
