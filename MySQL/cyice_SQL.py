# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 09:34
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : cyice_SQL.py
# @Software: PyCharm

import pymysql


class CyiceSQL():

    def __init__(self, host, user, passwd, db_name):
        """
        :param host: 服务器地址
        :param user: 用户名
        :param passwd: 密码
        :param db_name: 数据库名称
        """
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db_name = db_name
        self.db = None
        self.cursor = None

    def connect(self):
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.db_name)
        self.cursor = self.db.cursor()

    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")

        return res

    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")

        return res

    def insert(self, sql):
        return self._edit(sql)

    def update(self, sql):
        return self._edit(sql)

    def delete(self, sql):
        return self._edit(sql)

    def _edit(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()

        except:
            print("操作失败")
            self.db.rollback()

        return count

    def close(self):
        self.cursor.close()
        self.db.close()
