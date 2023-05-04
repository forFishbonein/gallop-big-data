import json

import numpy as np

import pandas as pd
from pymongo import MongoClient
import Connection
import urllib.parse as urlparse


from pyspark.sql.functions import col
from pyspark.sql import SparkSession

# def YearAndProData(indicator):
#     # province = spark.sql("select * from province")
#     indi = province.select("地区", "年份", indicator).na.drop()
#     indi = indi.withColumn('index', col('index').cast('integer')).dropna()
#     indi = indi.toPandas().reset_index().to_dict('records')
#     return indi

# 读取Excel文件


def getYearData(indicator,province):
    # collection = Connection.getCity()
    # data = []
    # for doc in collection.find({},{"_id":0,"地区":1,"年份":1,indicator:1}):
    #     # print(doc)
    #     data.append(doc)
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,indicator:1})

    data = pd.DataFrame(list(data)).dropna()
    # data = pd.DataFrame(data).dropna()
    provinceList = data[data['地区'] == province]
    # provinceList = yearList.dropna()
    provinceList = provinceList.reset_index()
    del provinceList[provinceList.keys()[0]]
    del provinceList[provinceList.keys()[0]]
    resList = []
    for i in range(len(provinceList)):
        resList.append(list(provinceList.loc[i]))
    dictYear={
        "values":resList
    }
    return json.dumps(dictYear)

def getProvinceData(indicator,year):
    # collection = Connection.getCity()
    # data = []
    # for doc in collection.find({},{"_id":0,"地区":1,"年份":1,indicator:1}):
    #     # print(doc)
    #     data.append(doc)
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({}, {"_id": 0, '地区': 1, '年份': 1, indicator: 1})

    data = pd.DataFrame(data).dropna()
    yearList = data[data['年份']==year]
    # print(yearList)
    yearList = yearList.reset_index()
    del yearList[yearList.keys()[0]]
    del yearList[yearList.keys()[1]]
    print(yearList)
    resList = []
    for i in range(len(yearList)):
        resList.append(list(yearList.loc[i]))
    dictProvince={
        "values":resList
    }
    return json.dumps(dictProvince)


def averageYear(indicator):
    # collection = Connection.getCity()
    # data = []
    # for doc in collection.find({},{"_id":0,"地区":1,"年份":1,indicator:1}):
    #     # print(doc)
    #     data.append(doc)
    #     # print(data)
    #     # break
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,indicator:1})

    indi = pd.DataFrame(list(data)).dropna()
    provincelist = indi.groupby(['年份']).mean()
    provincelist = provincelist.reset_index()
    # print(type(provincelist))
    resList = []
    for i in range(len(provincelist)):
        resList.append(list(provincelist.loc[i]))
    dictYear={
        "values":resList
    }

    return json.dumps(dictYear)

def getIndicatorAllData(indicator):
    # collection = Connection.getCity()
    # data = []
    # for doc in collection.find({}, {"_id": 0, "地区": 1, "年份": 1, indicator: 1}):
    #     data.append(doc)
    db = Connection.getDB()
    mycol = db["province"]
    print(indicator)
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,indicator:1})

    indicatorlist = pd.DataFrame(list(data)).dropna()
    # del indicatorlist[indicatorlist.keys()[0]]
    resList = indicatorlist.values.tolist()
    # indicatorlist = pd.DataFrame(data).dropna()
    # indicatorlist = indicatorlist.reset_index()
    # del indicatorlist[indicatorlist.keys()[0]]
    # resList = []
    # for i in range(len(indicatorlist)):
    #     resList.append(list(indicatorlist.loc[i]))
    dictIndicator={
        "values":resList
    }
    print(dictIndicator)
    return json.dumps(dictIndicator)

# if __name__ == "__main__":
    #
    # re  = getProvinceData("地区生产总值",2018)
    # print(re)