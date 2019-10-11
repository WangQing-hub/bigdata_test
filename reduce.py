#!/usr/bin/python3

from collections import Counter     #用来计数的类
import operator         #用来进行字典按值排序的相关包
import sys              #导入sys模块，用来获取标准输入

data=[]                 #创建存储从标准输入中获取的值
for line in sys.stdin:          #从标准输入中获取值
    line = line.strip('\n')     #去除输入数据中的换行符
    data.append(line)           #添加到data中

c = Counter(data)               #进行data数据计数
c1 = sorted(c.items(), key=operator.itemgetter(1),reverse=True)     #字典排序
for i,j in c1:      #遍历最终排好序的字典类型输出
    print(i,j)      
