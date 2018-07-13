# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 10:16
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : document_test.py
# @Software: PyCharm

import doctest


def my_sum(x, y):
    """

    :param x: 加数
    :param y: 加数
    :return: 两个数的和

    example
    >>> print(my_sum(1,2))
    3
    """

    return x + y + 1


print(my_sum(1, 2))

doctest.testmod()
