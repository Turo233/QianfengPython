import os

#邮箱分类

#邮箱根据@切片、根据.切片
#根据切片内容创建文件夹

#打开目标文件
with open(r"E:\1编程\千锋python\program\emailtask\email.txt", "r") as f:
    #读取一行
    fLen = len(f.readlines())
    f.seek(0)
    for i in range(fLen):
        fileLine = f.readline()
        #print(fileLine)
        #读取该行邮箱类型
        emailType = fileLine.split("@")[1].split(".")[0]
        #创建目标目录
        filePath = r"E:\1编程\千锋python\program\emailtask" +os.sep + emailType
        if not os.path.exists(filePath):
            os.mkdir(filePath)
        #创建目标文件路径
        path = r"E:\1编程\千锋python\program\emailtask" +os.sep + emailType +  os.sep + "邮箱" + emailType + ".txt"
        with open(path, "a") as f1:
            f1.write(fileLine)
