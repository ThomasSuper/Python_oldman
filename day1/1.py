# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 09:26:58 2018

@author: Thomas
"""
'''
name = "Thomas"
name2 = name
print(name,name2)
name = "Thomas_tang"
print(name,name2)

姓名 = "Thomas_tangxu"
print(姓名)
'''

name = input("name:")
age = int(input("age:"))
print(type(age))
job = input("job:")
salary = input("salary:")

info = '''
----------info of {_name}--------------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)


info2 = '''
------------info of %s-----------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (name,name,age,job,salary)

print(info2)




