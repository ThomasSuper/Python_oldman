# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:51:02 2018

@author: Thomas
"""
#import json
#
#json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#print(json.loads(json_str))
#
#
##把变量从内存中变成可存储或传输的过程称之为序列化,在Python中叫pickling
##把变量内容从序列化的对象重新读到内存里称之为反序列化,即unpickling

#import  json
#eval将字符串转换成可以执行的代码，生成data1的字典
#f = open("text.txt","r")
#data = f.read()
#data1 = eval(data)
#print(type(data))
#print(type(data1))
#print(data1["name"])

#f = open("text.txt","r")
#data = f.read()
#data1 = json.loads(data) #反序列化用loads
#print(data1["name"])
#
#data2 = json.dumps(data1)   #序列化用dumps
#print(data2)
#f1 = open("text1.txt","w")
#f1.write(data2)

#json是用于不同语言之间的转换的标准，只能做简单的转换，比如：字典，列表等，
#pickle跟json用法一致，但是能处理复杂的数据，默认就是二进制，而且只能在python中使用，序列化整个数据（反序列化时只认函数名）
#python3中只能dump一次load一次，每dump一次都保存一个文件，这样才是标准做法