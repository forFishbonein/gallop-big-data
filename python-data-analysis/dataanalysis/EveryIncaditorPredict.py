# -*- coding: utf-8 -*-
#导入必要的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import BPNN
from sklearn import metrics
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
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
    #



def readDataframe():
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id":0,"行政区划代码":1,"年份":1,"地区生产总值":1})
    df = pd.DataFrame(list(data))
    # for doc in collection.find({},{"_id":0,"行政区划代码":1,"年份":1,"地区生产总值":1}):
    #     # print(doc)
    #     data.append(doc)
    # data = pd.DataFrame(data)
    # data = pd.read_csv(r"D:\肖红娇\项目\大数据实训\data\province.csv")
    # data = data[["行政区划代码","年份","地区生产总值"]]

    df = df[df["年份"]>=2000]
    df = df.reset_index()

    # spark = SparkSession.builder.appName("GDP Average").getOrCreate()
    return df
def prepareData():
    inputData = readDataframe()
    print(inputData)
    # 进行数据归一化
    predictData = inputData[["行政区划代码","年份","地区生产总值"]]
    li = predictData.groupby("行政区划代码").count().reset_index()
    for i in range(31):
        year = 2020
        for j in range(10):
            year += 1
            predictData = pd.DataFrame(
                np.insert(predictData.values, len(predictData), values=[li["行政区划代码"][i], year, 0],
                          axis=0))

    predictData.columns = ["行政区划代码","年份","地区生产总值"]
    min_max_scaler = preprocessing.MinMaxScaler()
    df0 = min_max_scaler.fit_transform(predictData.interpolate())
    predictData = pd.DataFrame(df0, columns=predictData.columns)
    return predictData

if __name__ == '__main__':

    inputData = prepareData()
    x=inputData.iloc[:,:-1]
    print(x)
    y=inputData.iloc[:,-1]
    min_max_scaler = preprocessing.MinMaxScaler()
    #划分训练集测试集
    cut=310#取最后cut=30天为测试集
    x_train, x_predict=x.iloc[:-cut],x.iloc[-cut:]#列表的切片操作，X.iloc[0:2400，0:7]即为1-2400行，1-7列
    y_train=y.iloc[:-cut]
    x_train, x_predict=x_train.values, x_predict.values
    y_train=y_train.values
    #神经网络搭建
    bp1 = BPNN.BPNNRegression([2, 16, 1])
    # print(y_train)
    train_data = [[sx.reshape(2,1), sy.reshape(1,1)] for sx, sy in zip(x_train, y_train)]
    predict_data = [np.reshape(sx, (2,1)) for sx in x_predict]
    #神经网络训练
    bp1.MSGD(train_data, 80000, len(train_data), 0.2)
    #神经网络预测
    y_predict=bp1.predict(predict_data)
    y_pre = np.array(y_predict)  # 列表转数组
    y_pre=y_pre.reshape(310,1)
    y_pre=y_pre[:,0]
    #y_pre = min_max_scaler.inverse_transform(y_pre)
    # y_pre=inverse_transform_col(min_max_scaler,y_pre,n_col=0)      # 对预测值反归一化
    # y_test=inverse_transform_col(min_max_scaler,y_test,n_col=0)    # 对实际值反归一化（如果不想用，这两行删除即可）
    #画图 #展示在测试集上的表现
    print(y_pre)
    # draw=pd.concat([pd.DataFrame(y_test),pd.DataFrame(y_pre)],axis=1)
    # draw.iloc[:,0].plot(figsize=(12,6))
    # draw.iloc[:,1].plot(figsize=(12,6))
    # plt.legend(('real', 'predict'),loc='upper right',fontsize='15')
    # plt.title("Test Data",fontsize='30') #添加标题
    # plt.show()
    #输出精度指标
    # print('测试集上的MAE/MSE')
    # print(mean_absolute_error(y_pre, y_test))
    # print(mean_squared_error(y_pre, y_test) )
    # mape = np.mean(np.abs((y_pre-y_test)/(y_test)))*100
    # print('=============mape==============')
    # print(mape,'%')
    # # 画出真实数据和预测数据的对比曲线图
    # print("R2 = ",metrics.r2_score(y_test, y_pre)) # R2

    # -*- coding=utf-8 -*-
    # name: nan chen
    # date: 2021/5/6 15:05