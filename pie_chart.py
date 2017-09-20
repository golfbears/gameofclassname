# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:28:35 2017

@author: Administrator
"""
import numpy as np 
import pandas as pd 
import matplotlib. pyplot as plt # The slices will be ordered and plotted counter- clockwise. 

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs' #定义 标签 
sizes = [15, 30, 45, 10] #每 一块 的 比例 
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'] #每 一块 的 颜色 
explode = (0, 0.1, 0, 0) #突出 显示， 这里 仅仅 突出 显示 第二 块（ 即' Hogs'） 
plt.pie(sizes, explode= explode, labels= labels, colors= colors, autopct='%1.1f%%', shadow= True, startangle= 90) 
plt. axis('equal') #显示 为 圆（ 避免 比例 压缩 为 椭圆） 
plt. show()

x = np. linspace( 0, 2* np.pi, 50) #x 坐标 输入 
y = np. sin( x) #计算 对应 x 的 正弦 值 
plt. plot( x, y, 'bp--') #控制 图形 格式 为 蓝 色带 星 虚线， 显示 正弦 曲线 
plt. show()

x = np. random. randn( 1000) #1000 个 服从 正态分布 的 随机数 
plt. hist( x, 10) #分成 10 组 进行 绘制 直方图 
plt. show()



x = np. random. randn( 1000) #1000 个 服从 正态分布 的 随机数 
D = pd. DataFrame([ x, x+ 1]). T #构造 两 列 的 DataFrame 
D. plot( kind = 'box') #调用 Series 内置 的 作图 方法 画图， 用 kind 参数 指定 箱 形图 box 
plt. show()


