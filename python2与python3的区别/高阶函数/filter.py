# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 09:08
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : filter.py
# @Software: PyCharm

# filter(func,list）
# 参数1为函数
# 参数2为列表
# 将传入的函数作用于列表的每一个元素，根据返回的是True还是False
# 决定是否保留该元素


# 判断一个数是否是偶数
def func(num):
    if num % 2 == 0:
        return True
    return False


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 保留list_1中的偶数

list_2 = list(filter(func, list_1))

print(list_2)
