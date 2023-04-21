import pandas as pd
import Connnection
def fillnaCity():
    table = Connnection.getTable('city')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    df = pd.DataFrame(list(data))
    df = df.interpolate()
    return df

def fillnaCountry():
    table = Connnection.getTable('country')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    df = pd.DataFrame(list(data))
    df = df.interpolate()
    return df

def fillnaProvince():
    table = Connnection.getTable('province')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    df = pd.DataFrame(list(data))
    df = df.interpolate()
    return df


