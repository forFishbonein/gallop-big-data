import pandas as pd
from audioop import avg
import Connection
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql.functions import col



def GdpCity(GDPcity,GDPyear):
    table = Connection.getTable('city')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    # data = pd.read_csv(r'E:\fast_data\data\city.csv',encoding='gbk')
    cols = data[['地区', '年份', '地区生产总值(万元)', '第一产业增加值(万元)', '第二产业增加值(万元)', '第三产业增加值(万元)']]
    indi = cols[cols['地区'] == GDPcity]
    indi = indi[indi['年份'] == GDPyear]
    city_gdp_list = indi.dropna()
    city_gdp_list =city_gdp_list.reset_index(drop=True)
    # print(city_gdp_list)
    resList = city_gdp_list.to_dict(orient='list')
    return resList
# print(GdpCity('北京', 2020))

def TradeBalance(provinceTrade, year):
    # table = Connection.getTable('province')
    # collection = list(table.find())
    # data = pd.DataFrame(collection)
    data = pd.read_csv(r'E:\fast_data\data\province.csv')
    cols = data[['地区', '年份', '经营单位所在地进出口总额', '境内目的地和货源地进出口总额', '外商投资企业进出口总额']]
    indi = cols[cols['地区'] == provinceTrade]
    indi = indi[indi['年份'] == year]
    trade_list = indi.dropna()
    trade_list = trade_list.reset_index(drop=True)
    print(trade_list)
    resList = trade_list.to_dict(orient='list')
    return resList

def HouseholdConsumption(proConsumption):
    # table = Connection.getTable('province')
    # collection = list(table.find())
    # data = pd.DataFrame(collection)
    data = pd.read_csv(r'E:\fast_data\data\province.csv')
    cols = data[['地区', '年份', '居民消费价格指数(上年=100)']]
    indi = cols[cols['地区'] == proConsumption]
    consumption = indi.dropna()
    consumption = consumption.reset_index(drop=True)
    resList = consumption.to_dict(orient='list')
    return resList

def Degree(proDegree):
    table = Connection.getTable('province')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    # data = pd.read_csv(r'E:\fast_data\data\province.csv')
    cols = data[['地区', '年份', '居民消费价格指数(上年=100)']]
    indi = cols[cols['地区'] == proDegree]
    degree = indi.dropna()
    degree = degree.reset_index(drop=True)
    print(degree)
    resList = degree.to_dict(orient='list')
    return resList

def BothSexes(sexesPro):
    table = Connection.getTable('province')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    # data = pd.read_csv(r'E:\fast_data\data\province.csv')
    cols = data[['地区', '年份', '男性人口数(人口抽样调查)','女性人口数(人口抽样调查)','性别比(女=100)(人口抽样调查)']]
    indi = cols[cols['地区'] == sexesPro]
    sexes = indi.dropna()
    sexes = sexes.reset_index(drop=True)
    # print(sexes)
    resList = sexes.to_dict(orient='list')
    return resList

def getJson(scan_list):
    arr = scan_list
    arrSce=np.array(arr)
    # print(arrSce)
    x1list = arrSce[:, 0]
    x2list = arrSce[:, 1]
    x3list = arrSce[:, 2]
    x4list = arrSce[:, 3]
    x5list = arrSce[:, 4]
    x6list = arrSce[:, 5]
    res = []
    for i in range(len(x1list)):
        data = {'城市': x1list[i], '年份':x2list[i], '地区生产总值(万元)':x3list[i], '第一产业增加值(万元)':x4list[i], '第二产业增加值(万元)':x5list[i], '第三产业增加值(万元)':x6list}
        res.append(data)
    # msg="内存溢出"
    resDict={"code": 0, "msg": "", "data": res}
    # print(resDict)
    return resDict