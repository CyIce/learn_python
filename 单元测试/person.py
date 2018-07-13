# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 09:46
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : person.py
# @Software: PyCharm


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age + 1
