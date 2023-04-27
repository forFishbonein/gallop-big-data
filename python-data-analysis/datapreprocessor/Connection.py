
from pymongo import MongoClient
import pymongo
# 读取Excel文件
def getDB():
    client = MongoClient('mongodb://admin:12345678@121.41.107.144:27017/?authMechanism=DEFAULT&authSource=admin')
    db = client.template
    return db

def getTable(tableName):
    db = getDB()
    ##限定数据库表，plan
    myTable = db[tableName]
    return myTable

def getCol(tableName,colName):
    myTable = getTable(tableName)
    colData = myTable.distinct(colName)
    return colData