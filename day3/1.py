# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:45:41 2018

@author: Thomas
"""

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

list_1.add(999)
list_1.update([888,777,666,555])
list_1.remove(666)#删除，会报错
list_1.discard(555)#删除，不会报错

len(list_1)
if '777' in list_1:
    print(list_1)

list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)

print(list_1.pop())#删除并返回任意一个
#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
#并集
print(list_1.union(list_2))
print(list_1 | list_2)
#差集
print(list_1.difference(list_2))
print(list_1 - list_2)#in list1 but not in list2
print(list_2.difference(list_1))
print(list_2 - list_1)#in list1 but not in list2
#子集
list_3 = set([1,3,7])
print(list_1.issubset(list_3))

#父集
print(list_1.issuperset(list_3))

#对称差集 = 并集-交集
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)#对称差集

#没有交集返回True
list_4 = set([5,6,8])
print(list_3.isdisjoint(list_4))


