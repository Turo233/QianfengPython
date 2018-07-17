import urllib.request

#向指定的url地址发起请求, 并返回服务器响应的数据(文件的对象)
response = urllib.request.urlopen("http://www.baidu.com")

#读取文件的全部内容, 会把读取到的数据赋值给一个字符串变量
# data = response.read()
# print(data)
# print(type(data)) #bytes

#将爬取到的网页写入文件
# with open(r"E:\1编程\千锋python\Code\54_爬虫\file\file1.html", "wb") as f:
#     f.write(data)

#读取一行
#data = response.readline()

#读取文件的全部内容, 会把读取到的数据赋值给一个列表变量
data = response.readlines()
'''
print(data)
print(type(data)) #list
print(len(data))
print(type(data[100].decode("utf-8"))) #把数据改为字符串类型
'''


#response 属性
#返回当前环境的有关信息
print(response.info())

#返回状态码
#500以上服务器问题
#400以上请求问题
#200以上基本成功
print(response.getcode())
# if response.getcode() == 200 or response.getcode() == 304:
    #处理网页信息
    # pass

#返回当前正在爬取的URL地址
print(response.geturl())


url = r"https://www.baidu.com/s?wd=%E5%87%AF%E5%93%A5%E5%AD%A6%E5%A0%82&rsv_spt=1&rsv_iqid=0xaab6ecbd0003e9f1&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=monline_3_dg&rsv_enter=1&rsv_sug3=14&rsv_sug1=11&rsv_sug7=100&rsv_t=119fpIvTWPi9dkvj%2BxneoN8IyGsTkKRnAh06oB896YviuoW7vVlNdcOh93cWUJ7E3kyZ&rsv_sug2=0&inputT=48454&rsv_sug4=50324"

#解码
newUrl = urllib.request.unquote(url) #汉字地址直接urlopen会报错
print(newUrl)

#编码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)
