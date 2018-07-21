# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 14:11
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : thread_event.py
# @Software: PyCharm


import threading
import time


def func():
    event = threading.Event()

    def run():
        for i in range(5):
            # 阻塞线程
            event.wait()
            # 清除触发事件
            event.clear()
            print(i)

    threading.Thread(target=run).start()
    return event


e = func()

# 触发事件

for i in range(5):
    time.sleep(2)
    e.set()
