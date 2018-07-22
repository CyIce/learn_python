# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 08:45
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : create.py
# @Software: PyCharm

import pymysql

# 链接数据库
db = pymysql.connect("localhost", "root", "123456789", "python")

# 创建一个cursor对象
cursor = db.cursor()

# 检查表是否存在，存在就删除表
cursor.execute("drop table if exists blackboard")

# 创建一个表
sql = "create table blackboard(id int auto_increment primary key,money int not null )"


cursor.execute(sql)

# 断开连接
cursor.close()
db.close()
