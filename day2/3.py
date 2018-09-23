# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:17:05 2018

@author: Thomas
"""

name = "thomas \t {tang}"
print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("ang"))#判断以什么结尾
print(name.expandtabs(tabsize=10))
print(name[name.find("o"):])
print(name[name.find("o"):6])
print(name.format(tang = "tangxu"))
print(name.format_map({'tang':"tangxu"}))
print(name.isalnum())#是否是阿拉伯字母或者数字，返回true或者false
print(name.isdecimal())#是否是十进制
print(name.isdigit())#是否为整数
print(name.isidentifier())#判断是不是一个合法的标识符/变量名
print(name.islower())#s是否为小写
print(name.isnumeric())#不常用，不知道什么意思
print(name.istitle())#是否是首字母大写
print(name.isprintable())#是否能打印，用途少，不需要记住
print(name.isupper())#是否为大写
print('+'.join(['1','2','3']))
print(name.ljust(50,'*'))
print(name.rjust(50,'*'))
print(name.lower())#把大写变成小写
print("\nThomas\n".lstrip())#去左边的空格或者回车
print("\nThomas\n".rstrip())#去左边的空格或者回车
print("\nThomas\n".strip())#去两边的空格或者回车
print('---')
print('Thomas\n'.translate(str.maketrans("abcmTs","123456")))#加密 密码
print(name.replace('T','t',1))#替换
print(name.rfind('T'))#找到最右边的一个的位置（可能包含几个的情况）
print('1+2+3+4'.split('+')) #按照空格来分割成列表,括号里的为分割的字符，会被去掉
print('1 2 3 4'.split()) #按照空格来分割成列表,括号里的为分割的字符，会被去掉
print('1\n 2\n 3\n 4\n'.splitlines)#按照换行符来分割
print("Thomas".swapcase)#大小写替换
print("Thomas".title)#
print('Thomas'.zfill(50))#不够的用0填充，非常少用，忘记吧
