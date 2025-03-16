# 线程的创建

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import threading

# 定义一个继承自 threading.Thread 的类
class MyThread(threading.Thread):
    # 重写 run 方法，定义线程的行为
    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)

def main():
    print("Start main threading")

    # 创建并启动三个线程
    threads = [MyThread() for _ in range(3)]
    for t in threads:
        t.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

    print("End Main threading")

if __name__ == '__main__':
    main()

