from multiprocessing import Process
from time import sleep
import os

def run(str):
    print("子进程启动")
    sleep(3)
    print("子进程结束")

if __name__ == "__main__":
    print("父进程启动")
    p = Process(target=run, args=("nice",))
    p.start()

    #父进程的结束不能影响子进程, 需求让父进程等待子进程结束再让父进程结束
    #(父进程不干活, 创建多个子进程, 全部子进程结束后主进程结束)
    #->
    p.join()
    print("父进程结束")

'''
父进程启动
父进程结束
子进程启动
子进程结束

Process returned 0 (0x0)        execution time : 3.289 s
请按任意键继续. . .

'''
