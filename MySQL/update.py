# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 09:20
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : update.py
# @Software: PyCharm

import pymysql

# 链接数据库
db = pymysql.connect("localhost", "root", "123456789", "python")

# 创建一个cursor对象
cursor = db.cursor()

sql = "update blackboard set money=1000 where id=1"

try:
    cursor.execute(sql)
    db.commit()
except Exception:
    db.rollback()

# 断开连接
cursor.close()
db.close()
