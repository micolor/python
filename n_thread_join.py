# 线程合并（join方法）

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import threading

# 自定义线程类，继承自 threading.Thread
class MyThread(threading.Thread):
    def run(self):
        # 线程运行时执行的代码
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)  # 模拟工作负载

def main():
    print("Start main threading")

    # 创建并启动三个线程
    threads = [MyThread() for _ in range(3)]
    for t in threads:
        t.start()

    # 依次让新创建的线程执行 join
    # join 方法会阻塞主线程，直到对应的子线程执行完毕
    for t in threads:
        t.join()

    print("End main threading")

if __name__ == '__main__':
    main()


