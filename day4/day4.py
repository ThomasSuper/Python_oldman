# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:48:00 2018

@author: Thomas
"""
#内置函数
#print(abs(-1))#绝对值
#print(all([1]))#所有为真返回真
#print(any([1,0,3]))#任意一个为真，返回真
#print([ascii(["你好！"])])#很少用，将内存的数据对象转换成一个可打印的字符串
#print(bin(10))#将数据转换成二进制，前边加 ”0b“
#print(bool([1]))#判断真假

'''
a = bytes("abcde",encoding="utf-8")#字符串不能修改，二进制字节更不能修改
print(a)
print(a.capitalize())
print(a)


#很少用
b = bytearray("abcde",encoding="utf-8")#bytearray定义可修改的二进制列表
print(b[0])
b[1]=100 #给bytearray 赋值必须是二进制
print(b)
'''

#callable()#判断是否可调用
#chr(98)#返回ascii码对应的字符,必须输入数字
#ord('b')#返回ascii码对应的数字。必须输入字符
#@classmethod#类方法，后续再讲


#compile()#很少用到  底层用于把代码编译的过程，相当于import，但是可以实现动态的导入
#code = 'for i in range(10):print(i)'
#c = compile(code,'err.log','exec')#err.log错误日志打印
#exec(c)
#exec(code)#这样也可以执行
#
#complex() #复数 ，比较少用 
#delattr(object, name)#讲完面向对象再讲
#dict()#生成字典
#dir() #打印可以使用的方法，"__"的一般为系统自用
#divmod(a, b)#返回a/b（相除）的余数，也就是“熵”
#enumerate()#已经讲过
#eval()#将字符串str当成有效的表达式来求值并返回计算结果。简单的字符串，加减乘除等，复杂的用exec()
#exec()#
#匿名函数，使用一次就释放的函数，只能处理很简单的三元运算操作
#calc = lambda n:3 if n<4 else n
#print(calc(2))
#
#res = filter(lambda n:n>5, range(10))#对符合要求的（过滤）数据,打印出来
#print(type(res))
#for i in res:
#    print(i)


#res = map(lambda n:n*2,range(10))#map--对所有的值一一进行处理,返回一个列表
#for i in res:  #[lambda i:i*2 for i in range(10)]
#    print(i) # 整个等同于 [i*2 for i in range(10)] 

 
#import functools #python3中作为一个单独的模块来引用了    
#res = functools.reduce(lambda x,y:x+y,range(10))
##累加，就是一直操作，得到的值在赋给x（x存储结果），阶乘
#print(res)

#float()#浮点数
#format()#跟字符串里的format一样

#a = frozenset([1,4,22,56,88,9,23])#将集合变成不可修改

#getattr() 暂时没有讲
#a = 1
#print(globals())#返回这个文件的变量的名字和值,可以判断变量是否存在

#字典的实现就是通过映射关系，折半查找，取一半看在左还是在右，再取一半，这样的方式来查找
#print(type(hash("你好")))#通过一系列算法实现映射关系，MD5（用于比较文件是否相等）比哈希算法简单
#
#help()#查看帮助
#
#hex()#把一个数字转换为一个十六进制数
#
#id()#返回内存地址
#input()#
#int()#
#isinstance()#
#issubclass()#子类，讲类的时候再说
#iter()#迭代器
#len()#返回长度
#locals()#

#def test():很少用
#    local_var = 333
#    print(globals())#只打印全局变量
#    print(locals())#打印局部变量
#    
#test()
#
#print(globals())#只打印全局变量
#print(globals().get('local_var'))

#max()#返回最大值
#min()#返回最小值
#memoryview()#很少用
#
#next()#下一个（方法）
#class object#用类的时候生成对象，
# python 一切皆对象，世间万物皆对象，每个对象都对应属性
#oct()#8进制，少用
#open()
#pow(3,5)#返回x的y次方，等于x**y
#print()
#property()#以后讲，很重要
#range()
#print(type(repr(max(1,3))))#把一个对象转换成字符串
#reversed()#跟列表的是一样的
#print(round(1.235567,4)) #返回浮点数的小数点后“x”位的四舍五入值

#set()
#setattr()后边会讲

#a = range(10)
#b=a[slice(2,5)]#切片,很少用
#print(b)

##对所有可迭代的对象进行排序操作,返回一个列表。
#a = {6:2,3:8,4:6,0:9}
#b = sorted(a.items())#默认按照key排序
#c = sorted(a.items(),key= lambda x:x[1])#按照value排序
#print(b)
#print(c)
#print(type(a))
#print(type(b))


#staticmethod()#是一个方法，后边再讲
#str()#后边再讲
#sum()#把一个列表求和
#
#super()#是一个重要的继承的概念，面向对象的时候会讲
#tuple()#已经讲过，是列表转换为元组
#type()#返回数据类型，所有数据的类型都由type()演变而来
#
#
#vars()#返回对象的属性和属性值的字典对象，类似于local()

##zip,中文是指 “拉链“ 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
##然后返回由这些元组组成的列表。#如果各个迭代器的元素个数不一致，
##则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
#a = [1,2,3,4,5,6]
#b = ['a','b','c','d']
#for i in zip(a,b):
#    print(i)


__import__('sys')#引用模块的时候，用模块的字符串，非常有用





















































