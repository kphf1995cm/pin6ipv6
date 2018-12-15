#把数据按照序号merge在一起


from __future__ import division
import csv

#from pylab import *  # 支持中文
import sys

def predataping(file):
    file1 = open('target-ping-0.csv', 'r')
    csv_reader1 = csv.reader(file1)
    file2 = open('target-ping-3.csv', 'r')
    csv_reader2 = csv.reader(file2)
    file3 = open('target-ping-6.csv', 'r')
    csv_reader3 = csv.reader(file3)
    file4 = open('target-ping-9.csv', 'r')
    csv_reader4 = csv.reader(file4)
    file5 = open('target-ping-12.csv', 'r')
    csv_reader5 = csv.reader(file5)
    file6 = open('target-ping-15.csv', 'r')
    csv_reader6 = csv.reader(file6)
    file7 = open('target-ping-18.csv', 'r')
    csv_reader7 = csv.reader(file7)
    file8 = open('target-ping-21.csv', 'r')
    csv_reader8 = csv.reader(file8)
    file9 = open('target-ping-24.csv', 'r')
    csv_reader9 = csv.reader(file9)
    file25= open('target-ping-27.csv', 'r')
    csv_reader25 = csv.reader(file25)

    file110 = open('target-ping-1.csv', 'r')
    csv_reader110 = csv.reader(file110)
    file111 = open('target-ping-2.csv', 'r')
    csv_reader111 = csv.reader(file111)
    file112 = open('target-ping-4.csv', 'r')
    csv_reader112 = csv.reader(file112)
    file113 = open('target-ping-5.csv', 'r')
    csv_reader113 = csv.reader(file113)
    file114 = open('target-ping-7.csv', 'r')
    csv_reader114 = csv.reader(file114)
    file115 = open('target-ping-8.csv', 'r')
    csv_reader115 = csv.reader(file115)
    file116 = open('target-ping-10.csv', 'r')
    csv_reader116 = csv.reader(file116)
    file117 = open('target-ping-11.csv', 'r')
    csv_reader117 = csv.reader(file117)
    file118 = open('target-ping-13.csv', 'r')
    csv_reader118 = csv.reader(file118)
    file119 = open('target-ping-14.csv', 'r')
    csv_reader119 = csv.reader(file119)
    file120 = open('target-ping-16.csv', 'r')
    csv_reader120 = csv.reader(file120)
    file121 = open('target-ping-17.csv', 'r')
    csv_reader121 = csv.reader(file121)
    file122 = open('target-ping-19.csv', 'r')
    csv_reader122 = csv.reader(file122)
    file123 = open('target-ping-20.csv', 'r')
    csv_reader123 = csv.reader(file123)
    file124 = open('target-ping-22.csv', 'r')
    csv_reader124 = csv.reader(file124)
    file125 = open('target-ping-23.csv', 'r')
    csv_reader125 = csv.reader(file125)
    file126 = open('target-ping-25.csv', 'r')
    csv_reader126 = csv.reader(file126)
    file127 = open('target-ping-26.csv', 'r')
    csv_reader127 = csv.reader(file127)
    file128 = open('target-ping-28.csv', 'r')
    csv_reader128 = csv.reader(file128)
    file129 = open('target-ping-29.csv', 'r')
    csv_reader129 = csv.reader(file129)


    f = open(file, 'w')
    newline = []
    for row in csv_reader1:
        
        newline.append(row)

    for row in csv_reader2:
        
        newline.append(row)
    for row in csv_reader3:
        newline.append(row)

    for row in csv_reader4:

        newline.append(row)
    for row in csv_reader5:
        newline.append(row)
    for row in csv_reader6:
        newline.append(row)
    for row in csv_reader7:
        newline.append(row)
    for row in csv_reader8:
        newline.append(row)
    for row in csv_reader9:
        newline.append(row)


    for row in csv_reader25:
        newline.append(row)
    for row in csv_reader110:
        newline.append(row)
    for row in csv_reader111:
        newline.append(row)
    for row in csv_reader112:
        line1 = int(row[0])
        newline[line1] = row
    for row in csv_reader113:
        newline.append(row)

    for row in csv_reader114:
        newline.append(row)
    for row in csv_reader115:
        newline.append(row)
    for row in csv_reader116:
        newline.append(row)
    for row in csv_reader117:
        newline.append(row)

    for row in csv_reader118:
        newline.append(row)
    for row in csv_reader119:
        newline.append(row)
    for row in csv_reader120:
        newline.append(row)
    for row in csv_reader121:
        newline.append(row)
    for row in csv_reader122:
        newline.append(row)
    for row in csv_reader123:
        newline.append(row)
    for row in csv_reader124:
        newline.append(row)

    for row in csv_reader125:
        newline.append(row)
    for row in csv_reader126:
        newline.append(row)
    for row in csv_reader127:
        newline.append(row)
    for row in csv_reader128:
        newline.append(row)
    for row in csv_reader129:
        newline.append(row)
    for line in newline:
        f.writelines(line[0] + '\n')
    f.close()

if __name__ == '__main__':
    #对数据进行绘制
    filename = sys.argv[1]
    print(filename)
    predataping(filename)
    #predatatraceroute()
