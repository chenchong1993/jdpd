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
    dataLines = dataLines[:30000]  #读取行数的起始位置
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
    num = 0
    for i in data:
        if(i == 0):
            pass
        else:
            sum = sum + i*i
            num = num+1
    std2 = sum/num
    print(num,len(data))
    std = sqrt(std2)
    return std

def plot_2D(data1 = [],data2 = [],data3 = [],data4=[]):

# 修改配置----------------------------------------------
# 第一张图配置:
    data1_scale_y = 8 # y轴范围
    data1_epoch = len(data1) #x轴范围
    data1_yname = "multipath errors/m"
    data1_xname = "epoch/s"
    data1_label = "Huawei P30 L1"
# 第一张图配置:
    data2_scale_y = 8 # y轴范围
    data2_epoch = len(data2) #x轴范围
    data2_yname = "multipath errors/m"
    data2_xname = "epoch/s"
    data2_label = "xiaomi M8 L1"
# 第一张图配置:
    data3_scale_y = 1 # y轴范围
    data3_epoch = len(data3) #x轴范围
    data3_yname = "multipath errors/m"
    data3_xname = "epoch/s"
    data3_label = "Huawei P30 L5"
# 第一张图配置:
    data4_scale_y = 1 # y轴范围
    data4_epoch = len(data4) #x轴范围
    data3_yname = "multipath errors/m"
    data3_xname = "epoch/s"
    data4_label = "xiaomi M8 L5"
# 绘制第一张图----------------------------------------------------
    x3 = np.linspace(0, data3_epoch, data3_epoch)  # 0到24 分240份
    x = np.linspace(0, data1_epoch, data1_epoch)  # 0到24 分240份
    fig = plt.figure(1)
    ax = SubplotZero(fig, 2, 1, 1)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(hspace=0.5)
    plt.plot(x, data1, "g.", label=data1_label)
    plt.plot(x3, data3, "r.", label=data3_label)
    plt.ylabel(data1_yname, fontproperties=myfont)
    plt.xlabel(data1_xname, fontproperties=myfont)
    plt.ylim(-data1_scale_y, data1_scale_y)
    plt.legend()
    # plt.grid("on")

# 绘制二张图----------------------------------------------------
    x4 = np.linspace(0, data4_epoch, data4_epoch)  # 0到24 分240份
    x = np.linspace(0, data2_epoch, data2_epoch)  # 0到24 分240份
    fig = plt.figure(1)
    ax = SubplotZero(fig, 2, 1, 2)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    plt.plot(x, data2, "g.", label=data2_label)
    plt.plot(x4, data4, "r.", label=data4_label)
    plt.ylabel(data2_yname, fontproperties=myfont)
    plt.xlabel(data2_xname, fontproperties=myfont)
    plt.ylim(-data2_scale_y, data2_scale_y)
    plt.legend()
    # plt.grid("on")
# 绘制三张图----------------------------------------------------
#     x = np.linspace(0, data3_epoch, data3_epoch)  # 0到24 分240份
#     fig = plt.figure(1)
#     ax = SubplotZero(fig, 3, 1, 3)
#     ax.axhline(0, color='black', lw=1)
#     fig.add_subplot(ax)
#     fig.set_size_inches(8, 4)
#     plt.plot(x, data3, "g.", label=data3_label)
#     plt.ylabel(data3_yname, fontproperties=myfont)
#     plt.xlabel(data3_xname, fontproperties=myfont)
#     plt.ylim(-data3_scale_y, data3_scale_y)
#     plt.legend()
    # plt.grid("on")
# ------------------------------------------------------------------------------------------------
    plt.show()

fileR9 = 'gpsr9.m12'
dataR9 = readFile(fileR9)

fileP30L1 = 'gpsp30.m15'
dataP30L1 = readFile(fileP30L1)
fileP30L5 = 'gpsp30.m51'
dataP30L5 = readFile(fileP30L5)

fileM8L1 = 'gpsm8.m15'
dataM8L1 = readFile(fileM8L1)
fileM8L5 = 'gpsm8.m51'
dataM8L5 = readFile(fileM8L5)

multPathR9 = getData(dataR9)
multPathP30L1 = getData(dataP30L1)
multPathM8L1 = getData(dataM8L1)
multPathP30L5 = getData(dataP30L5)
multPathM8L5 = getData(dataM8L5)
# print(getSTD(multPathP30L1))
# print(getSTD(multPathP30L5))

print(getSTD(multPathR9))
print(getSTD(multPathM8L1))
print(getSTD(multPathP30L1))
print(getSTD(multPathM8L5))
print(getSTD(multPathP30L5))
# print(np.std(multPathP30L1))
# print(np.std(multPathM8))
# print(np.std(multPathR9))
# plot_2D(multPathP30L1,multPathM8L1,multPathP30L5,multPathM8L5)
# plot()