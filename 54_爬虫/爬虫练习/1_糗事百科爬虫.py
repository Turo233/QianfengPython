# https://www.qiushibaike.com/8hr/page/1/
# https://www.qiushibaike.com/8hr/page/2/


import urllib.request
import re

def jokeCrawler(url):

    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)")
    response = urllib.request.urlopen(req)

    HTML = response.read().decode("utf-8")

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat, re.S)
    divList = re_joke.findall(HTML)
    # print(divList)
    #print(len(divList))
    dic = {}
    for div in divList:
        #用户名
        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = re_u.findall(div)
        username = username[0]

        #段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        joke = re_d.findall(div)
        joke = joke[0]
        dic[username] = joke
    return dic
    # 打印出源代码进行寻找
    # with open(r"E:\1编程\千锋python\Code\54_爬虫\file\file3.html", "w") as f:
    #     f.write(HTML)


url = r"http://www.qiushibaike.com/8hr/page/1/"
info = jokeCrawler(url)
for k,v in info.items():
    print(k, v)
