# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 09:48
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : class_test_2.py
# @Software: PyCharm

import unittest
from python2与python3的区别.单元测试.person import Person


class Test_2(unittest.TestCase):
    def test_init(self):
        p = Person("CyIce", 20)
        self.assertEqual(p.name, "CyIce", "属性赋值有误")

    def test_get_age(self):
        p = Person("CyIce", 20)
        self.assertEqual(p.get_age(), 20, "age返回错误")


if __name__ == "__main__":
    unittest.main()
