import pandas as pd
import Connection
#国家贸易
def getForegintrade(city,year):
    collection = Connection.getProvince()
    foreginTradeData = []
    for doc in collection.find({}, {"_id": 0, '地区': 1, '年份': 1, '经营单位所在地进出口总额': 1,
                                    '境内目的地和货源地进出口总额': 1,'外商投资企业进出口总额':1}):
        # print(doc)
        foreginTradeData.append(doc)
    data = pd.DataFrame(foreginTradeData).dropna()
    data = data[(data["地区"] == city) & (data["年份"] == year)]
    listForeginTrade = []
    for i in range(len(data)):
        listForeginTrade.append(list(data.loc[i]))
    dictForeginTrade = {
        "value": listForeginTrade
    }
    return dictForeginTrade
