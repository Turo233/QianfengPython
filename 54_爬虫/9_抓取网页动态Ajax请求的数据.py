#不完整, 以后会通过啥方法将网页完全加载出来再抓取

import urllib.request
import ssl
import json

def ajaxCrawler(url):
    headers = {
        "User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)"
    }
    req = urllib.request.Request(url, headers=headers)

    #爬取https, 使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)


    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData
'''
https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20
'''

url = r"https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20"
info = ajaxCrawler(url)
print(info)

#加载动态页面
for i in range(1, 11):
    url = r"https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start="+ str(i * 20) + "&limit=20"
    info = ajaxCrawler(url)
    print(len(info))
