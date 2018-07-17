'''
排序:冒泡, 选择      快速排序, 插入, 计数器
'''

#普通排序
list1 = [4, 7, 2, 6, 3]
list2 = sorted(list1)#默认升序排序
print(list1)
print(list2)

#按绝对值大小排序
list3 = [4, -7, -2, 6, -3]
#key接受函数来实现自定义排序规则
list4 = sorted(list3, key=abs)#默认升序排序
print(list3)
print(list4)

#降序排序
list5 = [4, 7, 2, 6, 3]
#reverse 反转
list6 = sorted(list5, reverse=True)#默认升序排序
print(list5)
print(list6)

#acill码
list7 = ["a33", "z22", "c4", "g1", "f5"]
list8 = sorted(list7)#默认升序排序
print(list7)
print(list8)

#函数可以自己写
def myLen(str):
    return len(str)
list9 = ["a33", "z22", "c4333", "g11", "f53333"]
list0 = sorted(list9, key=myLen)#默认升序排序
print(list9)
print(list0)
