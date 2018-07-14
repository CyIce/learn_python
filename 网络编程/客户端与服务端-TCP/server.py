# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 17:51
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : server.py
# @Software: PyCharm

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8080))
# 设置监听
server.listen(5)
print("服务器启动成功")

client_socket, client_address = server.accept()
print("连接成功")

while True:
    data = client_socket.recv(1024)
    print("服务器收到：" + data.decode("utf-8"))
    client_socket.send(data)
