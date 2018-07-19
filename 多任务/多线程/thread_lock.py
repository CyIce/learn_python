# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 19:18
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : thread_lock.py
# @Software: PyCharm


import threading

# 创建锁对象
lock = threading.Lock()

num = 0


def run(n):
    global num

    for i in range(1000000):
        # 上锁

        lock.acquire()
        num += n
        num -= n
        # 释放锁
        lock.release()


if __name__ == "__main__":
    print("The value of num is ", num)

    thread_1 = threading.Thread(target=run, args=(6,))
    thread_2 = threading.Thread(target=run, args=(8,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("The value of num is ", num)
