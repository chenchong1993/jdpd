#-*-coding:utf-8 -*-
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')

import numpy as np
def readFile(filename):
    f = open(filename,'r',encoding='utf-8') #如果文件不是uft-8编码方式，读取文件可能报错
    dataLines = f.readlines() #返回list，文件的每一行作为list的一个字符串元素
    dataLines = dataLines[:60000]  #读取行数的起始位置
    dataList = []
    for i in dataLines:
        if "C" in i:
            pass
        elif "G" in i:
            pass
        elif "0 -1" in i:
            pass
        elif "9 -1" in i:
            pass
        else:
            dataList.append(i)
    return dataList[10:-10]

#计算平均数
def averagenum(num=[]):
    nsum = 0
    for i in range(len(num)):
        num[i] = float(num[i][:-2])
        nsum += num[i]
    return nsum / len(num)

def getData(data = []):
    multPath=[]
    for i in data:
        multPath.append(averagenum(i.split()))
    # print(multPath)
    return multPath

def getSTD(data = []):
    sum = 0
    for i in data:
        sum = sum + i*i
    std2 = sum/len(data)
    std = sqrt(std2)
    return std

def plot_2D(data1 = [],data2 = [],data3 = []):

# 修改配置----------------------------------------------
# 第一张图配置:
    data1_scale_y = 8 # y轴范围
    data1_epoch = len(data1) #x轴范围
    data1_yname = "multipath errors/m"
    data1_xname = "epoch/s"
    data1_label = "Huawei P30"
# 第一张图配置:
    data2_scale_y = 8 # y轴范围
    data2_epoch = len(data2) #x轴范围
    data2_yname = "multipath errors/m"
    data2_xname = "epoch/s"
    data2_label = "xiaomi M8"
# 第一张图配置:
    data3_scale_y = 1 # y轴范围
    data3_epoch = len(data3) #x轴范围
    data3_yname = "multipath errors/m"
    data3_xname = "epoch/s"
    data3_label = "Trimble R9"
# 绘制第一张图----------------------------------------------------
    x = np.linspace(0, data1_epoch, data1_epoch)  # 0到24 分240份
    fig = plt.figure(1)
    ax = SubplotZero(fig, 3, 1, 1)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(hspace=0.5)
    plt.plot(x, data1, "r.", label=data1_label)
    plt.ylabel(data1_yname, fontproperties=myfont)
    plt.xlabel(data1_xname, fontproperties=myfont)
    plt.ylim(-data1_scale_y, data1_scale_y)
    plt.legend()
    # plt.grid("on")

# 绘制二张图----------------------------------------------------
    x = np.linspace(0, data2_epoch, data2_epoch)  # 0到24 分240份
    fig = plt.figure(1)
    ax = SubplotZero(fig, 3, 1, 2)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    plt.plot(x, data2, "b.", label=data2_label)
    plt.ylabel(data2_yname, fontproperties=myfont)
    plt.xlabel(data2_xname, fontproperties=myfont)
    plt.ylim(-data2_scale_y, data2_scale_y)
    plt.legend()
    # plt.grid("on")
# 绘制三张图----------------------------------------------------
    x = np.linspace(0, data3_epoch, data3_epoch)  # 0到24 分240份
    fig = plt.figure(1)
    ax = SubplotZero(fig, 3, 1, 3)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    plt.plot(x, data3, "g.", label=data3_label)
    plt.ylabel(data3_yname, fontproperties=myfont)
    plt.xlabel(data3_xname, fontproperties=myfont)
    plt.ylim(-data3_scale_y, data3_scale_y)
    plt.legend()
    # plt.grid("on")
# ------------------------------------------------------------------------------------------------
    plt.show()

fileR9 = 'R9.m12'
dataR9 = readFile(fileR9)

fileP30 = 'P30.m15'
dataP30 = readFile(fileP30)

fileM8 = 'm8.m15'
dataM8 = readFile(fileM8)

multPathR9 = getData(dataR9)
multPathP30 = getData(dataP30)
multPathM8 = getData(dataM8)

print(getSTD(multPathP30))
print(getSTD(multPathM8))
print(getSTD(multPathR9))
print(np.std(multPathP30))
print(np.std(multPathM8))
print(np.std(multPathR9))
# plot_2D(multPathP30,multPathM8,multPathR9)
# plot()