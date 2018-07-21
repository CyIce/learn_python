# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 09:57
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : cyice_processing.py
# @Software: PyCharm

from multiprocessing import Process
from time import sleep
from os import getpid


class CyiceProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程(%s--%s)启动" % (self.name, getpid()))
        sleep(3)
        print("子进程(%s--%s)结束" % (self.name, getpid()))
