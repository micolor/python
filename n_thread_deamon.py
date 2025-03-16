# 守护线程
# 守护线程是指在主线程结束后自动结束的线程。它们通常用于在后台执行一些不重要的任务。
# 可以通过设置线程的 daemon 属性为 True 来将其设置为守护线程。
# 守护线程的一个常见用途是执行后台任务，例如日志记录、监控等。

import threading
import time

def background_task():
    # 这是一个后台任务函数，它会一直运行，直到主线程结束
    while True:
        print("后台任务正在运行...")
        time.sleep(1)

# 创建一个线程并将其设置为守护线程
daemon_thread = threading.Thread(target=background_task)
daemon_thread.daemon = True  # 设置为守护线程
daemon_thread.start()  # 启动线程

# 主线程执行一些任务
for i in range(5):
    print("主线程正在运行...")
    time.sleep(2)

print("主线程结束，守护线程也将结束。")

