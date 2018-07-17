import re
#pip 包管理工具

'''
13812345678djfaj;a;sdkjflaksj

'''

'''

re.match函数
原型:match(pattern, string, flags=0)
参数:
    pattern: 匹配的正则表达式
    string: 要匹配的字符串
    flags: 标志位, 用于控制正则表达式的匹配方式值如下:
        re.I 忽略大小写 (*常用)
        re.L 做本地化识别(一般不用)
        re.M 多行匹配, 影响 ^ 和 $ (*也可以用)
        re.S 使 . 匹配包括换行符在内的所有字符(*常用)
        re.U 根据Unicode字符集解析字符, 影响 \w \W \b \B
        re.X 使我们以更灵活的格式理解正则表达式(一般不用)

功能:尝试从字符串的起始位置匹配一个模式, 如果不是起始位置,匹配成功
的话, 也会返回None

'''
# www.baidu.com
print(re.match("www", "www.baidu.com").span())#得到其在字符串中的位置
print(re.match("www", "ww.baidu.com"))
print(re.match("www", "baidu.wwwcom"))
print(re.match("www", "wwW.baidu.com"))
print(re.match("www", "wwW.baidu.com", flags=re.I)) #.match()无效且报错
#扫描整个字符串, 返回从起始位置成功的匹配

print("--------------------------------------")

'''
re.search函数
原型: re.search(pattern, string, flags=0)
参数:
    pattern: 匹配的正则表达式
    string: 要匹配的字符串
    flags: 标志位, 用于控制正则表达式的匹配方式
功能:扫描整个字符串, 并返回第一个成功的匹配

'''
print(re.search("sunck", "good man is sunck! sunck is nice"))

print("--------------------------------------")

'''
re.findall函数
原型: re.findall(pattern, string, flags=0)
参数:
    pattern: 匹配的正则表达式
    string: 要匹配的字符串
    flags: 标志位, 用于控制正则表达式的匹配方式
功能:扫描整个字符串, 并返回结果列表

'''
print(re.findall("sunck", "good man is sunck! Sunck is nice", flags=re.I))
