# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 09:18
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : sorted.py
# @Software: PyCharm

# 普通排序
list_1 = [4, 5, 8, 4, 2, 5, 6, 8, 4]
list_2 = sorted(list_1)
list_3 = sorted(list_1, reverse=True)

print(list_2)
print(list_3)

# 按绝对值大小排序
list_4 = [4, -5, 8, -4, 2, 5, -1, 6, 8, 4]
list_5 = sorted(list_3, key=abs)
print(list_4)

list_6 = ['a', 't', 's', 'p']
list_7 = sorted(list_6)
print(list_7)
# 按字符串的长度排序
list_8 = ["11", "3444", "777g"]
list_9 = sorted(list_8, key=len)

print(list_9)


def my_len(l):
    return len(l)


list_10 = sorted(list_8, key=my_len)

print(list_10)
