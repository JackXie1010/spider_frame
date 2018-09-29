# coding: utf8
from model import *
# save as db          ---------------------------------------
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
sess = session()
# save as csv  --------------------------------------------
import os
import pandas as pd
file_list = os.listdir(os.path.abspath(os.path.dirname(__file__)))
# save as mongodb   -----------------------------------------
import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client.Target
table = db.target


#将爬取解析得到的数据：{ 'title': ['a', 'b', 'c'], 'img': ['i', 'ii', 'iii'] }
# 转换为为[{'title': 'a', 'img':'i'}, {}, {}...]
def get_obj_list(data):
    # obj_list = []
    length = 0
    for k in data.keys():
        length = len(data[k]) if length < len(data[k]) else length
    for i in range(length):
        obj = dict()
        for v in data.keys():
            try:
                obj[v] = data[v][i]
            except Exception:
                obj[v] = ''
        # print('obj------', obj)
        yield obj
    #     obj_list.append(obj)
    # return obj_list


def save_as_db(data):
    Model.metadata.create_all(engine)    # 创建   Model 数据库，该名称与model.py 中的class Model 是一致的
    for obj in get_obj_list(data):      # 将所有数据循环存储到表中
        mx = Model(        # sqlalchemy 的 orm 的存储方式
            title=obj['title'],     # title, img 与config.py 文件中的参数的键名是一致的
            img=obj['img'],
        )
        sess.add(mx)
        sess.commit()
    print('----------db-------------')


def save_as_csv(data):   # 数据保存到csv 文件
    # for v in get_obj_list(data):
    save = pd.DataFrame(get_obj_list(data))
    if 'target.csv' in file_list:
        save.to_csv('target.csv', mode='a', header=False, index=False, sep=',')
    else:
        save.to_csv('target.csv',index=False, sep=',')
    print('----------csv-------------')


def save_as_mongodb(data):     # 数据保存到mongodb
    for obj in get_obj_list(data):
        table.insert(obj)
    print('----------mongodb-------------')



