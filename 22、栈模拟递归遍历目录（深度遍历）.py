import os

def getAllDirDE(path):
    stack = []
    stack.append(path)

    #处理栈，当栈为空时结束循环
    while len(stack) != 0:
        #从栈里取出数据
        #[]
        dirPath = stack.pop()
        #print(dirPath)
        filesList = os.listdir(dirPath)
        #print(filesList)
        #处理每一个文件，如果是普通文件则打印出来，
        #如果是目录则将该目录的地址牙栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录：", fileName)
                stack.append(fileAbsPath)
            else:
                #打印普通文件
                print("文件：", fileName)

getAllDirDE(r"E:\1编程\千锋python")
