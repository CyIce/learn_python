# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 07:26
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : client.py
# @Software: PyCharm


import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = "Hello"
    client.sendto(data.encode("UTF-8"), ("127.0.0.1", 8900))
    info = client.recv(1024).decode("UTF-8")
    print("客户端发送：", data.encode("UTF-8"))
    print("客户端收到：", info)
    time.sleep(1)
