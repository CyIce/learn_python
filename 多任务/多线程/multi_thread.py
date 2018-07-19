# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 17:34
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : multi_thread.py
# @Software: PyCharm


import threading
import time

a = 10


def run(num):
    print("子线程（%s）启动" % (threading.current_thread().name))

    time.sleep(2)
    print(a)
    print(num)

    print("子线程（%s）结束" % (threading.current_thread().name))


if __name__ == "__main__":
    print("主线程（%s）启动" % (threading.current_thread().name))

    thread = threading.Thread(target=run, name="run_thread", args=(1,))
    thread.start()
    thread.join()
    print("主线程（%s）结束" % (threading.current_thread().name))
