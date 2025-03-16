# 线程同步与互斥锁

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import threading
import time

# 创建一个锁对象
lock = threading.Lock()

# 共享资源
shared_resource = 0

# 线程函数
def thread_task():
    global shared_resource
    for _ in range(100):
        # 获取锁
        lock.acquire()
        try:
            # 操作共享资源
            temp = shared_resource
            time.sleep(0.001)  # 增加延迟以更容易观察竞争条件
            shared_resource = temp + 1
        finally:
            # 释放锁
            lock.release()

# 创建多个线程
threads = []
for i in range(10):
    thread = threading.Thread(target=thread_task)
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"最终共享资源的值: {shared_resource}")

# 说明：
# 在上述代码中，我们创建了一个锁对象 `lock`，并在每次操作共享资源 `shared_resource` 时获取锁。
# 这样可以确保同一时间只有一个线程可以修改共享资源，从而避免竞争条件。
# 如果注释掉 `lock.acquire()` 和 `lock.release()`，则多个线程会同时访问和修改共享资源，导致最终结果不准确。
# 增加 `time.sleep(0.01)` 延迟可以更容易地观察到竞争条件的影响。

# 可重入锁案例
reentrant_lock = threading.RLock()

def reentrant_task():
    reentrant_lock.acquire()
    try:
        print(f"{threading.current_thread().name} 获取了可重入锁")
        reentrant_lock.acquire()
        try:
            print(f"{threading.current_thread().name} 再次获取了可重入锁")
        finally:
            reentrant_lock.release()
    finally:
        reentrant_lock.release()

# 创建并启动线程
reentrant_thread = threading.Thread(target=reentrant_task)
reentrant_thread.start()
reentrant_thread.join()

# 说明：
# 可重入锁（RLock）允许同一个线程多次获取同一个锁，而不会导致死锁。
# 在上述案例中，线程可以多次获取 `reentrant_lock`，并在最后释放锁。

# 递归锁案例
recursive_lock = threading.RLock()

def recursive_task(level):
    recursive_lock.acquire()
    try:
        print(f"{threading.current_thread().name} 获取了递归锁，level: {level}")
        if level > 0:
            recursive_task(level - 1)
    finally:
        recursive_lock.release()

# 创建并启动线程
recursive_thread = threading.Thread(target=lambda: recursive_task(3))
recursive_thread.start()
recursive_thread.join()

# 说明：
# 递归锁（RLock）允许同一个线程在不同的递归层次上多次获取同一个锁，而不会导致死锁。
# 在上述案例中，线程可以在递归调用中多次获取 `recursive_lock`，并在最后释放锁。

# 死锁案例
lock1 = threading.Lock()
lock2 = threading.Lock()

def deadlock_task1():
    lock1.acquire()
    time.sleep(0.1)
    lock2.acquire()
    lock2.release()
    lock1.release()

def deadlock_task2():
    lock2.acquire()
    time.sleep(0.1)
    lock1.acquire()
    lock1.release()
    lock2.release()

# 创建并启动线程
thread1 = threading.Thread(target=deadlock_task1)
thread2 = threading.Thread(target=deadlock_task2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

# 说明：
# 在上述代码中，两个线程分别获取 `lock1` 和 `lock2`，并尝试获取对方的锁，从而导致死锁。
# 解决死锁的一种方法是使用超时机制或避免嵌套锁。
