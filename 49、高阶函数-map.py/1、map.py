
#Google 文章

#分布式 - 多几台电脑干活， 分给几个电脑是map()  合成整体是reduce
#map() 处理列表中的每一个元素，
#reduce 处理列表在合成为一个列表
#python 内置了map()和reduce函数



#map()
#原型  map(fn, lsd)
#参数1 是函数
#参数2 是序列

#*************************************************
#功能: 将传入的函数依次作用在序列中的每一个元素,并把结果作为
#新的Interator(可迭代对象)返回
#***********************************************

#需求
#将单个字符转成对应的字面量整数
def char2int(char):
    return{"0":0, "1":1, "2":2, "3":3, "4":4, "5":5
    , "6":6, "7":7, "8":8, "9":9}[char]

list1 = ["2", "1", "6", "5"]
res = map(char2int, list1)
#[char2int("2"), char2int("1"), char2int("6"), char2int("5")]
# 惰性列表需要转换成列表
print(res)
print(list(res))



#需求2
#将整数元素的序列,转为字符串类型
#[1, 2, 3, 4]  -> ["1", "2", "3", "4"]

l = map(str, [1, 2, 3, 4])
print(list(l))



def myMap(func, li):
    resList = []
    for param in li:
        res = func(param)
        resList.append(res)
    return resList
print(myMap(char2int, list1))
