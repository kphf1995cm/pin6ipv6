#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 运行格式: ./thread.py host.csv a b c d
# host.csv:存放待测主机名
# a:下一个执行的curl行号
# b:下一个执行的taceroute行号
# c:下一个执行的ping行号
# d:线程个数

import threading
import datetime
import os
import time
import sys
import pycurl
import multiprocessing
import re 
#import commands
import subprocess
import csv

import linecache

line=0
a=0
b=0
c=0
d=0
line1=0
line2=0
line3=0


writer=open("result.csv","w")
class Test:
    def __init__(self):
        self.contents = ''
    def body_callback(self,buf):
        self.contents = self.contents + str(buf)



def  pingurl(url):
    cmd = 'ping6 -c 1 %s' % (url)
    try:
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        p.wait()
    except p.error as e:
        return
    line = []
    line.append(url)
    record = p.stdout.readline()
    print(record)
    if not record or len(record) == 0:
        return
    else:

        while True:
            record = p.stdout.readline()
            print(record)
            if not record or len(record) == 0:
                break

            if ('Destination unreachable' in str(record)):
                #writer.writelines(url+',0\n')
                #writer.flush()
                break;
            elif('ttl' in str(record)):
                writer.writelines(url + '\n')

                writer.flush()

                break;








if __name__ == '__main__':

    #设置生成文件路径
    record_path="./result1106/" 
    #####
    filename = 'target.txt'


    with open(filename, 'r') as f:
        list1 = f.readlines()

    for row in list1:
        row1=''
        for i in range(0,len(row)-1):
            if(i%4==0 and i!=0 and i!=len(row)-2):
                row1+=":"
            row1+=row[i]

        print(row1)
        pingurl(row1)
