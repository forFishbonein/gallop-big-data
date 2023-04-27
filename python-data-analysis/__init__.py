# from bottle import route
from flask import Flask, make_response
from flask_cors import CORS
from google.protobuf.api_pb2 import Api
from  datapreprocessor import IndicatorQuery as dsq
from dataanalysis import EveryEvaluation as epe
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

@app.route('/sd/<indicatorName>', methods=["GET","OPTIONS"])
def indYearAndProvince(indicatorName):
    # print(usrNo)
    resData = dsq.YearAndProData(indicatorName)
    print(resData)
    return resData

@app.route('evalution/yearToPro', methods=["GET","OPTIONS"])
def ProvinceEvaluation(yearToPro):
    provinceEvalRes = epe.demo(yearToPro)
    print(provinceEvalRes)
    return provinceEvalRes

@app.route('evalution/proToYear', methods=["GET","OPTIONS"])
def ProvinceEvaluation(proToYear):
    yearEvalRes = epe.demo(proToYear)
    print(yearEvalRes)
    return yearEvalRes
# def sce2():
#
#     return "ok"

CORS(app, resources=r'/*')
if __name__ == "__main__":
    app.run('localhost','8080')