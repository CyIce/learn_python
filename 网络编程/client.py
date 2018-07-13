# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 23:27
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : client.py
# @Software: PyCharm

import socket

# 创建一饿socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
# 阐参数是一个元组("ip",端口号)
sk.connect(("www.sina.com.cn", 80))
# 发送请求
sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收请求
data = []
while True:
    tmp = sk.recv(1024)
    if tmp:
        data.append(tmp)
    else:
        break

data_str = (b''.join(data)).decode('utf-8')

# 断开连接
sk.close()

print(data_str)

headers, HTML = data_str.split("\r\n\r\n", 1)
print(headers)
print(HTML)
