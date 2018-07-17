# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 10:04
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : test.py
# @Software: PyCharm

from 多任务.二次封装进程对象.cyice_processing import CyiceProcess


if __name__=="__main__":

    print("父进程启动")

    p=CyiceProcess("Test")

    p.start()
    p.join()

    print("父进程结束")