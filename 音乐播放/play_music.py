# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 00:08
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : play_music.py
# @Software: PyCharm

import pygame
import time

# 音乐路径
file_path="./res/云烟成雨.flac"

# 初始化
pygame.mixer.init()

# 加载音乐
track=pygame.mixer.music.load(file_path)

# 播放
pygame.mixer.music.play()
# 持续播放
time.sleep(10)
# 暂停
pygame.mixer.music.pause()



pygame.mixer.music.play()
# 停止
pygame.mixer.stop()