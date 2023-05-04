import json

import numpy as np

import pandas as pd
from pymongo import MongoClient
import Connection

def GetProvinceName():

    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({}, {"_id": 0, '地区': 1})
    data = pd.DataFrame(list(data)).dropna()
    data = data.groupby("地区").count()
    provinceName = data.reset_index()
    # del provinceName[provinceName.keys()[0]]
    provinceNameList = []
    for i in range(len(provinceName)):
        provinceNameList.append(provinceName["地区"][i])
    # provinceName = provinceName.values.tolist()
    dictProvinceName ={
        "values":provinceNameList
    }
    return dictProvinceName
