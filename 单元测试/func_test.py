# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 09:30
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : func_test.py
# @Software: PyCharm

import unittest

from .my_func import my_sum_1, my_sum_2


class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试")

    def tearDown(self):
        print("结束测试")

    # 测试
    def test_my_sum(self):
        self.assertEqual(my_sum_1(1, 2), 3, "my_sum_1加法错误")
        self.assertEqual(my_sum_2(1, 2), 3, "my_sum_2加法错误")


if __name__ == "__main__":
    unittest.main()
