# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 09:56:32 2018

@author: Thomas
"""

'''
import sys
print("-->","\n".join(sys.path))
print("-->",sys.argv)
print("-->",sys.argv[0])

import os
print("-->",os.path)

cmd_res = os.popen("dir").read()
print("-->",cmd_res)
#在当前目录新建文件夹
#os.mkdir("test")
'''
'''
msg = "我爱深圳"
print(msg.encode(encoding = "utf-8"))

msg1 = b'\xe6\x88\x91\xe7\x88\xb1\xe6\xb7\xb1\xe5\x9c\xb3'
print(msg1.decode(encoding = "utf-8"))
'''

import copy

names = ["tangxu","zhangsan","lisi","wanger"]

names.append("WuAnyan") #新增
names.insert(1,"ShunWukong") #插入
print(names)

names[1]="Shashen"   #修改

names.remove("WuAnyan")#删除
del names[-1]#删除

print(names[names.index("tangxu")])#索引
print(names.count("tangxu"),"统计")#统计

print(names)
names.pop(1)#弹出

print(names)
print(names[0],names[2]) #读值

#顾头不顾尾 
print(names[0:3]) #切片 list
print(names[-1]) #切片 str
print(names[:-2]) #切片 list

print(names[0:3:2]) #步长切片 list  类似于range（1，10，2）
print(names[::2]) #步长切片

names.reverse()#反转
names.sort()#排序

names2=["Tangshen"]
names.extend(names2)#扩展 
print(names,"扩展")

n1 = names.copy()#复制 浅copy，只copy第一层,第二层的内容保持一致（可以利用，
#比如夫妻共同拥有一个账号，一旦修改，对应的值2个列表都会变）， 有以下四个方法
n2 = names[:]
n3 = list(names)
n4 = copy.copy(names)

names5 = copy.deepcopy(names)#复制 深copy，完全独立
print(n1,"names3")
print(names5,"names5")


for i in names:  #循环
    print(i)

names.clear()#清空
print(names,"Clear")
print(n1,"names3 @names2 Clear")

#引用？？？？




