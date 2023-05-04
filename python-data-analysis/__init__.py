# from bottle import route
from urllib import request

from flask import Flask
from flask_cors import CORS
from dataanalysis import ContrastAnalysis,EveryEvaluation,ProvinceGdpPredict
# from dataanalysis import ContrastAnalysis
from dataquery import IndicatorQuery
from visualization import People,Financial,Employment,ForeignTrade

app = Flask(__name__)
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求


# @app.route('evalution/yearToPro', methods=["GET","OPTIONS"])
# def ProvinceEvaluation(yearToPro):
#     provinceEvalRes = EveryEvaluation.demo(yearToPro)
#     print(provinceEvalRes)
#     return provinceEvalRes

#基于BP神经网络的综合评价：
@app.route('/evaluation/<year>',methods=["GET","POST"])
def evalutionYear(year):
    print(EveryEvaluation.EveryYearEvalution(year))
    return EveryEvaluation.EveryYearEvalution(year)

@app.route('/evaluation/<province>',methods=["GET","POST"])
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
#预测板块---根据具体指标预测GDP（年份＋省份）
# @app.route('/prediction/prvincegdp/<province>',methods=["GET","POST"])
# def getPredictResult(province):
#     return ProvinceGdpPredict.getPredictData(province)

# 具体指标查询
@app.route('/singlequery/<indicator>/<year>/<province>',methods=["GET","POST"])
def getIndictorData(indicator,year,province):
    if indicator is None:
        return IndicatorQuery.getIndicatorAllData("北京市")
    elif year is None and province is None:
        return IndicatorQuery.getIndicatorAllData(indicator),IndicatorQuery.averageYear(indicator)
    elif province is None:
        return IndicatorQuery.getProvinceData(indicator,year)
    elif year is None:
        return IndicatorQuery.getYearData(indicator,province)

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
# @app.route('/contrast/industry')
# def PrimaryContrast():
#     return ContrastAnalysis.PrimaryContrast()


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
@app.route('/visualization/foregintrade/<pro><city>')
def getForegintrade(pro,year):
    return ForeignTrade.getForegintrade(pro,year)

#数据可视化大屏部分----第一产业发展情况

CORS(app, resources=r'/*')
if __name__ == "__main__":
    app.run('localhost','8080')