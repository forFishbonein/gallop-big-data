import pandas as pd
import Connnection

def YearAndProData(indicator):
    table = Connnection.getTable('province')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    indi = data[["地区",'年份',indicator]].dropna()
    indi = indi.reset_index()
    del indi[indi.keys()[0]]
    res = []
    for i in range(len(indi)):
        row_dict = indi.loc[i].to_dict()
        res.append(row_dict)
    return res

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

