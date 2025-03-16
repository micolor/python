# 创建进程的类

# Process([group [, target [, name [, args [, kwargs]]]])
# 参数说明：
# - target：表示调用对象，即子进程要执行的任务
# - args：表示调用对象的位置参数元组
# - kwargs：表示调用对象的字典参数
# - name：为进程设置别名
# - group：实质上不使用，值始终为None

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import multiprocessing
import time

def worker(interval, name):
    """
    子进程要执行的任务函数
    :param interval: 睡眠时间
    :param name: 进程名称
    """
    print(name + '【start】')
    time.sleep(interval)
    print(name + '【end】')

if __name__ == "__main__":
    # 创建三个进程
    p1 = multiprocessing.Process(target=worker, args=(10, 'a'))
    p2 = multiprocessing.Process(target=worker, args=(20, 'b'))
    p3 = multiprocessing.Process(target=worker, args=(30, 'c'))

    # 启动进程
    p1.start()
    p2.start()
    p3.start()

    # 输出CPU数量
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    
    # 输出所有活跃的子进程信息
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    
    # 等待所有子进程结束
    p1.join()
    p2.join()
    p3.join()
    
    print("END!!!!!!!!!!!!!!!!!")