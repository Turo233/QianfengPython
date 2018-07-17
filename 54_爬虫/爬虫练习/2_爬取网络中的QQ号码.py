import urllib.request
import ssl
import re
import os
from collections import deque#队列

#拆解, 爬取内容存入本地, 一种存字节, 一种存字符串
def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes, toPath):
    with open(toPath, "w") as f:
        f.write(str(htmlBytes))
def getHtmlBytes(url):
    header = {
        "User-Agent": "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)"
        }
    req = urllib.request.Request(url, headers=header)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()
#爬虫, 爬取的qq 写到某文件
def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    # writeFileBytes(htmlBytes, r"E:\1编程\千锋python\Code\54_爬虫\file\qqFile1.html")
    # writeFileStr(htmlBytes, r"E:\1编程\千锋python\Code\54_爬虫\file\qqFile2.html")
    htmlStr = str(htmlBytes)

    pat = r'''((http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)?((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.[a-zA-Z]{2,4})(\:[0-9]+)?(/[^/][a-zA-Z0-9\.\,\?\'\\/\+&amp;%\$#\=~_\-@]*)*)'''
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    urlsList = list(set(urlsList))
    # print(len(urlsList))
    # print(urlsList[100])
    # print(urlsList[101])


    pat = r'[1-9]\d{4,9}'
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    #去重
    qqsList = list(set(qqsList))
    # print(qqsList)
    # print(len(qqsList))
    with open(toPath, "a") as f:
        for qqStr in qqsList:
            f.write(qqStr+"\n")
    return urlsList

# qqCrawler(url, toPath)


#写中央控制器来使其可以爬取多个网页
def center(url, toPath):
    queue = deque()

    queue.append(url)

    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl, toPath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)

url = r"https://www.douban.com/group/topic/17359302/"
toPath = r"E:\1编程\千锋python\Code\54_爬虫\file\qqFile.txt"
try:
    center(url, toPath)
except:
    pass
