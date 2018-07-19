# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 18:59
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : barrier.py
# @Software: PyCharm

import threading
import time

barrier = threading.Barrier(3)


def run():
    print("%s--start" % (threading.current_thread().name))
    time.sleep(1)
    barrier.wait()
    print("%s--end" % (threading.current_thread().name))


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()
