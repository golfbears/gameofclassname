# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:27:09 2017

@author: Administrator
"""

from keras.models import Sequential 
from keras.layers.core import Dense, Dropout, Activation 
from keras.optimizers import SGD 

model = Sequential() #模型 初始化 
model.add( Dense( 20, 64)) #添加 输入 层（ 20 节点）、 第一 隐藏 层（ 64 节点） 的 连接 
model.add( Activation(' tanh')) #第一 隐藏 层 用 tanh 作为 激活 函数 
model.add( Dropout( 0.5)) #使用 Dropout 防止 过 拟 合 
model.add( Dense( 64, 64)) #添加 第一 隐藏 层（ 64 节点）、 第二 隐藏 层（ 64 节点） 的 连接 
model.add( Activation(' tanh')) #第二 隐藏 层 用 tanh 作为 激活 函数 
model.add( Dropout( 0.5)) #使用 Dropout 防止 过 拟 合 
model.add( Dense( 64, 1)) #添加 第二 隐藏 层（ 64 节点）、 输出 层（ 1 节点） 的 连接 
model.add( Activation(' sigmoid')) #输出 层 用 sigmoid 作为 激活 函数 
sgd = SGD( lr= 0.1, decay= 1e-6, momentum= 0.9, nesterov= True) #定义 求解 算法 
model.compile( loss=' mean_ squared_ error', optimizer= sgd) #编译 生成 模型， 损失 函数 为 平均 误差 平方 和 
model.fit( X_train, y_train, nb_epoch= 20, batch_size= 16) #训练 模型 
score = model.evaluate( X_test, y_test, batch_size= 16) #测试 模型

