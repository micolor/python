# 进程池 Pool
# -*- coding: UTF-8 -*-

from multiprocessing import Pool
import os, time, random

# 定义一个耗时任务函数
def long_time_task(name):
    print('进程的名称：{0} ；进程的PID: {1} '.format(name, os.getpid()))
    start = time.time()
    # 模拟一个耗时操作
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程 {0} 运行了 {1} 秒'.format(name, (end - start)))

if __name__ == '__main__':
    print('主进程的 PID：{0}'.format(os.getpid()))
    # 创建一个包含4个进程的进程池
    p = Pool(4)
    # 向进程池中添加任务
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    # 关闭进程池，不再接受新的任务
    p.close()
    # 等待所有子进程结束后再关闭主进程
    p.join()
    print('【End】')