'''

multiprocessing 库
跨平台版本的多进程模块, 提供了一个Process类来代表一个进程对象

(linux中有fork库)
'''

from multiprocessing import Process
from time import sleep
import os

#子进程需要执行的代码
def run(str):
    while True:
        #os.getpid()获取当前进程ID号
        #os.getppid()获取当前进程的父进程ID号
        print("turo is a %s man -%s-%s" %(str, os.getpid(), os.getppid()))
        sleep(1.2)

if __name__ == "__main__":
    print("主(父)进程启动...-%s" % (os.getpid()))
    #创建一个子进程
    #target 说明进程要执行的任务
    #args 需要传的参
    p = Process(target=run, args=("nice",))
    #启动进程
    p.start()

    q = Process(target=run, args=("happy",))
    q.start()
    
    while True:
        print("turo is a good man")
        sleep(1)
