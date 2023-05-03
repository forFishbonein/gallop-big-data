import numpy as np

import pandas as pd
from pymongo import MongoClient
import Connection


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
    collection = Connection.getCity()
    data = []
    for doc in collection.find({},{"_id":0,"地区":1,"年份":1,indicator:1}):
        # print(doc)
        data.append(doc)
    data = pd.DataFrame(data).dropna()
    provinceList = data[data['地区'] == province]
    # provinceList = yearList.dropna()
    provinceList = provinceList.reset_index()
    del provinceList[provinceList.keys()[0]]
    del provinceList[provinceList.keys()[1]]
    resList = []
    for i in range(len(provinceList)):
        resList.append(list(provinceList.loc[i]))
    dictYear={
        "values":resList
    }
    return dictYear

def getProvinceData(indicator,year):
    collection = Connection.getCity()
    data = []
    for doc in collection.find({},{"_id":0,"地区":1,"年份":1,indicator:1}):
        # print(doc)
        data.append(doc)

    data = pd.DataFrame(data).dropna()
    yearList = data[data['年份']==year]
    # print(yearList)
    yearList = yearList.reset_index()
    del yearList[yearList.keys()[0]]
    del yearList[yearList.keys()[0]]
    resList = []
    for i in range(len(yearList)):
        resList.append(list(yearList.loc[i]))
    dictProvince={
        "values":resList
    }
    return dictProvince


def averageYear(indicator):
    collection = Connection.getCity()
    data = []
    for doc in collection.find({},{"_id":0,"地区":1,"年份":1,indicator:1}):
        # print(doc)
        data.append(doc)
        # print(data)
        # break
    indi = pd.DataFrame(data).dropna()
    provincelist = indi.groupby(['年份']).mean()
    provincelist = provincelist.reset_index()
    # print(type(provincelist))
    resList = []
    for i in range(len(provincelist)):
        resList.append(list(provincelist.loc[i]))
    dictYear={
        "values":resList
    }

    return dictYear

def getIndicatorAllData(indicator):
    collection = Connection.getCity()
    data = []
    for doc in collection.find({}, {"_id": 0, "地区": 1, "年份": 1, indicator: 1}):
        data.append(doc)
    indicatorlist = pd.DataFrame(data).dropna()
    indicatorlist = indicatorlist.reset_index()
    del indicatorlist[indicatorlist.keys()[0]]
    resList = []
    for i in range(len(indicatorlist)):
        resList.append(list(indicatorlist.loc[i]))
    dictIndicator={
        "values":resList
    }
    return dictIndicator

# if __name__ == "__main__":

    # re  = getIndicatorAllData("地区生产总值(万元)")
    # print(re)