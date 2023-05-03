import pandas as pd

#农业生产情况
def getAgri_product(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','粮食产量','粮食单位面积产量','农作物总播种面积','粮食作物播种面积','农业机械总动力']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    data = data1.to_dict(orient='dict')
    return data

#农业受灾情况
def getAgri_disaster(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','农作物受灾面积','农作物绝收面积']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    data = data1.to_dict(orient='dict')
    return data

#林业发展情况
def getForestry(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','林业用地面积','森林面积','人工林面积','森林覆盖率']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    data = data1.to_dict(orient='dict')
    return data


#畜牧业发展情况
def getHusbandry(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','草原总面积','大牲畜年底头数','肉类产量','家禽出栏量']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    data = data1.to_dict(orient='dict')
    return data

#渔业发展情况
def getFishery(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','水产品总产量','水产品养殖面积','捕捞产量','养殖产量']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    data = data1.to_dict(orient='dict')
    return data