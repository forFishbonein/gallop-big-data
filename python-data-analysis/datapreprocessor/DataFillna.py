import pandas as pd
from pymongo import MongoClient
import Connection
from fancyimpute import KNN


def fillnaCity():
    table = Connection.getTable('city')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    df = pd.DataFrame(list(data))
    df = df.interpolate()
    return df

def fillnaCountry():
    table = Connection.getTable('country')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    df = pd.DataFrame(list(data))
    df = df.interpolate()
    return df

def fillnaProvince():
    table = Connection.getTable('province')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    df = pd.DataFrame(list(data))
    df = df.interpolate()
    return df

def test():

    table = Connection.getTable('province')
    collection = list(table.find())
    df = pd.DataFrame(collection)
    df = df.iloc[:, 4:]
    cols = list(df.loc[0:1])

    data = pd.DataFrame(KNN(k=6).fit_transform(df))
    data.columns = cols
    return data

data = test()
print(data)