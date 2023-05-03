import pandas as pd

#采矿业
def getMining(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','焦炭生产量','原油生产量','焦炭消费量','原油消费量','石油加工及炼焦业投资']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    data = data1.to_dict(orient='dict')
    return data

#制造业
def getProduction(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','产品质量合格率','产品质量合格品率','出入境货物检验检疫批次','出入境货物检验检疫不合格批次']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    data = data1.to_dict(orient='dict')
    return data

#建筑业
def getConstruction(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','建筑业企业利税总额合计','建筑业企业利税总额合计','建筑业企业利润总额']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    data = data1.to_dict(orient='dict')
    return data

