num1 = int(input("输入第一个数"))
num2 = int(input("输入第二个数"))
rNum = 1

while rNum != 0:
    rNum = num2 % num1
    num2 = num1
    num1 = rNum
print(num2)
