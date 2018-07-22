# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 08:38
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : connect_MySQL.py
# @Software: PyCharm

import pymysql

# 链接数据库
db = pymysql.connect("localhost", "root", "123456789", "python")

# 创建一个cursor对象
cursor = db.cursor()

# sql语句
sql = "select now();"

# 执行sql语句
cursor.execute(sql)

# 获取返回的信息
data = cursor.fetchone()

print(data)

# 断开连接
cursor.close()
db.close()
