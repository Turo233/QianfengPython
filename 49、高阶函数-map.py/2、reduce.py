from functools import reduce

#reduce(fn, lsd)
#参数1 为函数
#参数2 为列表

#功能: 一个函数作用在序列上, 这个函数必须接受两个参数,
#reduce把结果继续和序列的下一个元素累计运算

# reduce(f, [a, b, c, d])
# f(((a, b), c), d)


#需求
#求一个序列的和
list2 = [1, 2, 3, 4, 5]
#1 + 2
#1 + 2 + 3
#1 + 2 + 3 + 4
#1 + 2 + 3 + 4 + 5
def mySum(x, y):
    return x + y

r = reduce(mySum, list2)
# print(r)
