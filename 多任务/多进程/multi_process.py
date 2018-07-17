# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 08:10
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : multi_process.py
# @Software: PyCharm


from multiprocessing import Process
from time import sleep
import os


def process_1(times):
    while times > 0:
        times -= 1
        # getpid()获取当前进程的pid
        # getppid()获取当前进程父进程的pid
        print("Process: %s,%s" % (os.getpid(), os.getppid()))
        sleep(1)


def process_2(times):
    while times > 0:
        times -= 1
        print("Process: %s,%s" % (os.getpid(), os.getppid()))
        sleep(1)


if __name__ == "__main__":
    print("Main process", os.getpid())

    # 创建进程
    p_1 = Process(target=process_1, args=(10,))
    p_2 = Process(target=process_2, args=(15,))

    p_1.start()
    p_2.start()

    print("Main process end")
