import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import BPNN
# from sklearn import metrics
# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import mean_squared_error
# from sklearn import preprocessing
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col
from pyspark.sql.types import *
from pyspark.sql.functions import *
import json
from pyspark.sql.functions import array
import Connection


# 定义DataFrame的schema
schema = StructType([
    StructField("province", StringType(), True),
    StructField("year", IntegerType(), True),
    StructField("gdp", FloatType(), True)])

def readData():
    spark = SparkSession.builder.appName("GDP Average").getOrCreate()
    df = spark.read.csv("data\province.csv", header=False, inferSchema=True)
    return df
def readDataframe():
    # collection = Connection.getCity()
    # data = []
    # for doc in collection.find({},{"_id":0,"地区":1,"年份":1,"地区生产总值":1}):
    #     # print(doc)
    #     data.append(doc)
    # data = pd.DataFrame(data).dropna()
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,
                                    '地区生产总值': 1})

    data = pd.DataFrame(list(data)).dropna()
    # spark = SparkSession.builder.appName("GDP Average").getOrCreate()
    data.columns = ["province","year","gdp"]
    return data

def TimeContrast():
    # spark = SparkSession.builder.appName("GDP Average").getOrCreate()
    df = readData()
    df = df.selectExpr("_c1 as province", "_c2 as year", "_c51 as gdp")
    # df = df.orderBy(["provrince", "year"], ascending=[True, True])
    # df = df.groupBy("province").agg(avg("gdp").alias("average_gdp"))
    eastern_provinces = ["上海市", "江苏省", "浙江省", "福建省", "山东省", "广东省", "海南省"]
    central_provinces = ["河南省", "湖北省", "湖南省", "江西省", "安徽省"]
    western_provinces = ["陕西省", "甘肃省", "青海省", "宁夏回族自治区", "新疆维吾尔自治区", "西藏自治区", "四川省",
                     "云南省", "贵州省", "重庆市"]
    def group_data_to_array(province_list):
        disdata = df.filter(col("province").isin(province_list)) \
            .groupBy("province", "year") \
            .agg(avg(col("gdp")).alias("gdp_avg")) \
            .orderBy("year")

        # disdata = df.filter(col("province").isin(province_list)) \
        #     .groupBy("province") \
        #     .agg(collect_list(col("average_gdp")).alias("gdp_array"))
        gdp_sum = disdata.groupBy("year").agg(sum("gdp_avg").alias("gdp_sum"))
        # 将 column1 和 column2 合并为一个数组列
        array_col = array("year", "gdp_sum")
        # 将数组列拆分为两列
        df_with_array = gdp_sum.select(array_col.alias("data")).selectExpr("data[0] as year", "data[1] as gdp")
        # 使用 collect() 方法将 DataFrame 收集到 Driver 中
        data_array = df_with_array.collect()
        # 将 DataFrame 转化为二维数组
        result = [[row[column] for column in range(2)] for row in data_array]

        return result
    # 构建中西东部地区的二维数据
    eastern_avg = group_data_to_array(eastern_provinces)
    central_avg = group_data_to_array(central_provinces)
    western_avg = group_data_to_array(western_provinces)


    # 将DataFrame转换为json字符串
    def dataframe_to_json(df):
        return df.toJSON().collect()

    # 将DataFrame转换为json文件，每个二维数组为一个value

    def save_data_to_json(eastern_data, central_data, western_data):
        data_dict = {
            "eastern_data": eastern_avg,
            "central_data": central_avg,
            "western_data": western_avg
        }
        return data_dict

    return save_data_to_json(eastern_avg, central_avg, western_avg)



def ProvinceContrast():
# 创建SparkSession
#     spark = SparkSession.builder.appName("GDP Average").getOrCreate()
    # 读取CSV文件
    # df = readDataframe()
    # print(df)
    # 转换列名
    df = readData()
    df = df.selectExpr("_c1 as province", "_c2 as year", "_c51 as gdp")
    result = df.groupBy("province").agg(round(avg("gdp"), 2).alias("average_gdp"))

    # result = df.groupby("province").agg(avg(col("gdp").cast("int")).alias("average_gdp"))

    result_array = result.collect()

    result_array.remove(result_array[5])
    # print("Result array: ", result_array)
    result_array = [[row[column] for column in range(2)] for row in result_array]
    # result_array = [[row[0],round(row[1])]for row in result_array]
    return  result_array


def getJsonPro():
    arr=ProvinceContrast()
    arrSce=np.array(arr)
    # print(arrSce)
    x1list=arrSce[:,0]
    x2list=arrSce[:,1]

    res=[]
    for i in range(len(x1list)):
        data={'province':x1list[i],'GDP':x2list[i]}
        res.append(data)
    # msg="内存溢出"
    resDict={"code":0,"msg":"","data":res}
    # print(resDict)
    return json.dumps(resDict)

def PrimaryContrast():
    # db = Connection.getDB()
    # mycol = db["province"]
    # data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,
    #                                 '第一产业增加值': 1,'第二产业增加值':1,"第三产业增加值":1})
    PrimaryData = pd.read_csv("data\province.csv")
    # PrimaryData = pd.DataFrame(list(data)).dropna()
    firstPrimaryList = PrimaryData[["地区","年份","第一产业增加值"]].dropna()

    # firstPrimaryList = PrimaryData[["地区","年份","第一产业增加值"]]
    firstPrimaryList = firstPrimaryList[firstPrimaryList["年份"] >= 2010].values.tolist()
    print(firstPrimaryList)
    secondPrimaryList = PrimaryData[["地区","年份","第二产业增加值"]].dropna()
    secondPrimaryList = secondPrimaryList[secondPrimaryList["年份"] >= 2010].values.tolist()
    print(secondPrimaryList)
    # thirdPrimaryData = PrimaryData[["地区", "年份", "第三产业增加值"]].values.tolist()
    thirdPrimaryList = PrimaryData[["地区", "年份", "第三产业增加值"]].dropna()
    thirdPrimaryList = thirdPrimaryList[thirdPrimaryList["年份"] >= 2010].values.tolist()
    print(thirdPrimaryList)
    dictPrimary = {
        "firstPrimary":firstPrimaryList,
        "secondPrimary":secondPrimaryList,
        "thirdPrimary":thirdPrimaryList
    }
    # print(dictPrimary)
    return json.dumps(dictPrimary)

def IndustryContrast():
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,
                                    '农林牧渔业增加值': 1,'工业增加值':1,"建筑业增加值":1,"批发和零售业增加值":1,"交通运输、仓储和邮政业增加值":1,"住宿和餐饮业增加值":1,
                          "金融业增加值":1,"房地产业增加值":1,"其他行业增加值":1})

    industryData = pd.DataFrame(list(data)).dropna()
    agricultureList = industryData[["地区","年份","农林牧渔业增加值"]].values.tolist()
    industryList = industryData[["地区","年份","工业增加值"]].values.tolist()
    constructionList = industryData[["地区", "年份", "建筑业增加值"]].values.tolist()
    retailList = industryData[["地区", "年份", "批发和零售业增加值"]].values.tolist()
    transportationList = industryData[["地区", "年份", "交通运输、仓储和邮政业增加值"]].values.tolist()
    restaurantList = industryData[["地区", "年份", "住宿和餐饮业增加值"]].values.tolist()
    financeList = industryData[["地区", "年份", "金融业增加值"]].values.tolist()
    realEstateList = industryData[["地区", "年份", "房地产业增加值"]].values.tolist()
    otherList = industryData[["地区", "年份", "其他行业增加值"]].values.tolist()

    dictPrimary = {
        "agriculture":agricultureList,
        "industry":industryList,
        "construction":constructionList,
        "retail": retailList,
        "transportation": transportationList,
        "restaurant": restaurantList,
        "finance": financeList,
        "realEstate": realEstateList,
        "other": otherList,
    }
    return json.dumps(dictPrimary)

if __name__ == '__main__':
    # data = PrimaryContrast()
    print(PrimaryContrast())
    # print(TimeContrast())


