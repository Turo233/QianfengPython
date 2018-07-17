import os

def getAllDir(path, sp = ""):
    fileList = os.listdir(path)
    sp += "  "
    for fileName in fileList:
        #判断是否是路径
        fileAbsPath = os.path.join(path, fileName)

        if os.path.isdir(fileAbsPath):
            print(sp + "目录：", fileName)
            #递归调用
            getAllDir(fileAbsPath, sp)
        else:
            print(sp + "普通文件:", fileName)


getAllDir(r"E:\1编程\千锋python")
