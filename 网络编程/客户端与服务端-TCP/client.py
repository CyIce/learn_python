# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 17:50
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : client.py
# @Software: PyCharm

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

while True:
    data = input("请输入发送到服务器的数据:")
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("客户端收到：", info.decode("utf-8"))
