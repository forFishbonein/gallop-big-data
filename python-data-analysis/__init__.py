# from bottle import route
from urllib import request

# from ahocorasick import unicode
from flask import Flask
from flask_cors import CORS
from dataanalysis import ContrastAnalysis,EveryEvaluation,ProvinceGdpPredict,CityGdpPredict,EveryIncaditorPredict
# from dataanalysis import ContrastAnalysis
from dataquery import IndicatorQuery,ProvinceNameQuery,indicatorClassification
# from dataquery import IndicatorQuery,ProvinceNameQuery,ProvinceDict
from visualization import People,Financial,Employment,ForeignTrade
# import sys


app = Flask(__name__)
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求


# def receive_chinese_data(chinese_data):
#     u_data = unicode(chinese_data, "utf-8")
#     utf8_data = u_data.encode("utf-8")

# @app.route('evalution/yearToPro', methods=["GET","OPTIONS"])
# def ProvinceEvaluation(yearToPro):
#     provinceEvalRes = EveryEvaluation.demo(yearToPro)
#     print(provinceEvalRes)
#     return provinceEvalRes

#基于BP神经网络的综合评价：
@app.route('/evaluation/year/<year>',methods=["GET","POST"])
def evalutionYear(year):
    year = int(year)
    print(EveryEvaluation.EveryYearEvalution(year))
    return EveryEvaluation.EveryYearEvalution(year)

@app.route('/evaluation/pro/<province>',methods=["GET","POST"])
def evalutionProvince(province):
    print(EveryEvaluation.EveryProvinceEvalution(province))
    return EveryEvaluation.EveryProvinceEvalution(province)
# @app.route('evalution/proToYear', methods=["GET","OPTIONS"])
# def ProvinceEvaluation(proToYear):
#     yearEvalRes = EveryEvaluation.demo(proToYear)
#     print(yearEvalRes)
#     return yearEvalRes

#预测板块---根据省份预测GDP
@app.route('/prediction/prvincegdp/<province>',methods=["GET","POST"])
def getPredictResult(province):
    return ProvinceGdpPredict.getPredictData(province)

#预测板块---根据城市预测GDP
@app.route('/prediction/citygdp/<city>',methods=["GET","POST"])
def CityPredictResult(city):
    return CityGdpPredict.getPredictData(city)

#预测板块---预测具体指标后10年的值：
@app.route('/prediction/indicator/<indicator>',methods=["GET","POST"])
def IndicatorPredict(indicator):
        return EveryIncaditorPredict.IndicatorPrediction(indicator)

# 具体指标查询
@app.route('/singlequery/alldata/<indicator>',methods=["GET","POST"])
def IndictorData(indicator):
    # u_data = unicode(indicator, "utf-8")
    # indicator = u_data.encode("utf-8")
    return IndicatorQuery.getIndicatorAllData(indicator)

@app.route('/singlequery/avgdata/<indicator>',methods=["GET","POST"])
def IndictorAvgData(indicator):
    return IndicatorQuery.averageYear(indicator)

@app.route('/singlequery/year/<indicator>/<year>',methods=["GET","POST"])
def IndictorProvinceData(indicator,year):
    year = int(year)
    return IndicatorQuery.getProvinceData(indicator,year)

@app.route('/singlequery/pro/<indicator>/<province>',methods=["GET","POST"])
def IndictorYearData(indicator,province):
    return IndicatorQuery.getYearData(indicator, province)
# @app.route('/singlequery/<indicator>/<year>/<province>',methods=["GET","POST"])
# def getIndictorData(indicator,year,province):
#     if indicator is None:
#         return IndicatorQuery.getIndicatorAllData("北京市")
#     elif year is None and province is None:
#
#     elif province is None:
#         return IndicatorQuery.getProvinceData(indicator,year)
#     elif year is None:

# 对比部分--地区，行业，时间对比
@app.route('/contrast/province')
def ProvinceAvgGdp():
    print(ContrastAnalysis.getJsonPro())
    return ContrastAnalysis.getJsonPro()

@app.route('/contrast/time')
def TimeAvgGdp():
    print(ContrastAnalysis.TimeContrast())
    return ContrastAnalysis.TimeContrast()
@app.route('/contrast/primary')
def PrimaryContrast():
    return ContrastAnalysis.PrimaryContrast()
@app.route('/contrast/industry')
def IndustryContrast():
    return ContrastAnalysis.IndustryContrast()


# 数据可视化大屏部分----人口情况
@app.route('/visualization/people/peoplebirth')
def getPeopleBirth():
    return People.getPeopleBirth()

@app.route('/visualization/people/peoplesex')
def getPeopleSex():
    return People.getPeopleSex()

@app.route('/visualization/people/peopleurban')
def getPeopleUrban():
    return People.getPeopleUrban()

@app.route('/visualization/people/peopleeducation')
def getPeopleEducation():
    return People.getPeopleEducation()

#  数据可视化大屏部分----消费情况
@app.route('/visualization/financial/consumpution')
def getConsumption():
    return Financial.getConsumption()
#  数据可视化大屏部分----财政情况

# @app.route('/visualization/financial/financialpay')
# def getFinancialPay():
#     return Financial.getFinancialpay()

@app.route('/visualization/financial/financialtax/<pro>')
def getFinancialTax(pro):
    return Financial.getFinancialtax(pro)

# #  数据可视化大屏部分----就业情况
@app.route('/visualization/employment/employment')
def getEmployment():
    return Employment.getEmployment()

# @app.route('/visualization/employment/unemployment')
# def getUnemployment():
#     return Employment.getUnemployment()

#数据可视化大屏部分----外贸交易情况
@app.route('/visualization/foregintrade/<pro>/<city>')
def getForegintrade(pro,year):
    return ForeignTrade.getForegintrade(pro,year)

#数据可视化大屏部分----第一产业发展情况


@app.route('/query/provincelist')
def GetProvinceList():
    return ProvinceNameQuery.GetProvinceName()

@app.route('/query/provinceinterpreter')
def GetProvinceDict():
    return ProvinceDict.GetProvinceDict()

@app.route('/query/listpage/<indicator>/<page_size>/<page_number>')
def GetIndicatorListPage(indicator,page_size,page_number):
    page_size = int(page_size)
    page_number = int(page_number)
    return indicatorClassification.getProvinceByIndicatorPage(indicator,page_size,page_number)

@app.route('/query/listpage/<indicator>')
def GetIndicatorList(indicator):
    return indicatorClassification.getProvinceByIndicator(indicator)

CORS(app, resources=r'/*')
if __name__ == "__main__":
    app.run('localhost','8080')