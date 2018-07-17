'''
特点: 把参数进行打包, 单独传输

优点: 承载数据大, 安全(当对服务器进行修改时, 建议使用pos)

缺点: 速度慢
'''

import urllib.request
import urllib.parse #对参数进行打包

url = ""
#将要发送的数据, 合成一个字典
#字典的键去网址里找, 一般为input标签里的name属性的值
data = {
    "username": "turo",
    "passwd":"666"
}
#对要发送的数据进行打包, 记住编码
postData = urllib.parse.urlencode(data).encode("utf-8")
#请求体
req = urllib.request.Request(url, data=postData)
#发起请求
req.add_header("User-Agent":"Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11")
response = urllib.request.urlopen(req)
