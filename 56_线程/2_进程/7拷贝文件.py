import os, time
from multiprocessing import Process

def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")

    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


path = r"E:\1编程\千锋python\Code\56_线程\2_进程\file"
toPath = r"E:\1编程\千锋python\Code\56_线程\2_进程\tofile"

#读取path下的所有文件
fileList = os.listdir(path)

#启动for 循环处理每一个文件
start = time.time()
for fileName in fileList:
    copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))
end = time.time()
print("总耗时: %0.2f" % (end-start))
