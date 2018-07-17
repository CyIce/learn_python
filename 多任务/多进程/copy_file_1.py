# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 09:16
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : copy_file_1.py
# @Software: PyCharm

import os, time


def copy_file(r_path, w_path):
    '''
    拷贝文件
    :param r_path: 需要拷贝的文件路径
    :param w_path: 文件拷贝的地址
    '''
    fr = open(r_path, "rb")
    fw = open(w_path, "wb")
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()
    time.sleep(1)


path = "./file_1"
to_path = "./file_2"

# 获取path路径下所有文件名称
file_list = os.listdir(path)
start_time = time.time()
for file in file_list:
    copy_file(os.path.join(path, file), os.path.join(to_path, file))
end_time = time.time()

print("总耗时%0.2f" % (end_time - start_time))
