#-*-coding:utf-8 -*-需要用rtklib转换成NEU然后使用此脚本画图
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')

import numpy as np
def readFile(filename):
    f = open(filename,'r',encoding='utf-8') #如果文件不是uft-8编码方式，读取文件可能报错
    dataLines = f.readlines() #返回list，文件的每一行作为list的一个字符串元素
    dataLines = dataLines[200:-100]  #读取行数的起始位置
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
        E.append(float(i.split()[0]))
        N.append(float(i.split()[1]))
        U.append(float(i.split()[2]))
    return [E,N,U]

# def draw(data = [],str = "x方向"):
#     x = range(len(data))
#     fig = plt.figure(1, (10, 6))
#
#     ax = SubplotZero(fig, 1, 1, 1)
#     fig.add_subplot(ax)
#     ax.axis["xzero"].set_visible(True)
#     ax.axis["xzero"].label.set_color('green')
#     plt.ylim(-5, 5)  # 限定纵轴的范围
#     plt.plot(x, data)
#     plt.legend()  # 让图例生效
#     plt.margins(0)
#     plt.subplots_adjust(bottom=0.15)
#     plt.xlabel(u"eph") #X轴标签
#     plt.ylabel("m") #Y轴标签
#     plt.title(str) #标题
#     plt.show()

def draw(dataE = [],dataN = [],dataU = [],Me = "",Mn = "",Mu = ""):
    eph = range(len(data))
    fig = plt.figure()
    # 将整个figure分成三行一列，第三个参数表示该图形放在第1个网格
    ax = SubplotZero(fig, 3, 1, 1)
    fig.add_subplot(ax)
    ax.axis["xzero"].set_visible(True)
    plt.ylim(-2, 2)  # 限定纵轴的范围
    plt.scatter(eph, dataE,marker='x',s=0.5,color=(0.,0.5,0.))
    plt.legend()  # 让图例生效
    plt.margins(0)
    #plt.xlabel(u"eph")  # X轴标签
    #plt.ylabel("m")  # Y轴标签
    plt.title("E方向残差/m",fontproperties=myfont)
    plt.tight_layout()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.5, hspace=0.5)
    # 将整个figure分成三行一列，第三个参数表示该图形放在第2个网格
    ax = SubplotZero(fig, 3, 1, 2)
    fig.add_subplot(ax)
    ax.axis["xzero"].set_visible(True)
    plt.ylim(-2, 2)  # 限定纵轴的范围
    plt.scatter(eph, dataN,marker='x',s=0.5,color=(0.,0.5,0.))
    plt.legend()  # 让图例生效
    plt.margins(0)
    #plt.xlabel(u"eph")  # X轴标签
    #plt.ylabel("m")  # Y轴标签
    plt.title("N方向残差/m",fontproperties=myfont)

    # 将整个figure分成三行一列，第三个参数表示该图形放在第3个网格
    ax = SubplotZero(fig, 3, 1, 3)
    fig.add_subplot(ax)
    ax.axis["xzero"].set_visible(True)
    plt.ylim(-3, 3)  # 限定纵轴的范围
    plt.scatter(eph, dataU,marker='x',s=0.5,color=(0.,0.5,0.))
    plt.legend()  # 让图例生效
    plt.margins(0)
    #plt.xlabel(u"eph")  # X轴标签
    #plt.ylabel("m")  # Y轴标签
    plt.title("U方向残差/m",fontproperties=myfont)

    plt.show()


def getM(data = []):
    dataSum = 0
    for i in data:
        dataSum =float(i) * float(i)+dataSum
    dataM2 = dataSum/(len(data)-1)
    dataM = sqrt(dataM2)
    return dataM

filename = 'C:\\Users\\chenc\\Desktop\\不规则格网\\不同高程测试\\最终数据\\不规则1000NEU.txt'
data = readFile(filename)

ENU = getData(data)

E=ENU[0]
N=ENU[1]
U=ENU[2]

print(E)
print(N)
print(U)

Me = "Me=" + str(getM(E))
Mn = "Mn=" + str(getM(N))
Mu = "Mu=" + str(getM(U))
Me = Me[0:8]
Mn = Mn[0:8]
Mu = Mu[0:8]
draw(E,N,U,Me,Mn,Mu)
