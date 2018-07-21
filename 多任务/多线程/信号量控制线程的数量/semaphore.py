# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 18:28
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : semaphore.py
# @Software: PyCharm


import threading
import time

# 定义一个信号量
semaphore = threading.Semaphore(3)


def run():
    with semaphore:
        for i in range(10):
            print("%s--%d" % (threading.current_thread().name, i))
            time.sleep(1)



if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()
