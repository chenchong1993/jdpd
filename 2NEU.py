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
        E.append(float(i.split()[0]))
        N.append(float(i.split()[1]))
        U.append(float(i.split()[2]))
    print(E)
    return [E,N,U]



def plot_2D(dataE = [],dataN = [],dataU = []):


    e1 = dataE
    n1 = dataN

    std_e = np.std(e1)
    std_n = np.std(n1)

    var_e = 5  # 标准差
    var_n = np.var(n1) ** 0.5  # 标准差

    scale_y = max(var_e,var_n) # 刻度 四倍中误差

    if scale_y > 200:  # 最大不超过2m
        scale_y = 200

    epoch = len(e1)

    lim1 = [10] * epoch
    lim2 = [-10] * epoch

    x = np.linspace(0, epoch, epoch)  # 0到24 分240份

    fig = plt.figure(1)
    ax = SubplotZero(fig, 2, 1, 1)
    fig.add_subplot(ax)

    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置

    # print(x)
    # print(e1)

    plt.plot(x, e1, "r.", label="E "+u"方向")
    plt.plot(x, n1, "b.", label="N "+u"方向")

    plt.plot(lim1, "m--")
    plt.plot(lim2, "m--")


    font2 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 15,
             }

    plt.ylabel("残差/m", font2,fontproperties=myfont)
    plt.xlabel("历元/s", font2,fontproperties=myfont)
    # plt.title(format("平面残差"), font2,fontproperties=myfont)
    plt.ylim(-scale_y, scale_y)
    plt.legend()
    plt.grid("on")
    # plt.savefig("error of 2D" +"("")"+ "{0}{1}.png".format(" ", name), dpi=300)
# ---------------------------------------U方向---------------------------------------------------------------------------
    u1 = dataU

    std_u = np.std(u1)

    var_u = 20 # 标准差
    var_n = np.var(u1) ** 0.5  # 标准差

    scale_y = max(var_u, var_n)  # 刻度 四倍中误差

    if scale_y > 200:  # 最大不超过2m
        scale_y = 200

    epoch = len(u1)
    #   print("历元数为=", epoch)

    lim1 = [10] * epoch
    lim2 = [-10] * epoch

    x = np.linspace(0, epoch, epoch)  # 0到24 分240份

    ax = SubplotZero(fig, 2, 1, 2)
    fig.add_subplot(ax)

    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=0.13, bottom=0.2)  # 一些设置
    #
    # print(x)
    # print(u1)

    plt.plot(x, u1, "g.", label="U " + u"方向")

    plt.plot(lim1, "m--")
    plt.plot(lim2, "m--")


    plt.ylabel("残差/m", font2, fontproperties=myfont)
    plt.xlabel("历元/s", font2, fontproperties=myfont)
    # plt.title(format("U方向残差"), font2,fontproperties=myfont)
    plt.ylim(-scale_y, scale_y)
    plt.legend()
    plt.grid("on")
    plt.show()

def plot_enu(data1 = [],data2 = [],data3 = []):

# 修改配置----------------------------------------------
# 第一张图配置:
    data1_scale_y = 15 # y轴范围
    data1_epoch = len(data1) #x轴范围
    data1_yname = "errors/m"
    data1_xname = "epoch/s"
    data1_label = "E"
# 第一张图配置:
    data2_scale_y = 8 # y轴范围
    data2_epoch = len(data2) #x轴范围
    data2_yname = "errors/m"
    data2_xname = "epoch/s"
    data2_label = "N"
# 第一张图配置:
    data3_scale_y = 30 # y轴范围
    data3_epoch = len(data3) #x轴范围
    data3_yname = "errors/m"
    data3_xname = "epoch/s"
    data3_label = "U"

# 绘制第一张图----------------------------------------------------
    E = np.linspace(0, data1_epoch, data1_epoch)  # 0到24 分240份
    N = np.linspace(0, data2_epoch, data2_epoch)  # 0到24 分240份
    fig = plt.figure(1)
    ax = SubplotZero(fig, 2, 1, 1)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(hspace=0.5)
    plt.plot(E, data1, "g.", label=data1_label)
    plt.plot(N, data2, "r.", label=data2_label)
    plt.ylabel(data1_yname, fontproperties=myfont)
    plt.xlabel(data1_xname, fontproperties=myfont)
    plt.ylim(-data1_scale_y, data1_scale_y)
    plt.legend()
    # plt.grid("on")

# 绘制二张图----------------------------------------------------
    U = np.linspace(0, data3_epoch, data3_epoch)  # 0到24 分240份
    fig = plt.figure(1)
    ax = SubplotZero(fig, 2, 1, 2)
    ax.axhline(0, color='black', lw=1)
    fig.add_subplot(ax)
    fig.set_size_inches(8, 4)
    plt.plot(U, data3, "g.", label=data3_label)
    plt.ylabel(data3_yname, fontproperties=myfont)
    plt.xlabel(data3_xname, fontproperties=myfont)
    plt.ylim(-data3_scale_y, data3_scale_y)
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

def getM(data = []):
    dataSum = 0
    for i in data:
        dataSum =float(i) * float(i)+dataSum
    dataM2 = dataSum/(len(data)-1)
    dataM = sqrt(dataM2)
    return dataM

filename = 'G:\\湖南测试\\论文数据\\单点\\201910211155TestSPPpos.txt'
# filename = 'E:\\湖南测试\\论文数据\\改正数\\201911131806TestGRIDpos.txt'
data = readFile(filename)

ENU = getData(data)

E=ENU[0]
N=ENU[1]
U=ENU[2]
print("1111111111111111111111111111111111111111")
print(E)
print(N)
print(U)
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
plot_enu(E,N,U)


