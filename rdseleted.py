# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:24:50 2017

@author: Administrator
"""
import matplotlib
import matplotlib.pyplot as plt
from numpy import *
nameofClass = {'唐林':{1:20},'万家旭':{2:9},'韩金阳':{3:134},'黄斌':{4:169},'方嘉玮':{5:786},\
                '王延飞':{6:201},'廖明江':{7:217},'王晓虎':{8:209},'商礼军':{9:210},'陈建锋':{10:224},\
                '李雪源':{11:225},'何铭华':{12:243},'魏勺增':{13:244},'黄宝剑':{14:245},'苑凯全':{15:216},\
                '严秦':{16:9},'李恒':{17:9},'戴林杰':{18:9},'张子建':{19:9},'孙唯':{20:9}, \
                '刘潇潇':{21:59},'秦茹':{22:43},'胡康莉':{23:100},'陆恬恬':{24:200},\
                '沈涛':{25:154},'宋静':{26:9},'彭瑶':{27:9},'黄勇':{28:9},'樊治康':{29:9},\
                '黄春娇':{30:183},'陈勤':{31:54},'奚嘉洁':{32:118}
                }
myClass = int(random.uniform(1,33))
#print myClass
for v in nameofClass:
   # print v, nameofClass[v].keys()
    if myClass == nameofClass[v].keys()[0]:
        print v
        
fig = plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),40.0*array(datingLabels))        
plt.show()

fig = plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))        
plt.show()

fig = plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))        
plt.show()
