import threading, time

def func():
    #事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            #阻塞, 等待事件的触发
            event.wait()
            #重置, 如果不重置, 下一次不阻塞
            event.clear()
            print("turo is a good man!! %d" % i)
    t = threading.Thread(target=run).start()
    return event

e = func()

#触发事件
for i in range(5):
    e.set()
    time.sleep(2)
