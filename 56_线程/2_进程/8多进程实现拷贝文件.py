import os, time
from multiprocessing import Pool

def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")

    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


path = r"E:\1编程\千锋python\Code\56_线程\2_进程\file"
toPath = r"E:\1编程\千锋python\Code\56_线程\2_进程\tofile"


if __name__ == "__main__":
    #读取path下的所有文件
    fileList = os.listdir(path)

    start = time.time()
    pp = Pool(2)
    for fileName in fileList:
        pp.apply_async(copyFile, args=(os.path.join(path, fileName), os.path.join(toPath, fileName)))

    pp.close()
    pp.join()
    end = time.time()
    print("总耗时: %0.2f" % (end-start))
