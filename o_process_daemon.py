# daemon 属性

# -*- coding: UTF-8 -*-

import multiprocessing
import time

def worker(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))

if __name__ == '__main__':
    # 创建一个进程
    p = multiprocessing.Process(target=worker, args=(3,))
    # 将进程设置为守护进程
    # 守护进程会在主进程结束时自动终止
    p.daemon = True
    # 启动进程
    p.start()
    # 主进程打印信息
    print('【EMD】')
    # 主进程结束后，守护进程也会随之结束