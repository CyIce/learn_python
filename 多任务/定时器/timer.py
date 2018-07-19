# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 19:03
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : timer.py
# @Software: PyCharm


import threading


def run():
    print("This thread is running")


if __name__ == '__main__':
    threading.Timer(5, run).start()

    print("主线程结束")
