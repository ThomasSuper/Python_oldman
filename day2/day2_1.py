# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 17:17:32 2018

@author: Thomas
"""
'''
#购物车 
输入金额后->显示商品，价格->选中商品后->
加入购物车->自动扣除货款->余额不足时提醒->输入“q“后打印已选择的商品，并退出程序.
'''
#import sys
product_file = "product_list.txt"
shoping_file = "shoping_list.txt"
product_list = []
#读一个txt文件，返回一个列表
def read_file(product_file):
    product_1 = []
    product_2 = []
    with open(product_file) as product:
        product_list = product.readlines()
        for i in product_list:
            i = i.strip()
            product_1.append(i.split(","))
            
        for j in product_1:
            j[0]=int(j[0])   
            j[2]=int(j[2]) 
            product_2.append(j)
        return product_2
#product_list = read_file(product_file)       
#print(product_list,"-->") 
Cord_Balance = 0

List_Inventory= read_file(product_file)
List_Shoping = []

print(List_Inventory) 

Cord_Balance = int(input("Please input the money:"))
while True:
    print(List_Inventory,"\n")
    Number_Choose = input("Please choose goods:")
    if Number_Choose == "q":
        print("You have choosed:",List_Shoping)
        with open(shoping_file,'w') as shoping_list:
            shoping_list.write(str(List_Shoping))
        print("Your Cord_balance is: %d" % Cord_Balance)
        break
    #elif Number_Choose in List_Inventory:
    else:       
        Pice =(List_Inventory[int(Number_Choose)-1][2])
        if Cord_Balance > Pice: 
            Cord_Balance = Cord_Balance - Pice  
            List_Shoping.append(List_Inventory[int(Number_Choose)-1])               
            print("You have choosed:",List_Shoping)
            print("Your Cord_balance is: %d" % Cord_Balance,"\n")
        else:
            print("Your Insufficient balance,Please Choose else goods!")























