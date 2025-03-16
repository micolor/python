# 把进程创建成类
# -*- coding: UTF-8 -*-

import multiprocessing
import time

# 定义一个继承自 multiprocessing.Process 的类
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        # 调用父类的构造函数
        multiprocessing.Process.__init__(self)
        self.interval = interval

    # 重写 run 方法，定义进程启动后的行为
    def run(self):
        n = 5
        while n > 0:
            print("当前时间: {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

# 主程序入口
if __name__ == '__main__':
    # 创建 ClockProcess 类的实例，并传入时间间隔参数
    p = ClockProcess(3)
    # 启动进程
    p.start()
    # 等待进程结束
    p.join()