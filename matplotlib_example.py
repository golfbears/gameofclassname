# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:07:24 2017

@author: Administrator
"""


import numpy as np 
import matplotlib. pyplot as plt #导入 Matplotlib 
plt. rcParams['font.sans-serif'] = ['SimHei'] #这 两句 用来 正常 显示 中文 标签
#plt. rcParams['axes.unicode_minus'] = False #解决 保存 图像 是 负号'-' 显示 为 方块 的 问题



x = np. linspace( 0, 10, 1000) #作图 的 变量 自变量 
y = np. sin( x) + 1 #因变量 y 
z = np. cos( x** 2) + 1 #因变量 z 
plt. figure( figsize = (8, 4)) #设置 图像 大小 
plt. plot( x, y, label = '$\sin x+ 1$', color = 'red', linewidth = 2) #作图， 设置 标签、 线条 颜色、 线条 大小 
plt. plot( x, z, 'b--', label = '$\cos x^ 2+ 1$') #作图， 设置 标签、 线条 类型 
plt. xlabel(' Time( s) ') # x 轴 名称 
plt. ylabel(' Volt') # y 轴 名称 
plt. title(' A Simple Example') #标题 
#plt. title('简单例子') #标题 
plt. ylim(0, 2.2) #显示 的 y 轴 范围 
plt. legend() #显示 图例 
plt. show() #显示 作图 结果

