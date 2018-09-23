# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 01:10:21 2018

@author: Thomas
"""
#key - value

info = {
        'stul101':"TengLan Wu",
        'stul102':"Longze Luola",
        'stul103':"Xiaoze Maliya"
        }

info_1 = {
        'stul101':"TengLan Wu",
        'stul102':"Longze Luola",
        'stul103':"Boduo"
        }

print(info["stul101"])#查找，确定有这个值才用这个办法
print(info.get("stul108"))#安全查找，不存在返回 null
print('stul104' in info)#判断是否存在

info["stul101"] = "武藤兰"
print(info["stul101"])

info["stul104"] = "苍井空"#不存在就创建一条  新建
print(info["stul104"])

#del info["stul101"]#删除
info.pop("stul101")#标准删除
info.popitem()#随便删除，位置位置

print(info)


info.update(info_1)#合并 交叉的更新，不存在的直接添加
print(info.items())
print(dict.fromkeys([6,7,8]))#初始化一个字典，赋值key，值为null，慎用，忘记吧

for i in info:
    print(i,info[i])  #循环