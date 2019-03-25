# -*- coding: utf-8 -*-
"""
绘制登高线图
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.cm as cm

# 定义等高线高度函数
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(- x ** 2 - y ** 2)

def get_contour():
    # 数据数目
    n = 256
    # 定义x, y
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)

    # 生成网格数据
    X, Y = np.meshgrid(x, y)

    # 填充等高线的颜色, 8是等高线分为几部分
    plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)
    # 绘制等高线
    C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=0.5)
    # 绘制等高线数据
    plt.clabel(C, inline=True, fontsize=10)

    # 去除坐标轴
    plt.xticks(())
    plt.yticks(())
    plt.show()

#get_contour()     #生成等高线图

def get_3d_map():
    # -*- coding: utf-8 -*-
    """
    绘制3d图形
    """
    # 定义figure
    fig = plt.figure()
    # 将figure变为3d
    ax = Axes3D(fig)

    # 数据数目
    n = 256
    # 定义x, y
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)

    # 生成网格数据
    X, Y = np.meshgrid(x, y)

    # 计算每个点对的长度
    R = np.sqrt(X ** 2 + Y ** 2)
    # 计算Z轴的高度
    Z = np.sin(R)

    # 绘制3D曲面

    plt.title("这是我画的哦",fontproperties="KaiTi")  # 总标题

    z1 = Z * np.cos(0.5 * x)

    N = z1 / z1.max()  # normalie 0..1

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'),alpha=0.5,facecolors=cm.jet(N))
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')  # 给三个坐标轴注明
    # 绘制从3D曲面到底部的投影
    ax.contour(X, Y, Z, zdim='z', offset=-2, cmap='rainbow')

    # 设置z轴的维度
    ax.set_zlim(-2, 2)

    #fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

# get_3d_map()    #绘制3d图

'''
    绘制余弦 正弦图
'''
def get_sin_map():
    x = np.linspace(0,10,100)
    y = np.sin(x)

    plt.plot(x,y,'--')
    plt.plot(x,np.cos(x))
    plt.show()

#get_sin_map()

'''
    保存图片    传入要保存的地址  以及x-y
'''
def save_map(save_path,x,y):
    fig = plt.figure()
    plt.plot(x,y,'--')
    #plt.show()
    fig.savefig(save_path)

#save_map('C:/Users/HASEE/Desktop/python',x = np.linspace(0,10,100),y=np.sin(np.linspace(0,10,100)))

def get_mut_map(x):
    plt.subplot(2,1,1)
    plt.plot(x,np.sin(x),'--')

    plt.subplot(2,1,2)
    plt.plot(x,np.cos(x),'o')

    plt.show()

#get_mut_map(np.linspace(0,10,50))  #绘制多个图

def get_map_color(x,y,color):
   plt.plot(x,np.sin(x),'o',color=color)
   plt.show()

#get_map_color(np.linspace(0,10,20),np.cos(np.linspace(0,10,30)),'blue')

def get_desc_map(x):
    y = np.sin(x)
    plt.plot(x,y,'--',label='sin(x)')
    plt.plot(x,np.cos(x),'o',label='cos(x)')
   #plt.plot(x,np.tan(x),'-p',color='orange',markersize=16,linewidth=2,markeredgecolor='pink',markeredgewidth=1)
    #plt.ylim(-0.5,0.8)
    #plt.xlim(0.8,1)
    plt.legend(loc=1)
    plt.show()

#get_desc_map(np.linspace(0,10,20))

def get_scatter_map():
    plt.scatter(np.linspace(0,10,20),np.sin(np.linspace(0,10,20)),s=100,c='pink')
    plt.show()

#get_scatter_map()

def get_random_scatter_map():
    x = np.random.randn(100)
    y = np.random.rand(100)
    colors = np.random.rand(100)
    sizes = 1000 * np.random.rand(100)
    plt.scatter(x,y,c=colors,s=sizes,alpha=0.4)
    plt.colorbar()
    plt.show()

#get_random_scatter_map()

def get_pandas_map():
    df = pd.DataFrame(np.random.rand(100,4).cumsum(0),columns=['A','B','C','D'])
    df.plot()
    plt.show()

#get_pandas_map()

def get_pandas_histogram_map():
    df = pd.DataFrame(np.random.randint(10,50,(3,4)).cumsum(0),columns=['A','B','C','D'],index=['one','two','three'])
    df.plot.bar()
    df.plot(kind='bar',stacked=True)
    plt.show()

#get_pandas_histogram_map()

def get_hist_map():
    df = pd.DataFrame(np.random.rand(100,4), columns=['A', 'B', 'C', 'D'])
    df.hist()
    plt.show()

#get_hist_map()
def get_hist_one_map():
    df = pd.DataFrame(np.random.rand(100,4), columns=['A', 'B', 'C', 'D'])
    df.hist(column='A',figsize=(12,10))
    plt.show()

#get_hist_one_map()



