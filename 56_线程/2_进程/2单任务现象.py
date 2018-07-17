from time import sleep

def run():
    while True:
        print("turo is a nice man")
        sleep(1.2)

if __name__ == "__main__":
    while True:
        print("turo is a good man")
        sleep(1)
        
    #只能执行上面的任务
    #不会执行到run()方法, 只有上面的while循环结束才可以执行

    run()
