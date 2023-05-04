import pandas as pd
import Connection
import json

#国家经济支出
def getFinancialpay():
    collection = Connection.getProvince()
    financialPayData = []
    for doc in collection.find({}, {"_id": 0, '地区': 1, '年份': 1, '政府消费': 1,
                                    '地方财政一般预算支出': 1}):
        # print(doc)
        financialPayData.append(doc)

    dictFinancialPay = {
        "value": financialPayData
    }
    return dictFinancialPay


#国家经济税收
# 待测
def getFinancialtax(city):
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1, '地方财政国内增值税': 1,'地方财政企业所得税':1})
    financialTaxData = pd.DataFrame(list(data)).dropna()
    print(financialTaxData)
    financialTaxData = financialTaxData[financialTaxData["地区"] == city]

    # financialTaxData = financialTaxData[financialTaxData["年份"] == year]
    financialTaxData = financialTaxData.reset_index()[
        [ '年份', '地方财政国内增值税', "地方财政企业所得税"]]
    listFinancialTax = []
    for i in range(len(financialTaxData)):
        listFinancialTax.append(list(financialTaxData.loc[i]))
    dictFinancialTax = {
        "value": listFinancialTax
    }
    return dictFinancialTax

def getConsumption():
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1, '政府消费': 1,'农村居民消费':1,"城镇居民消费":1,
                                    '农村居民消费水平': 1,'城镇居民消费水平':1})
    consumptionData = pd.DataFrame(list(data)).dropna()

    consumptionData = consumptionData.groupby("地区").mean()
    consumptionData = consumptionData.reset_index()[['地区', '政府消费','农村居民消费',"城镇居民消费",'农村居民消费水平','城镇居民消费水平']]
    # print(consumptionData)
    bjConsumptionData = consumptionData[consumptionData["地区"]=="北京市"].values.tolist()
    tjConsumptionData = consumptionData[consumptionData["地区"]=="天津市"].values.tolist()
    shConsumptionData = consumptionData[consumptionData["地区"] == "上海市"].values.tolist()
    cqConsumptionData = consumptionData[consumptionData["地区"] == "重庆市"].values.tolist()
    dictConsumption = {
        "beijing": bjConsumptionData,
        "shanghai":shConsumptionData,
        "tianjin":tjConsumptionData,
        "chongqing":cqConsumptionData
    }
    return json.dumps(dictConsumption)

print(getFinancialtax("河北省"))