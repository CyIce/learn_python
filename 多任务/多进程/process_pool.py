# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 08:53
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : process_pool.py
# @Software: PyCharm

from multiprocessing import Process, Pool
import os, time, random


def run(id):
    print("子进程%d启动" % (id))
    start = time.time()
    time.sleep(random.choice([1, 2, 3]))
    end = time.time()
    print("子进程%d结束, 耗时%.2f" % (id, end - start))


if __name__ == "__main__":
    print("父进程启动")

    # 创建一个进程池,大小默认为CPU核心数
    pool = Pool()
    for i in range(8):
        pool.apply_async(run, args=(i,))

    # 在调用join()之前必须调用close()
    pool.close()
    pool.join()

    print("父进程结束")
