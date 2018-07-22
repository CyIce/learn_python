# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 09:23
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : search.py
# @Software: PyCharm


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

sql = "select * from blackboard where money>500"

try:
    cursor.execute(sql)
    res = cursor.fetchall()

    for row in res:
        print("%s---%s" % (row[0], row[1]))

except Exception:
    pass

# 断开连接
cursor.close()
db.close()
