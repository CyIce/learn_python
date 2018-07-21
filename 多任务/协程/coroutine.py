# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 08:12
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : coroutine.py
# @Software: PyCharm


def run():
    # 空变量，起到存储的作用，始终为空
    data = ""
    ret = yield data
    print(1, ret, data)
    ret = yield data
    print(2, ret, data)
    ret = yield data
    print(3, ret, data)
    ret = yield data


m = run()

# 启动
print(m.send(None))
print(m.send("a"))
print(m.send("b"))
print(m.send("c"))

print("0--------------------0")
