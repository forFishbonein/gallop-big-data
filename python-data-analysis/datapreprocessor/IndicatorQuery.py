import pandas as pd
import Connection
from pyspark.sql.functions import col
from pyspark.sql import SparkSession

# def YearAndProData(indicator):
#     # province = spark.sql("select * from province")
#     indi = province.select("地区", "年份", indicator).na.drop()
#     indi = indi.withColumn('index', col('index').cast('integer')).dropna()
#     indi = indi.toPandas().reset_index().to_dict('records')
#     return indi

def readDataframe():
    spark = SparkSession.builder.appName("GDP Average").getOrCreate()
    df = spark.read.csv(r"D:\肖红娇\项目\大数据实训\data\province.csv", header=False, inferSchema=True)
    return df
def selectProvince(indicator,province):
    client = MongoClient('mongodb://admin:12345678@121.41.107.144:27017/?authMechanism=DEFAULT&authSource=admin')
    db = client.fastdata
    table = db['province']
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

    #
    # df = readDataframe()
    # # 选择 "地区"、"年份" 和 "indicator" 三列
    # # cols = ["_c1", "_c2", indicator]
    # # indi = df.select(cols).where(col("_c1")==province)
    # indi = df.select("地区", "年份", indicator).where(col("地区") == province)
    # # 删除包含空值的行，并将结果转化为包含嵌套列表的 PySpark DataFrame
    # provinceList = indi.na.drop().rdd.map(lambda row: list(row)).collect()
    # # 展平嵌套列表
    # resList = sum(provinceList, [])
    return resList

def selectYear(indicator,year):
    table = Connection.getTable('province')
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
    table = Connection.getTable('city')
    collection = list(table.find())
    data = pd.DataFrame(collection)
    indi = data[["地区",'年份',indicator]].dropna()
    provincelist = indi.groupby(['年份']).mean()
    resList = []
    for i in range(len(provincelist)):
        resList.append(list(provincelist.loc[i]))
    return resList

if __name__ == "__main__":

    re  = selectProvince("全体居民人均消费支出","北京市")
    print(re)