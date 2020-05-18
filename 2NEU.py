#-*-coding:utf-8 -*-需要用rtklib转换成NEU然后使用此脚本画图
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')

plt.rcParams['font.sans-serif']=['simsun']
plt.rcParams['axes.unicode_minus']=False

import numpy as np
def readFile(filename):
    f = open(filename,'r',encoding='utf-8') #如果文件不是uft-8编码方式，读取文件可能报错
    dataLines = f.readlines() #返回list，文件的每一行作为list的一个字符串元素
    # dataLines = dataLines[200:-250]  #读取行数的起始位置
    return dataLines


def getE(data = []):
    E = []
    for i in data:
        E.append(float(i[0:9]))
    return E
def getN(data = []):
    N = []
    for i in data:
        print(i)
        N.append(float(i[10:19]))
    return N
def getU(data = []):
    U = []
    for i in data:
        U.append(float(i[20:29]))
    return U

def getData(data = []):
    E=[]
    N=[]
    U=[]
    for i in data:
        E.append(float(i.split()[0])+0.3)
        N.append(float(i.split()[1]))
        U.append(float(i.split()[2]))
    return [E,N,U]

def plot_enu(data1 = [],dataName1='',data2 = [],dataName2='',data3 = [],dataName3='',data12_scale_y=0,data3_scale_y=0):
# 第一个数据配置:
    data1_scale_y = data12_scale_y # y轴范围
    data1_epoch = len(data1) #x轴范围
    data1_yname = "errors/m"
    data1_xname = "epoch/s"
    data1_label = dataName1
# 第二个数据配置:
    data2_scale_y = data12_scale_y # y轴范围
    data2_epoch = len(data2) #x轴范围
    data2_yname = "errors/m"
    data2_xname = "epoch/s"
    data2_label = dataName2
# 第三个数据配置:
    data3_scale_y = data3_scale_y # y轴范围
    data3_epoch = len(data3) #x轴范围
    data3_yname = "errors/m"
    data3_xname = "epoch/s"
    data3_label = dataName3

# 只绘制一张图，含三个数据集----------------------------------------------------
#     data1x = np.linspace(0, data1_epoch, data1_epoch)
#     data2x = np.linspace(0, data2_epoch, data2_epoch)
#     data3x = np.linspace(0, data3_epoch, data3_epoch)
#     fig = plt.figure(1)
#     ax = SubplotZero(fig, 1, 1, 1)
#     ax.axhline(0, color='black', lw=1)
#     fig.add_subplot(ax)
#     fig.set_size_inches(8, 4)
#     fig.subplots_adjust(hspace=0.5)
#     plt.plot(data3x, data3, "g.", label=data3_label)
#     plt.plot(data2x, data2, "b.", label=data2_label)
#     plt.plot(data1x, data1, "r.", label=data1_label)
#     plt.grid("on")
#     plt.ylabel(data1_yname, fontproperties=myfont)
#     plt.xlabel(data1_xname, fontproperties=myfont)
#     plt.ylim(-data1_scale_y, data1_scale_y)
#     plt.legend()

# 绘制两张图----------------------------------------------------
# 第一张图，含两个数据集
    data1x = np.linspace(0, data1_epoch, data1_epoch)
    data2x = np.linspace(0, data2_epoch, data2_epoch)
    fig = plt.figure(1)
    ax = SubplotZero(fig, 2, 1, 1)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(hspace=0.5)
    plt.plot(data2x, data2, "b.", label=data2_label)
    plt.plot(data1x, data1, "r.", label=data1_label)
    plt.grid("on")
    plt.ylabel(data1_yname, fontproperties=myfont)
    plt.xlabel(data1_xname, fontproperties=myfont)
    plt.ylim(-data1_scale_y, data1_scale_y)
    plt.legend()
# 第二张图，含一个数据集
    data3x = np.linspace(0, data3_epoch, data3_epoch)
    fig = plt.figure(1)
    ax = SubplotZero(fig, 2, 1, 2)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(hspace=0.5)
    plt.plot(data3x, data3, "g.", label=data3_label)
    plt.grid("on")
    plt.ylabel(data3_yname, fontproperties=myfont)
    plt.xlabel(data3_xname, fontproperties=myfont)
    plt.ylim(-data3_scale_y, data3_scale_y)
    plt.legend()


    plt.show()

def getM(data = []):
    dataSum = 0
    for i in data:
        dataSum =float(i) * float(i)+dataSum
    dataM2 = dataSum/(len(data)-1)
    dataM = sqrt(dataM2)
    return dataM

filename106 = 'G:\\北斗地基增强导航定位平台软件\\不规则格网测试\\106NEU.txt'
filename500 = 'G:\\北斗地基增强导航定位平台软件\\不规则格网测试\\500NEU.txt'
filename1000 = 'G:\\C-workspace\\材料\\材料\\GNSS_Primary_VS\\GNSS_Primary_vs\\GNSS_Primary\\mobileDiffenu.txt'
# filename = 'E:\\湖南测试\\论文数据\\改正数\\201911131806TestGRIDpos.txt'
data106 = readFile(filename106)
data500 = readFile(filename500)
data1000 = readFile(filename1000)

ENU106 = getData(data106)
ENU500 = getData(data500)
ENU1000 = getData(data1000)

E=ENU1000[0]
N=ENU1000[1]
U=ENU1000[2]

# print("1111111111111111111111111111111111111111")
# print(E)
# print(N)
# print(U)
print("1111111111111111111111111111111111111111")
Me = getM(E)
Mn = getM(N)
Mu = getM(U)
print(Me,Mn,Mu,sqrt(Me*Me+Mn*Mn),sqrt(Me*Me+Mn*Mn+Mu*Mu))
'''
Me = Me[0:8]
Mn = Mn[0:8]
Mu = Mu[0:8]
'''
# draw(E,N,U,Me,Mn,Mu)
plot_enu(E,'E',N,'N',U,'U',30,50)




