# -*- coding: utf-8 -*-
import json

import numpy as np
import math
import random
import string
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import Connection
#random.seed(0)  #当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
#参考https://blog.csdn.net/jiangjiang_jian/article/details/79031788

#生成区间[a,b]内的随机数
def random_number(a,b):
    return (b-a)*random.random()+a

#生成一个矩阵，大小为m*n,并且设置默认零矩阵
def makematrix(m, n, fill=0.0):
    a = []
    for i in range(m):
        a.append([fill]*n)
    return a

#函数sigmoid(),这里采用tanh，因为看起来要比标准的sigmoid函数好看
def sigmoid(x):
    return math.tanh(x)

#函数sigmoid的派生函数
def derived_sigmoid(x):
    return 1.0 - x**2

#构造三层BP网络架构
class BPNN:
    def __init__(self, num_in, num_hidden, num_out):
        #输入层，隐藏层，输出层的节点数
        self.num_in = num_in + 1  #增加一个偏置结点
        self.num_hidden = num_hidden + 1   #增加一个偏置结点
        self.num_out = num_out

        #激活神经网络的所有节点（向量）
        self.active_in = [1.0]*self.num_in
        self.active_hidden = [1.0]*self.num_hidden
        self.active_out = [1.0]*self.num_out

        #创建权重矩阵
        self.wight_in = makematrix(self.num_in, self.num_hidden)
        self.wight_out = makematrix(self.num_hidden, self.num_out)

        #对权值矩阵赋初值
        for i in range(self.num_in):
            for j in range(self.num_hidden):
                self.wight_in[i][j] = random_number(-0.2, 0.2)
        for i in range(self.num_hidden):
            for j in range(self.num_out):
                self.wight_out[i][j] = random_number(-0.2, 0.2)

        #最后建立动量因子（矩阵）
        self.ci = makematrix(self.num_in, self.num_hidden)
        self.co = makematrix(self.num_hidden, self.num_out)

        #信号正向传播
    def update(self, inputs):
        if len(inputs) != self.num_in-1:
            raise ValueError('与输入层节点数不符')

        #数据输入输入层
        for i in range(self.num_in - 1):
            #self.active_in[i] = sigmoid(inputs[i])  #或者先在输入层进行数据处理
            self.active_in[i] = inputs[i]  #active_in[]是输入数据的矩阵

        #数据在隐藏层的处理
        for i in range(self.num_hidden - 1):
            sum = 0.0
            for j in range(self.num_in):
                sum = sum + self.active_in[i] * self.wight_in[j][i]

            self.active_hidden[i] = sigmoid(sum)   #active_hidden[]是处理完输入数据之后存储，作为输出层的输入数据

        #数据在输出层的处理
        for i in range(self.num_out):
            sum = 0.0
            for j in range(self.num_hidden):
                sum = sum + self.active_hidden[j]*self.wight_out[j][i]
            self.active_out[i] = sigmoid(sum)   #与上同理
            # print(self.active_out[i])
        return self.active_out[:]

    #误差反向传播
    def errorbackpropagate(self, targets, lr, m):   #lr是学习率， m是动量因子
        global j
        if len(targets) != self.num_out:
            raise ValueError('与输出层节点数不符！')

        #首先计算输出层的误差
        out_deltas = [0.0]*self.num_out
        for i in range(self.num_out):
            error = targets[i] - self.active_out[i]
            out_deltas[i] = derived_sigmoid(self.active_out[i])*error

        #然后计算隐藏层误差
        hidden_deltas = [0.0]*self.num_hidden
        for i in range(self.num_hidden):
            error = 0.0
            for j in range(self.num_out):
                error = error + out_deltas[j]* self.wight_out[i][j]
            hidden_deltas[i] = derived_sigmoid(self.active_hidden[i])*error

        #首先更新输出层权值
        for i in range(self.num_hidden):
            for j in range(self.num_out):
                change = out_deltas[j]*self.active_hidden[i]
                self.wight_out[i][j] = self.wight_out[i][j] + lr*change + m*self.co[i][j]
                self.co[i][j] = change

        #然后更新输入层权值
        for i in range(self.num_in):
            for i in range(self.num_hidden):
                change = hidden_deltas[j]*self.active_in[i]
                self.wight_in[i][j] = self.wight_in[i][j] + lr*change + m* self.ci[i][j]
                self.ci[i][j] = change

        #计算总误差
        error = 0.0
        for i in range(len(targets)):
            error = error + 0.5*(targets[i] - self.active_out[i])**2
        return error

    #测试
    def test(self, patt):
        dfData = pd.DataFrame(columns = ['评价指数'],index = range(0,len(patt)))

        for i in range(len(patt)):
            # dfData.iloc[i,0] = year[i]
            # dfData.iloc[i,1] = pro[i]
            dfData.iloc[i,0] = (self.update(list(patt)[i][0]))[0]
        return dfData
    #权重
    # def weights(self):
    #     print("输入层权重")
    #     for i in range(self.num_in):
    #         print(self.wight_in[i])
    #     print("输出层权重")
    #     for i in range(self.num_hidden):
    #         print(self.wight_out[i])

    def train(self, pattern, itera=10000, lr = 0.1, m=0.1):
        for i in range(itera):
            error = 0.0
            #             print(pattern)
            for j in pattern:
                inputs = j[0]
                targets = j[1]
                self.update(inputs)
                error = error + self.errorbackpropagate(targets, lr, m)
#             if i % 100 == 0:
#                 print('误差 %-.5f' % error)
#实例

def ZscoreNormalization(x):

    """Z-score normaliaztion"""
    x = (x - np.mean(x)) / np.std(x)
    return x

def MinMaxNormalized(x,type,ymin=0,ymax=1):
    """
    实现正向或负向指标MinMax归一化，返回归一化后的数据矩阵；
    x：为原始数据矩阵, 一行代表一个样本, 每列对应一个指标；
    type：设定正向指标1,负向指标2；
    ymin,ymax：归一化的区间端点，即归一化时将数据缩放到(ymin,ymax)的范围内，默认应设置为[0,1]；
    """
    n, m = x.shape
    y = np.zeros((n, m))
    xmin = np.min(x,axis=0)
    xmax = np.max(x,axis=0)
    if type == 1:
        for j in range(m):
            y[:,j] = (ymax-ymin)*(x[:,j]-xmin[j]) / (xmax[j]-xmin[j])+ymin
    elif type == 2:
        for j in range(m):
            y[:,j] = (ymax-ymin)*(xmax[j]-x[:,j]) / (xmax[j]-xmin[j])+ymin
    return y
def mal(x,ymin=0.0001,ymax=0.9999):
    n=len(x)
    Y = np.zeros(n)
    Y[:] = MinMaxNormalized(x[:].reshape(-1,1),1,ymin,ymax).flatten()
    # print(Y)
    return Y

def Normalization(x,ind,ymin=0.0001,ymax=0.9999):
    n,m = x.shape
    Y = np.zeros((n, m))
    for i in range(m):
        if ind[i] == 1: #正向指标归一化
            Y[:,i] = MinMaxNormalized(x[:,i].reshape(-1,1),1,ymin,ymax).flatten()
        elif ind[i] == 2: #负向指标归一化
            Y[:,i] = MinMaxNormalized(x[:,i].reshape(-1,1),2,ymin,ymax).flatten()
    return Y

#实例
def demo(yr,inputData,outputData):

    indata = np.array(inputData.interpolate())
    indI = [1,1,1,1]

    outdata = np.array(outputData.interpolate())

    inputData = Normalization(indata,indI)
    outputData= mal(outdata)
    out = []
    for i in range(len(outputData)):
        li = []
        li.append(outputData[i])
        out.append(li)
    # print(out)
    patt=list(zip(inputData,out))
    #     arr.astype(float)
    # for i in range(len(arrList)):
    #     temp=[list(arrList[i]),list(arrX[i][0:1])]
    #     patt.append(temp)
    #创建神经网络，3个输入节点，3个隐藏层节点，1个输出层节点
    # print(patt)
    n = BPNN(4, 3, 1)
    #训练神经网络
    n.train(patt)
    # n.weights()
    dataF = n.test(patt)
    return dataF
    #测试神经网络
def readDataframe():
    # collection = Connection.getCity()
    # data = []
    # for doc in collection.find({},{"_id":0,"地区":1,"年份":1,"居民消费价格指数(上年=100)":1,"全体居民人均消费支出":1,"规模以上工业企业出口交货值":1,"地区生产总值":1}):
    #     # print(doc)
    #     data.append(doc)
    # data = pd.DataFrame(data).dropna()
    db = Connection.getDB()
    mycol = db["province"]
    data = mycol.find({},{"_id": 0, '地区': 1, '年份': 1,
                                    '居民消费价格指数(上年=100)': 1,'全体居民人均消费支出':1,"规模以上工业企业出口交货值":1,"规模以上工业企业主营业务收入":1,"地区生产总值":1})

    data = pd.DataFrame(list(data)).dropna()
    return data

def EveryProvinceEvalution(pro):
    # provinceData = readDataframe()
    provinceData = pd.read_csv("data\province.csv")
    cols = ['居民消费价格指数(上年=100)','全体居民人均消费支出','规模以上工业企业出口交货值','规模以上工业企业主营业务收入']
    inputData = provinceData[provinceData['地区']==pro][cols]
    outputData = provinceData[provinceData['地区']==pro]['地区生产总值']

    year = provinceData[provinceData['地区']==pro]['年份']
    year = year.reset_index()
    # print(year)
    dataF = demo(pro,inputData,outputData)
    pro = provinceData[provinceData['地区']==pro]['地区']
    pro = pro.reset_index()

    dataF['年份'] = ''
    #查阅权重值
    # print(dataF)
    dataF['年份'] = year['年份']
    # dataF['省份'] = pro['地区']

    dataF = dataF[['年份','评价指数']]
    return dataF

def EveryYearEvalution(yr):
    # provinceData = readDataframe()
    provinceData = pd.read_csv(r"data\province.csv")

    cols = ['居民消费价格指数(上年=100)','全体居民人均消费支出','规模以上工业企业出口交货值','规模以上工业企业主营业务收入']

    inputData = provinceData[provinceData['年份']==yr][cols]

    outputData = provinceData[provinceData['年份']==yr]['地区生产总值']
    dataF = demo(yr,inputData,outputData)

    year = provinceData[provinceData['年份']==yr]['年份']
    year = year.reset_index()
    # print(year)

    pro = provinceData[provinceData['年份']==yr]['地区']
    pro = pro.reset_index()

    dataF['省份'] = ''
    #查阅权重值
    # dataF['年份'] = year['年份']
    dataF['省份'] = pro['地区']
    # print(dataF)
    dataF = dataF[['省份','评价指数']].values.tolist()
    dictYearEvaluation={
        "values":dataF
    }
    return json.dumps(dictYearEvaluation)

if __name__ == '__main__':
    # dataF = EveryYearEvalution(2016)
    # EvaluationRes = dataF.values
    # print(readDataframe())
    # print(EveryProvinceEvalution("北京市"))
    print(EveryYearEvalution(2016))