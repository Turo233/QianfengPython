
from functools import reduce

#需求1
#将字符串转成对应自变量数字
def str2int(str):
    def fc(x, y):
        return x * 10 + y
    def fs(char):
        return{"0":0, "1":1, "2":2, "3":3, "4":4, "5":5
        , "6":6, "7":7, "8":8, "9":9}[char]
    return reduce(fc, map(fs, list(str)))

a = str2int("12356")
print(a)
print(type(a))
