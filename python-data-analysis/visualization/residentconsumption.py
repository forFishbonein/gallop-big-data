import pandas as pd

#居民消费
def getResidentconsumption(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','最终消费','居民消费','农村居民消费','城镇居民消费']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    print(data1)
    data = data1.to_dict(orient='dict')
    return data

#居民消费水平
def getResidentrate(city,year):
    table = pd.DataFrame(pd.read_csv(r'D:\学习\大三\大三下\实训\data\province.csv'))
    indi = table[['地区','年份','居民消费水平','农村居民消费水平','城镇居民消费水平']].dropna()
    data1 = indi[(indi["地区"]==city)&(indi["年份"]==year)]
    print(data1)
    data = data1.to_dict(orient='dict')
    return data