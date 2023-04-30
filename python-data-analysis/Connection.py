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
    ##限定数据库表，plan
    myTable =  db.provincce
    return myTable

def getCountry():
    db = getDB()
    ##限定数据库表，plan
    myTable =  db.country
    return myTable
# def getCol(tableName,colName):
#     myTable = getTable(tableName)
#     colData = myTable.distinct(colName)
#     return colData

# 读取其中的几列，并将其转化为dataframe对象
# collection = getCity()
# data = []
# for doc in collection.find({},{"_id":0,"年份":1}):
#     # print(doc)
#     data.append(doc)
#     # print(data)
#     # break
# df = pd.DataFrame(data)
# # print(list(table.find()))
# # data = pd.DataFrame(collection)
