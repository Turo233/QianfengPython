'''
QQ  6666-1234567890
mail  turo@163.com
phone  010-55348281
user 6-12位
passwd
ip
url
'''
import re

def checkQQ(str):
    par = r"[1-9]\d{5,10}$"
    res = re.match(par, str)
    print(res)

# checkQQ("107474")

def checkMail(str):
    par = r"[^0][0-9a-zA-Z]*@[1-9a-zA-Z]{2,7}\.(com|cn)"
    res = re.match(par, str)
    print(res)
# checkMail("ls056@qq.cn")
def checkPhone(str):
    par = r"0\d{2}-\d{8}"
    res = re.match(par, str)
    print(res)
    #*******************************
    #问题:QQ 和 座机 超出8位数仍可以使用
    #解决:在末尾加 $ 可以解决 即 par = r"0\d{2}-\d{8}$ "
    #*******************************
# checkPhone("027-55348881")
def checkUser(str):
    par = r".{6,12}"
    res = re.match(par, str)
    print(res)
# checkUser("ls0564")
def checkPasswd(str):
    par = r".{6,8}"
    res = re.match(par, str)
    print(res)
# checkPasswd("asdf3#@#31")
def checkIp(str):
    #不知道怎么限制数大小
    par = r""
    res = re.match(par, str)
    print(res)

def checkUrl(str):
    par = r""
    res = re.match(par, str)
    print(res)
