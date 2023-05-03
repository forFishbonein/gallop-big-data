import pandas as pd
from pymongo import MongoClient
import pymongo
# 读取Excel文件
def getDB():
    client = MongoClient('mongodb://admin:12345678@47.93.250.53:27017/?authMechanism=DEFAULT&authSource=admin')
    db = client.fastdata
    return db
def getCity():
    db = getDB()
    ##限定数据库表，plan
    myTable =  db.city
    return myTable

def getProvince():
    db = getDB()
    #限定数据库表，plan#
    # client = MongoClient('mongodb://admin:12345678@47.93.250.53:27017/?authMechanism=DEFAULT&authSource=admin')
    # db = client.fastdata
    mycol = db["province"]
    data = mycol.find({},{"_id":0,"行政区划代码":1,"年份":1,"地区生产总值":1})
    df = pd.DataFrame(list(data))
    print(df)
    return df

def getCountry():
    db = getDB()
    ##限定数据库表，plan
    myTable =  db.country
    return myTable
# def getCol(tableName,colName):
#     myTable = getTable(tableName)
#     colData = myTable.distinct(colName)
#     return colData
# client = MongoClient('mongodb://admin:12345678@47.93.250.53:27017/?authMechanism=DEFAULT&authSource=admin')
# db = client.fastdata
# mycol = db["province"]
# data = mycol.find({},{"_id":0,"年份":1})
# df = pd.DataFrame(list(data))
# print(df)
getProvince()
# 读取其中的几列，并将其转化为dataframe对象
# collection = getProvince()
# data = []
# for doc in collection.find({},{"_id":0,"年份":1}):
#     # print(doc)
#     data.append(doc)
# print(data)

# for doc in collection.find({},{"_id":0,"年份":1}):
#     print(doc)
#     print("--------------")
#     data.append(doc)
# print(data)
#     # break
# df = pd.DataFrame(data)
# # print(list(table.find()))
# # data = pd.DataFrame(collection)
