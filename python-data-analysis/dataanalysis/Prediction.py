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

def inverse_transform_col(scaler,y,n_col):
    '''scaler是对包含多个feature的X拟合的,y对应其中一个feature,n_col为y在X中对应的列编号.返回y的反归一化结果'''
    y = y.copy()
    y -= scaler.min_[n_col]
    y /= scaler.scale_[n_col]
    return y

if __name__ == '__main__':


    provinceData=pd.read_csv(r"D:\肖红娇\项目\大数据实训\data\province.csv")
    cols = ['居民消费价格指数(上年=100)','全体居民人均消费支出','规模以上工业企业出口交货值','地区生产总值']

    inputData = provinceData[cols]

    #进行数据归一化

    min_max_scaler = preprocessing.MinMaxScaler()
    df0=min_max_scaler.fit_transform(inputData.interpolate())
    df = pd.DataFrame(df0, columns=inputData.columns)
    x=df.iloc[:,:-1]
    print(x)
    y=df.iloc[:,-1]

    #划分训练集测试集
    cut=300#取最后cut=30天为测试集
    x_train, x_test=x.iloc[:-cut],x.iloc[-cut:]#列表的切片操作，X.iloc[0:2400，0:7]即为1-2400行，1-7列
    y_train, y_test=y.iloc[:-cut],y.iloc[-cut:]
    x_train, x_test=x_train.values, x_test.values
    y_train, y_test=y_train.values, y_test.values
    #神经网络搭建
    bp1 = BPNN.BPNNRegression([3, 16, 1])
    # print(y_train)

    train_data = [[sx.reshape(3,1), sy.reshape(1,1)] for sx, sy in zip(x_train, y_train)]
    test_data = [np.reshape(sx, (3,1)) for sx in x_test]
    #神经网络训练
    bp1.MSGD(train_data, 80000, len(train_data), 0.2)
    #神经网络预测
    y_predict=bp1.predict(test_data)
    y_pre = np.array(y_predict)  # 列表转数组
    y_pre=y_pre.reshape(300,1)
    y_pre=y_pre[:,0]

    #y_pre = min_max_scaler.inverse_transform(y_pre)
    y_pre=inverse_transform_col(min_max_scaler,y_pre,n_col=0)      # 对预测值反归一化
    y_test=inverse_transform_col(min_max_scaler,y_test,n_col=0)    # 对实际值反归一化（如果不想用，这两行删除即可）
    #画图 #展示在测试集上的表现
    draw=pd.concat([pd.DataFrame(y_test),pd.DataFrame(y_pre)],axis=1)
    draw.iloc[:,0].plot(figsize=(12,6))
    draw.iloc[:,1].plot(figsize=(12,6))
    plt.legend(('real', 'predict'),loc='upper right',fontsize='15')
    plt.title("Test Data",fontsize='30') #添加标题
    plt.show()
    #输出精度指标
    print('测试集上的MAE/MSE')
    print(mean_absolute_error(y_pre, y_test))
    print(mean_squared_error(y_pre, y_test) )
    mape = np.mean(np.abs((y_pre-y_test)/(y_test)))*100
    print('=============mape==============')
    print(mape,'%')
    # 画出真实数据和预测数据的对比曲线图
    print("R2 = ",metrics.r2_score(y_test, y_pre)) # R2

    # encoding:utf-8

