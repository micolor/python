#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import threading, time

# 消费者线程类
class Consumer(threading.Thread):
    def __init__(self, cond, name):
        # 初始化
        super(Consumer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        # 确保先运行Seeker中的方法
        time.sleep(1)
        self.cond.acquire()
        print(self.name + ': 我这两件商品一起买，可以便宜点吗')
        self.cond.notify()  # 通知生产者
        self.cond.wait()    # 等待生产者回应
        print(self.name + ': 我已经提交订单了，你修改下价格')
        self.cond.notify()  # 通知生产者
        self.cond.wait()    # 等待生产者回应
        print(self.name + ': 收到，我支付成功了')
        self.cond.notify()  # 通知生产者
        self.cond.release() # 释放锁
        print(self.name + ': 等待收货')

# 生产者线程类
class Producer(threading.Thread):
    def __init__(self, cond, name):
        super(Producer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        # 释放对锁的占用，同时线程挂起在这里，直到被 notify 并重新占有锁。
        self.cond.wait()
        print(self.name + ': 可以的，你提交订单吧')
        self.cond.notify()  # 通知消费者
        self.cond.wait()    # 等待消费者回应
        print(self.name + ': 好了，已经修改了')
        self.cond.notify()  # 通知消费者
        self.cond.wait()    # 等待消费者回应
        print(self.name + ': 嗯，收款成功，马上给你发货')
        self.cond.release() # 释放锁
        print(self.name + ': 发货商品')

# 创建条件变量
cond = threading.Condition()
# 创建消费者和生产者线程
consumer = Consumer(cond, '买家')
producer = Producer(cond, '卖家')
# 启动线程
consumer.start()
producer.start()
