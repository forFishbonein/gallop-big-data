import pandas as pd
import Connection

# from pyspark.sql.functions import col

def YearAndProData(indicator):
    # province = spark.sql("select * from province")
    indi = province.select("地区", "年份", indicator).na.drop()
    indi = indi.withColumn('index', col('index').cast('integer')).dropna()
    indi = indi.toPandas().reset_index().to_dict('records')
    return indi

def selectProvince(indicator,province):
    table = Connnection.getTable('province')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    cols = data["地区",'年份',indicator]
    indi = data[data['地区'] == province][cols]
    provinceList = indi.dropna()
    provinceList = provinceList.reset_index()
    del provinceList[provinceList.keys()[0]]
    resList = []
    for i in range(len(provinceList)):
        resList.append(list(provinceList.loc[i]))
    return resList

def selectYear(indicator,year):
    table = Connnection.getTable('province')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    cols = data["地区",'年份',indicator]
    indi = data[data['年份'] == year][cols]
    yearList = indi.dropna()
    yearList = yearList.reset_index()
    del yearList[yearList.keys()[0]]
    resList = []
    for i in range(len(yearList)):
        resList.append(list(yearList.loc[i]))
    return resList


def averageNation(indicator):
    table = Connnection.getTable('city')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    indi = data[["地区",'年份',indicator]].dropna()
    provincelist = indi.groupby(['年份']).mean()
    resList = []
    for i in range(len(provincelist)):
        resList.append(list(provincelist.loc[i]))
    return resList

