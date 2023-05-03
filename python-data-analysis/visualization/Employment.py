import pandas as pd
import Connection
#就业人口
def getEmployment():
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,
                                    '城镇就业人数': 1,'城镇私营企业投资者就业人数':1,"乡村私营企业投资者就业人数":1})

    employment = pd.DataFrame(list(data)).dropna()
    yearList = range(2006,2021)
    urbanEmploymentData = employment.groupby("年份")["城镇就业人数"].sum()
    urbanEmploymentData = urbanEmploymentData.values.tolist()

    urbanEmploymentData = [list(i) for i in zip(yearList, urbanEmploymentData)]
    EmploymentData = employment.groupby("年份")["城镇私营企业投资者就业人数"].sum()
    EmploymentData = EmploymentData.values.tolist()
    EmploymentData = [list(i) for i in zip(yearList,EmploymentData)]
    countryEmploymentData = employment.groupby("年份")["城镇私营企业投资者就业人数"].sum()
    countryEmploymentData = countryEmploymentData.values.tolist()
    countryEmploymentData = [list(i) for i in zip(yearList, countryEmploymentData)]
    dicEmployment={
        "urbanEmployment":urbanEmploymentData,
        "employment":EmploymentData,
        "countryEmployment":countryEmploymentData

    }
    return dicEmployment

#失业人口
def getUnemployment():
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({}, {"_id": 0, '地区': 1, '年份': 1, '城镇登记失业人数': 1,
                                    '城镇登记失业率': 1})
    unemploymentData = pd.DataFrame(list(data)).dropna()
    return unemploymentData

print(getEmployment())