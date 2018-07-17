str1 = input("输入字符串: ")
str2 = str1.strip()

for index in range(len(str1)):
    if ord(str1[index]) >= 97 and  ord(str1[index]) <= 122:
        print(chr(ord(str1[index]) - 32), end="")
    elif ord(str1[index]) >= 65 and  ord(str1[index]) <= 90:
        print(chr(ord(str1[index]) + 32), end="")



# print(ord('b')-ord('B')) = 32
#a -> 97  z -> 122
#A -> 65  Z -> 90
