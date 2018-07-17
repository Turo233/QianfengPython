import os
import random
import time

emailType = ['126', '163', 'qq', 'outlook']
emailNum = []
j = 100
while j:
    #生成首位数字不为0的八位数
    emailNum.append(str(random.randint(1,9)))
    for i in range(7):
        emailNum.append(str(random.randint(0, 9)))
    emailStr = "".join(emailNum)
    #将八位数字与emailType用@相连接
    email = emailStr + r"@" + random.choice(emailType) + ".com\n"
    #将email写入目标文件
    with open(r"E:\1编程\千锋python\email.txt", "a") as f:
        f.write(email)
    emailNum.clear()
    print(j)
    j -= 1
#print(fileList)
