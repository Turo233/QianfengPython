# num = int(input("请输入一个需要被分解的数："))
#
# i = num - 1
# print("num = %d 的分解质因数为" % num, end=" ")
# while i:
#     if num % i == 0:
#         a = num // i
#         num = i
#         print(a, end=", ")
#     i -= 1

num = int(input())
i = 2
while num != i:
    if num % i == 0:
        print(i)
        num //= i
    else:
        i += 1
print(i)
