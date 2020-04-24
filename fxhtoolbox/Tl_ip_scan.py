#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import threading
import os
import platform

global unreach_list,reach_list,platOS

unreach_list=list()  #保存无法ping通的ip list
reach_list=list()   #保存可以ping通的ip list

#根据不同的OS，调用不同的命令语句
def is_reacheable(ip):
    backinfo = subprocess.os.system('ping -n 1 -w 1 %s >nul' % ip)  # 实现pingIP地址的功能，-n1指发送报文一次，-w1指等待1毫秒

    if backinfo:  # 返回值非0，代表无法pingt通
        unreach_list.append(ip)
    else:  # 返回值为0，代表pingt通
        reach_list.append(ip)

def Tl_ip_scan(ip_list):
    threads = []
    for line in ip_list:
         thr = threading.Thread(target=is_reacheable, args=(line,))
         thr.start()
         threads.append(thr)

    for thr in threads:
        thr.join()
    return reach_list,unreach_list
