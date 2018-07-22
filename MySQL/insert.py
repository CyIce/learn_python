# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 08:49
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : insert.py
# @Software: PyCharm


import pymysql

# 链接数据库
db = pymysql.connect("localhost", "root", "123456789", "python")

# 创建一个cursor对象
cursor = db.cursor()

sql = "insert into blackboard values (0,100),(0,200),(0,300),(0,400),(0,600),(0,910)"

try:
    cursor.execute(sql)
    db.commit()
except Exception:
    db.rollback()


# 断开连接
cursor.close()
db.close()
