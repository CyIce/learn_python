# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 08:27
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : thread_local.py
# @Software: PyCharm


import threading

local = threading.local()
num = 0


def run(x, n):
    x += n
    x -= n


def func(n):
    local.x = num
    for i in range(1000000):
        run(local.x, n)
    print("%s-%d" % ((threading.current_thread()).name, local.x))


if __name__ == "__main__":
    print("The value of num is ", num)

    thread_1 = threading.Thread(target=func, args=(6,))
    thread_2 = threading.Thread(target=func, args=(8,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("The value of num is ", num)
