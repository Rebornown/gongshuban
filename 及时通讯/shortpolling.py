# 短轮询
"""
传统的通讯模式，不定时发出请求
效率低:轮询的请求间隔时间一般是固定的，无论服务器是否有新的数据，都需要等待一段固定的时间。当数据更新的频率较低时，大部分请求都是无效的;
实时性差:如果数据在两次请求间发生了更新，那么用户只能在下一次轮询时才能得到最新数据;
浪费资源:高频率的操作功能，或者页面访问，导致的大量用户使用轮询时，会占用大量的网络资源，降低整
体网络速度
"""
import sys 
sys.path.append('../settings')

from settings.packages import *
# import time

def poll_task():
    # 任务
    print("Polling task is run")

while True:
    poll_task()
    time.sleep(5)