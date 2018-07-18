# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 08:42
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : communication.py
# @Software: PyCharm

from multiprocessing import Process, Queue
import os
import time


def write(queue):
    print("写子进程%s开始" % (os.getpid()))

    for ch in ["A", "B", "C", "D", "E", "F", "G"]:
        queue.put(ch)
        time.sleep(1)

    print("写子进程%s结束" % (os.getpid()))


def read(queue):
    print("读子进程%s开始" % (os.getpid()))

    while True:
        value = queue.get()
        print("value = " + value)

    print("读子进程%s结束" % (os.getpid()))


if __name__ == "__main__":
    print("父进程开始")
    queue = Queue()

    p_write = Process(target=write, args=(queue,))
    p_read = Process(target=read, args=(queue,))
    p_write.start()
    p_read.start()

    p_write.join()
    # 当写进程结束后，强行结束读进程
    p_read.terminate()

    print("父进程结束")
