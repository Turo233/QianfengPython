from turoProcess import TuroProcess

if __name__ == "__main__":
    print("父进程启动")

'''
优点: 子进程方法不用写在主进程中, 主进程结构更清晰
'''
    #创建子进程
    p = TuroProcess("test")
    #自动调用p进程对象的run方法
    p.start()
    p.join()

    print("父进程结束")
