# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 07:26
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : server.py
# @Software: PyCharm

import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 8900))

while True:
    data, addr = server.recvfrom(1024)
    server.sendto(data, addr)
    print("服务器收到：", data.decode("UTF-8"))
    print("服务器发送：", data)
    time.sleep(1)
