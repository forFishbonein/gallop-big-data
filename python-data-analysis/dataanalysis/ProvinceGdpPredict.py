# -*- coding: utf-8 -*-
#导入必要的库
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import BPNN
# from sklearn import metrics
# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import mean_squared_error
# from sklearn import preprocessing
import Connection
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
def inverse_transform_col(scaler,y,n_col):
    '''scaler是对包含多个feature的X拟合的,y对应其中一个feature,n_col为y在X中对应的列编号.返回y的反归一化结果'''
    y = y.copy()
    y -= scaler.min_[n_col]
    y /= scaler.scale_[n_col]
    return y

def readDataframe():
    collection = Connection.getCity()
    data = []
    for doc in collection.find({},{"地区":1,"居民消费价格指数(上年=100)":1,"全体居民人均消费支出":1,"规模以上工业企业出口交货值":1,"地区生产总值":1}):
        # print(doc)
        data.append(doc)
    data = pd.DataFrame(data).dropna()
    # spark = SparkSession.builder.appName("GDP Average").getOrCreate()
    return data


    # 读取数据 进行数据预处理
def read_check_data(pro):
    data_before = pd.read_csv("data\province.csv")
    db = Connection.getDB()
    mycol = db["province"]
    data1 = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,
                                    '房地产开发投资额': 1,'经营单位所在地进出口总额':1,"地方财政一般预算收入":1,"地区生产总值":1})

    data1 = pd.DataFrame(list(data1))

    data1 = data1[data1["地区"]==pro]

    # # 输出每个列丢失值
    data = data_before[["地区","年份","房地产开发投资额","经营单位所在地进出口总额","地方财政一般预算收入","地区生产总值"]].dropna()
    # print(data)
    # data = readDataframe()
    data = data[data["地区"]==pro]

    x_first_train = np.array(data['房地产开发投资额'].loc[:15])

    x_second_train = np.array(data['经营单位所在地进出口总额'].loc[:15])
    x_third_train = np.array(data['地方财政一般预算收入'].loc[:15])
    x = list(data["年份"])
    y_income = np.array(data['地区生产总值'].loc[:15])
    x_first_predict = np.array(data['房地产开发投资额'])
    x_second_predict = np.array(data['经营单位所在地进出口总额'])
    x_third_predict = np.array(data['地方财政一般预算收入'])
    # 可视化展示数据
    # plt.title("1992年至今季度国内生产总值与工业、建筑业、交通运输业增加值(万亿元)")
    # plt.plot(x, x_first_train, '.', label='工业增加值')
    # plt.plot(x, x_second_train, '.', label='建筑业增加值')
    # plt.plot(x, x_third_train, '.', label='交通运输业增加值')
    # plt.plot(x, y_income, '.', label='国内生产总值')
    # plt.legend()
    return x_first_train,x_second_train,x_third_train, x_first_predict,x_second_predict, x_third_predict, y_income


# 多元线性回归
def multiple_regression(x_first_train,x_second_train,x_third_train, x_first_predict,x_second_predict, x_third_predict, y_income):
    x1 = range(2005,2021)
    x2 = range(2005,2026)
    Y = y_income.T
    X = np.array([list(x) for x in zip(np.ones(len(y_income)), x_first_train, x_second_train, x_third_train)])

    B = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), Y)
    print("B = ", B)
    # # 多元线性回归模型
    # print("回归方程为 y = %f + %fx1 + %fx2 + %fx3" % (B[0], B[1], B[2], B[3]))
    y_predict = B[0] + B[1] * x_first_predict + B[2] * x_second_predict + B[3] * x_third_predict
    # 可视化
    plt.figure()
    plt.title("国内生产总值与预测值对比图")
    plt.plot(x1, y_income, '*', label='国内生产总值(万亿元)')
    plt.plot(x2, y_predict, '.', label='预测值')
    plt.legend()
    # plt.show()
    return x1,x2,X, B, y_predict


# 检验
def check(y_real, y_predict, X, B):
    y1 = np.sum((y_predict - np.mean(y_real)) ** 2)
    y2 = np.sum((y_real - np.mean(y_real)) ** 2)
    R1 = y1 / y2
    print("可决系数R^2=", R1)
    R2 = 1 - ((len(y_real) - 1) / (len(y_real) - 4 - 1)) * (1 - R1 ** 2)
    print("修正自由度的可决系数R^2=", R2)
    # 计算标准估计误差
    S = (np.sum((y_real - y_predict) ** 2) / (len(y_real) - 4)) ** 0.5
    print("标准估计误差为S = ", S)
    u2 = (y_real - y_predict) ** 2
    plt.figure()
    plt.title("u^2-x散点图")
    plt.plot(u2, '.')
    plt.show()
    S = (np.sum((y_real - y_predict) ** 2) / (len(y_predict) - 4)) ** 0.5
    C = np.linalg.inv(np.matmul(X.T, X))
    T = []
    for i in range(len(B)):
        T.append(B[i] / (S * C[i][i] ** 0.5))
    print(T)
    T = np.array(T)
    plt.figure()
    plt.axhline(y=1.9818, ls="-", c="green")
    plt.plot(np.abs(T), '.')
    # plt.show()
    # print(y_predict[-1])

def getPredictData(pro):
    x_first_train, x_second_train, x_third_train, x_first_predict, x_second_predict, x_third_predict, y_income = read_check_data(
        pro)
    x1,x2,X, B, y_predict = multiple_regression(x_first_train, x_second_train, x_third_train, x_first_predict,
                                          x_second_predict, x_third_predict, y_income)
    # realData = list(zip(x1,y_income))
    realData = [list(i) for i in zip(x1,y_income)]
    predictData = [list(i) for i in zip(x2, y_predict)]
    dictPrediction={
        "realGdp": realData,
        "predictGdp":predictData
    }
    return  json.dumps(dictPrediction)

if __name__ == '__main__':
    pro = "北京市"
    # x_first_train,x_second_train,x_third_train, x_first_predict,x_second_predict, x_third_predict, y_income = read_check_data(pro)
    # X, B, y_predict = multiple_regression(x_first_train,x_second_train,x_third_train, x_first_predict,x_second_predict, x_third_predict, y_income)
    print(getPredictData(pro))
    # check(y_income, y_predict, X, B)
    # print(read_check_data(pro)[0])
    # print(read_check_data(pro)[3])


