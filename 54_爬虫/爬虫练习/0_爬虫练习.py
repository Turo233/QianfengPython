#先做准备工作, 再写详细内容

import urllib.request
import re
import os

def imageCrawler(url, toPath):
    header = {
        "User-Agent": "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)"
        }
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")
    #先写到文件里, 分析
    # with open(r"E:\1编程\千锋python\Code\54_爬虫\file\yhd.html", "wb") as f:
    #     f.write(HtmlStr)

    #分析网页, 写正则
    pat = r'<div style="position: relative">\n<img src="//(.*?)"/>'
    re_image = re.compile(pat, re.S)
    imagesList = re_image.findall(HtmlStr)

    for i in range(len(imagesList)):
        path = os.path.join(toPath, str(i)+".jpg")
        #把图片下载到本地
        urllib.request.urlretrieve("http://"+imagesList[i], filename=path)

url = r"http://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E8%25A3%2585/"
toPath = r"E:\1编程\千锋python\Code\54_爬虫\file"
imageCrawler(url, toPath)
