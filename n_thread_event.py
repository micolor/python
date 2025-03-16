# -*- coding: UTF-8 -*-

# threading.Event 对象用于在线程之间进行信号传递。
# event.set() 设置内部标志为 True，表示事件已发生。
# event.clear() 清除内部标志，将其设置为 False。
# event.wait() 阻塞线程，直到内部标志为 True。
# event.is_set() 检查内部标志是否为 True。
# 在 run 方法中，线程根据 event 的状态执行不同的操作，从而实现线程间的同步。

import threading

class mThread(threading.Thread):
    def __init__(self, threadname):
        super().__init__(name=threadname)  # 使用super()简化初始化

    def run(self):
        global event
        if event.is_set():  # 使用is_set()代替isSet()
            event.clear()  # 清除内部标志，将其设置为 False
            event.wait()   # 阻塞线程，直到内部标志为 True
            print(self.getName())
        else:
            print(self.getName())
            event.set()    # 设置内部标志为 True，表示事件已发生

event = threading.Event()
event.set()  # 设置初始状态为 True
threads = [mThread(str(i)) for i in range(10)]  # 创建10个线程

for thread in threads:
    thread.start()  # 启动所有线程