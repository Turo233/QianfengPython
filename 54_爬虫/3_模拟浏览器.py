import urllib.request
import random

url = "http://www.baidu.com"

#User-Agent
#Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0

'''
#模拟请求头
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    "Content-Type": "text/html;charset=utf-8"
}

#设置一个请求体
req = urllib.request.Request(url, headers=headers)

#发起请求, 请求头
response = urllib.request.urlopen(req)

data = response.read().decode("utf-8")
print(data)
'''

#从网上找User-Agent大全
agentList = [
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)"
]
agentStr = random.choice(agentList)
req = urllib.request.Request(url)
#向请求体里添加了User-Agent
req.add_header("User-Agent", agentStr)
response = urllib.request.urlopen(req)

print(response.read().decode("utf-8"))
