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
Cord_Balance = 0

List_Inventory= [[1,"Iphone 6s",4300],[2,"Guiter",650],[3,"watch",350],[4,"bicycle",300],[5,"Cup",30]]
List_Shoping = []

Cord_Balance = int(input("Please input the money:"))
while True:
    print(List_Inventory,"\n")
    Number_Choose = input("Please choose goods:")
    if Number_Choose == "q":
        print("You have choosed:",List_Shoping)
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
    
