#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    # 写数据进程
    print('写进程的PID:{0}'.format(os.getpid()))
    for value in ['a', 'b', 'c']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)  # 将值放入队列
        time.sleep(random.random())  # 随机休眠一段时间

def read(q):
    # 读取数据进程
    print('读进程的PID:{0}'.format(os.getpid()))
    while True:
        value = q.get(True)  # 从队列中读取值
        print('从 Queue 读取的值为：{0}'.format(value))

if __name__ == '__main__':
    # 父进程创建 Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))  # 创建写进程
    pr = Process(target=read, args=(q,))  # 创建读进程
    # 启动子进程 pw
    pw.start()
    # 启动子进程 pr
    pr.start()
    # 等待 pw 结束
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()