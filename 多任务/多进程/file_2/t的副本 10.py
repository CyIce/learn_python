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
    p_1 = Process(target=process_1, args=(3,))
    p_2 = Process(target=process_2, args=(5,))

    # 把子进程加入队列
    process_list=[]
    process_list.append(p_1)
    process_list.append(p_2)

    for p in process_list:
        p.start()
    for p in process_list:
        # 等待子进程执行完后父进程再执行
        p.join()


    print("Main process end")
