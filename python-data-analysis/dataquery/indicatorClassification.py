import Connection
import pandas as pd
import json
# def getFirstIndicator():
def getProvinceByIndicatorPage(indicator, page_size, page_number):
    skip_number = (page_number - 1) * page_size
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({}, {"_id": 0, '地区': 1, '年份': 1, indicator: 1}).skip(skip_number).limit(page_size)

    indicatorlist = pd.DataFrame(list(data)).dropna()
    resList = indicatorlist.values.tolist()
    dictIndicator = {
        "values": resList
    }
    print(json.dumps(dictIndicator))
    return json.dumps(dictIndicator)

def getProvinceByIndicator(indicator):
    skip_number = (page_number - 1) * page_size
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({}, {"_id": 0, '地区': 1, '年份': 1, indicator: 1})

    indicatorlist = pd.DataFrame(list(data)).dropna()
    resList = indicatorlist.values.tolist()
    dictIndicator = {
        "values": resList
    }
    print(json.dumps(dictIndicator))
    return json.dumps(dictIndicator)
page_size = 10
page_number = 2
getProvinceByIndicator("地区生产总值")
