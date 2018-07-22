# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 09:50
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : test_SQL.py
# @Software: PyCharm

from MySQL.cyice_SQL import CyiceSQL

db = CyiceSQL("localhost", "root", "123456789", "python")

res = db.get_all("select * from blackboard where money>500")

for row in res:
    print("%s--%s" % (row[0], row[1]))
