# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:27:31 2018

@author: Thomas
"""
import sys
import time
#data = open("txt.txt",encoding="utf-8").read()
#print(data)

f = open("txt.txt","a",encoding = "UTF-8")#文件句柄，文件的内存、对象，起始位置，大小等
#a= append  追加 能写不能读
#r 能读 不能写
#w 能写 不能读
#r+ 读写
#W+ 写读 很少用
f = open("txt.txt","rb")
#rb 二进制读取，用在网络传输上
f = open("txt.txt","wb")
f.write("hello binary\n".encode())
'''
for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)
''' 
'''
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())

print(f.encoding)#返回编码类型

print(f.fileno())#文件在内存的编号
print(f.isatty())#打印机交互
print(f.seekable())#是否可以移动光标
print(f.readable())#判断文件是否可读
print(f.flush())#刷新一下，内存数据往硬盘写入,
#可以不缓存，直接写硬盘，每次强制刷新
print(f.buffer)#
''' 

#f.write("hello 1\n")
f.seek(5)
f.truncate(1)#传递函数不写就是清空
#传递多少数量都只能从头开始截断，保留前多少个数据

  
'''
data1= f.read()
data2=f.read()
print(data1)
print(data2)
'''


#with open("txt.txt",enconding="utf-8") as data1:
#f.write("你好，测试-------\n")
#print(f.read())

#print(f.readline())

'''
for index,line in enumerate(f.readlines()): 

    if index == 5:
        print("------我是分割符------")
        continue
    print(line.strip())
    '''
'''    
#高效的循环方法
count = 0    
for line in f:
    count +=1
    if count ==5:
        print("------我是分割符------")
        continue
    print(line.strip())
'''



f.close()