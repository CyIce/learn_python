# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 08:34
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : map_reduce.py
# @Software: PyCharm

from functools import reduce


# map(fn,lsd)
# 参数1是函数
# 参数2是一个列表


# 将单个字符转化位单个int值
def char_to_int(ch):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[ch]


# 将字符序列转化位整数序列
list_1 = ["1", "2", "0", "7"]
list_2 = list(map(char_to_int, list_1))
print(list_2)

# 将整序列转化位字符序列数
list_3 = list(map(str, list_2))
print(list_3)

# reduce(fn,lsd)
# 参数1为函数，接收两个参数
# 参数2为列表


# 求一个序列的和
list_4 = [1, 2, 3, 4, 5]


# 求两个数的和
def my_sum(x, y):
    return x + y


sum = reduce(my_sum, list_4)

print(sum)


# 将字符串str转化为整型

def str_to_int(s):
    def fc(x, y):
        return x * 10 + y

    lt = list(map(int, s))
    ret = reduce(fc, lt)
    return ret


print(str_to_int("1234"))


# 自定义简单map()

def my_map(func, lsd):
    res_list = []

    for parse in lsd:
        res = func(parse)
        res_list.append(res)
