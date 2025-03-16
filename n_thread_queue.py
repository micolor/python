# 线程间通信

# -*- coding: UTF-8 -*-
from queue import Queue, Empty
from threading import Thread, Event
import time

# 全局变量，用于控制读线程的运行状态
isRead = True

def write(q):
    # 写数据进程
    for value in ['a', 'b', 'c']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)  # 将数据放入队列
        time.sleep(1)  # 模拟写入延迟

def read(q):
    # 读取数据进程
    while isRead or not q.empty():
        try:
            value = q.get(timeout=1)  # 从队列中获取数据，设置超时时间为1秒
            print('从 Queue 读取的值为：{0}'.format(value))
        except Empty:
            pass  # 如果队列为空，继续循环

if __name__ == '__main__':
    q = Queue()  # 创建队列实例
    t1 = Thread(target=write, args=(q,))  # 创建写线程
    t2 = Thread(target=read, args=(q,))  # 创建读线程
    t1.start()  # 启动写线程
    t2.start()  # 启动读线程
    t1.join()  # 等待写线程结束
    isRead = False  # 通知读线程停止
    t2.join()  # 等待读线程结束