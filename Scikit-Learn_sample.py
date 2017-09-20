# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:16:27 2017

@author: Administrator
"""

from sklearn import datasets #导入 数据 集 
iris = datasets.load_iris() #加载 数据 集 
print(iris.data.shape) #查看 数据 集 大小 
from sklearn import svm #导入 SVM 模型 
clf = svm.LinearSVC() #建立 线性 SVM 分类器 
clf.fit( iris.data, iris.target) #用 数据 训练 模型 
clf.predict([[ 5.0, 3.6, 1.3, 0.25]]) #训练 好 模型 之后， 输入 新的 数据 进行 预测 
clf.coef_ #查看 训练 好 模型 的 参数

