import urllib.request

path = r"E:\1编程\千锋python\Code\54_爬虫\file\file2.html"
urllib.request.urlretrieve("http://www.baidu.com", filename=path)

#urlretrieve在执行的过程当中, 会产生一些缓存, 耗费性能

#清除缓存
urllib.request.urlcleanup()
