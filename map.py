#!/usr/bin/python3
# 1
import jieba   #导入jieba库用来进行中文分词
import pymongo   #MongoDB数据库的python驱动包

myclient = pymongo.MongoClient("mongodb://localhost:27017/")    #连接MongoDB
mydb = myclient['bigdata']         #连接名为bigdata的数据库
mycol = mydb['data']               #列名为data的数据库列

data = []                          #创建一个用来读取数据库中的数据的列表变量
for i in mycol.find():             #遍历数据库data列的所有数据
    data.append(i['Content: '])    #添加到data变量中

seg_list = []                      #用来存储分好词之后的数据
for i in data:                     #遍历所有data进行分词
    temp = list(jieba.cut_for_search(i))    #进行中文分词（使用搜索引擎分词模式），并且将它变为list类型
    seg_list.append(temp)                   #将它添加到一个变量中
    for j in temp:                          #输出
        print(j)

