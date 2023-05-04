import pandas as pd
import Connection
import json

def getProvinceTable():
    collection = Connection.getProvince()
    data = []
    for doc in collection.find():
        # print(doc)
        data.append(doc)
    data = pd.DataFrame(data).dropna()
    return data

#出生率死亡率
def getPeopleBirth():
    collection = Connection.getProvince()
    peopleData = []
    for doc in collection.find({},{"_id":0,"地区":1,'年份':1,'人口出生率':1,'人口死亡率':1}):
        # print(doc)
        peopleData.append(doc)

    dictPeopleBirth={
        "value":peopleData
    }
    return dictPeopleBirth

#男女人口
def getPeopleSex():
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({}, {"_id": 0, '地区':1,'年份':1,'男性人口数(人口抽样调查)':1,'女性人口数(人口抽样调查)':1})
        # print(doc)
    peopleSexData = pd.DataFrame(list(data)).dropna()
    bjPeopleSexData = peopleSexData[peopleSexData["地区"] == "北京市"]
    bjPeopleSexData = bjPeopleSexData[bjPeopleSexData["年份"] == 2019].values.tolist()
    shPeopleSexData = peopleSexData[peopleSexData["地区"] == "上海市"]
    shPeopleSexData = shPeopleSexData[shPeopleSexData["年份"] == 2019].values.tolist()
    tjPeopleSexData = peopleSexData[peopleSexData["地区"] == "天津市"]
    tjPeopleSexData = tjPeopleSexData[tjPeopleSexData["年份"] == 2019].values.tolist()
    cqPeopleSexData = peopleSexData[peopleSexData["地区"] == "重庆市"]
    cqPeopleSexData = cqPeopleSexData[cqPeopleSexData["年份"] == 2019].values.tolist()
    nmgPeopleSexData = peopleSexData[peopleSexData["地区"] == "内蒙古自治区"]
    nmgPeopleSexData = nmgPeopleSexData[nmgPeopleSexData["年份"] == 2019].values.tolist()
    gxPeopleSexData = peopleSexData[peopleSexData["地区"] == "广西壮族自治区"]
    gxPeopleSexData = gxPeopleSexData[gxPeopleSexData["年份"] == 2019].values.tolist()
    xzPeopleSexData = peopleSexData[peopleSexData["地区"] == "西藏自治区"]
    xzPeopleSexData = xzPeopleSexData[xzPeopleSexData["年份"] == 2019].values.tolist()
    nxPeopleSexData = peopleSexData[peopleSexData["地区"] == "宁夏回族自治区"]
    nxPeopleSexData = nxPeopleSexData[nxPeopleSexData["年份"] == 2019].values.tolist()
    xjPeopleSexData = peopleSexData[peopleSexData["地区"] == "新疆维吾尔自治区"]
    xjPeopleSexData = xjPeopleSexData[xjPeopleSexData["年份"] == 2019].values.tolist()

    dictPeopleSex = {
        "beijing": bjPeopleSexData,
        "shanghai":shPeopleSexData,
        "tianjin":tjPeopleSexData,
        "chongqing":cqPeopleSexData,
        "neimenggu":nmgPeopleSexData,
        "guangxi":gxPeopleSexData,
        "xizang":xzPeopleSexData,
        "ningxia":nxPeopleSexData,
        "xinjiang":xjPeopleSexData
    }

    return json.dumps(dictPeopleSex)

#城乡人口
def getPeopleUrban():
    collection = Connection.getProvince()
    peopleUrbanData = []
    for doc in collection.find({}, {"_id": 0, '地区': 1, '年份': 1, '城镇人口': 1,
                                    '乡村人口': 1}):
        # print(doc)
        peopleUrbanData.append(doc)

    dictPeopleUrban = {
        "value": peopleUrbanData
    }
    return dictPeopleUrban


#人口年龄层次
def getPeopleAge():
    collection = Connection.getProvince()
    peopleAgeData = []
    for doc in collection.find({}, {"_id": 0, '地区': 1, '年份': 1, '人口数(人口抽样调查)': 1,
                                    '0-14岁人口数(人口抽样调查)': 1,'15-64岁人口数(人口抽样调查)':1,'65岁及以上人口数(人口抽样调查)':1}):
        # print(doc)
        peopleAgeData.append(doc)

    dictPeopleAge = {
        "value": peopleAgeData
    }
    return dictPeopleAge


#人口学历层次
def getPeopleEducation():
    collection = Connection.getProvince()
    peopleEducationData = []
    for doc in collection.find({}, {"_id": 0, '地区': 1, '年份': 1, '6岁及6岁以上未上过学人口数(人口抽样调查)': 1,
                                    '6岁及6岁以上小学人口数(人口抽样调查)': 1,'6岁及6岁以上初中人口数(人口抽样调查)':1,'6岁及6岁以上高中人口数(人口抽样调查)':1,'6岁及6岁以上大专及以上人口数(人口抽样调查)':1}):
        # print(doc)
        peopleEducationData.append(doc)

    dictPeopleEducation = {
        "value": peopleEducationData
    }
    return dictPeopleEducation


print(getPeopleSex())
