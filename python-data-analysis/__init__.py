# from bottle import route
from urllib import request

from flask import Flask
from flask_cors import CORS
from dataanalysis import ContrastAnalysis
# from dataanalysis import ContrastAnalysis
from dataquery import IndicatorQuery
app = Flask(__name__)
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
# api = Api(app)

# @app.after_request
# def func_res(resp):
#     res = make_response(resp)
#     res.headers['Access-Control-Allow-Origin'] = '*'
#     res.headers['Access-Control-Allow-Methods'] = 'GET,POST'
#     res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
#     return res


# @app.route('evalution/yearToPro', methods=["GET","OPTIONS"])
# def ProvinceEvaluation(yearToPro):
#     provinceEvalRes = EveryEvaluation.demo(yearToPro)
#     print(provinceEvalRes)
#     return provinceEvalRes
#
# @app.route('evalution/proToYear', methods=["GET","OPTIONS"])
# def ProvinceEvaluation(proToYear):
#     yearEvalRes = EveryEvaluation.demo(proToYear)
#     print(yearEvalRes)
#     return yearEvalRes

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

@app.route('/contrast/province')
def ProvinceAvgGdp():
    print(ContrastAnalysis.getJsonPro())
    return ContrastAnalysis.getJsonPro()

@app.route('/contrast/time')
def TimeAvgGdp():
    print(ContrastAnalysis.TimeContrast())
    return ContrastAnalysis.TimeContrast()


CORS(app, resources=r'/*')
if __name__ == "__main__":
    app.run('localhost','8080')