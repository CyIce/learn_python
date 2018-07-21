# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 14:29
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : thread_control.py
# @Software: PyCharm

import threading
import time

# 线程条件变量
cond = threading.Condition()


def run_1():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            # 阻塞当前线程
            cond.wait()
            # 通知其他线程执行
            cond.notify()


def run_2():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.notify()
            cond.wait()


threading.Thread(target=run_1).start()
threading.Thread(target=run_2).start()
