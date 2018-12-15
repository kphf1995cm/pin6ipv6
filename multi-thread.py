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
#import pycurl
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



class Test:
    def __init__(self):
        self.contents = ''
    def body_callback(self,buf):
        self.contents = self.contents + str(buf)



def pingurl(url, writer, line3):
    print('scanning ipv6 num',line3)
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
            if('ttl' in str(record)):
                writer.writelines(url + '\n')
                writer.flush()
                break;


def read_row3(lines,lock):
    global line3
    row=""
    liner3=0
    finish=False
    if lock.acquire():
        try:
            if line3-1==len(lines):
                finish=True
            else:
                row=lines[line3-1]
                line3+=1
                liner3=line3
        finally:
            lock.release()
    return finish,row,liner3
def do_something(filename, lock, lines, thread_index):

    if thread_index % 1 == 0:
        output_file = filename[:-4] + "-ping-%s.csv" % thread_index

    f = open(output_file, 'a')
    # row=lines[d-1]



    if thread_index % 1 == 0:
        count2 = 0
        while True:
            (finish, row, liner2) = read_row3(lines, lock)
            if finish:
                f.flush()
                f.close()
                break
            else:
                pingurl(row.strip(), f, liner2 - 1)
                count2 = count2 + 1
                if count2 == 21:
                    f.flush()
                    count2 = 0


if __name__ == '__main__':

    #设置生成文件路径
    record_path="./result1106/" 
    #####
    filename = sys.argv[1]
    lock3 = threading.Lock()
    lock_record = threading.Lock()
    with open(filename, 'r') as f:
        list1 = f.readlines()
    line=[]
    for row in list1:
        row1=''
        for i in range(0,len(row)-1):
            if(i%4==0 and i!=0 and i!=len(row)-2):
                row1+=":"
            row1+=row[i]
        line.append(row1)

    for i in range(30):
        t = threading.Thread(target=do_something, args=(filename, lock3, line, i))
        t.start()
