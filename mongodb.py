import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['bigdata']

with open('data.txt',encoding='utf-8') as f:
    data = f.readlines()
    
mycol = mydb['data']
data_all=[]
temp={}
for i in data:
    if i == '\n':
        data_all.append(temp)
        temp={}
    i=i.strip('\n')
    if i[:10] == 'Nickname: ':
        i=i.strip('Nickname: ')
        temp['Nickname: ']=i
    if i[:9] == 'Content: ':
        i=i.strip('Content: ')
        temp['Content: ']=i
    if i[:6] =='date: ':
        i=i.strip('date: ')
        temp['date: ']=i

mycol.insert_many(data_all)

# import jieba
# from collections import Counter
# data_all=[]
# temp={}
# seg_list = []
# for i in data:
#     if i == '\n':
#         data_all.append(temp)
#         temp={}
#     i=i.strip('\n')
    
#     if i[:9] == 'Content: ':
#         i=i.strip('Content: ')
#         temp['Content: ']=i
#         seg_list.append(list(jieba.cut_for_search(i)))

# c = Counter(sum(seg_list, []))