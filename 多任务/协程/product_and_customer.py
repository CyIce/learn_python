# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 08:39
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : product_and_customer.py
# @Software: PyCharm


def product(c):
    c.send(None)
    for i in range(5):
        print("生产者生产了%d" % i)
        data=c.send(str(i))
        print(data)

    c.close()


def consumer():
    data = ""
    while True:
        ret = yield data
        if not ret:
            return
        print("消费者消费了%s" % ret)
        data = "消费成功"


c = consumer()
product(c)