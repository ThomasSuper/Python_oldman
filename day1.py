# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:07:51 2018

@author: Thomas
"""

import sys

user_info_file_path = "user_info.txt"
user_lock_file_path = "user_lock.txt"

def open_file(file_path): 
    with open(file_path) as file_info:    
        list_file_info = file_info.readlines() 
        #print(list_file_info)                
    return list_file_info   



def main():
    #循环开始
    count = 0
    while count < 3:
        #输入用户名
        user_name = input("用户名:")  
        #打开被锁定名单     
        list_user_lock = open_file(user_lock_file_path)
        #判断用户名是否被锁定
        for check_user_name in list_user_lock:
            if user_name + '\n' == check_user_name:
                print('用户 %s 已经被锁定,请联系管理员解锁.' % user_name)
                print("拜拜!")
                sys.exit() 
                
        #读取用户信息        
        list_user_info = open_file(user_info_file_path)        
        #判断用户是否正确
        if user_name + '\n' in list_user_info: 
            count_1 = 0
            while count_1 < 3:               
                password = input("password:")
                if password + '\n' == list_user_info[1]:       
                    print("嗨,{_username},欢迎登陆! ".format(_username = user_name))
                    sys.exit()    
                else:
                    if count_1 ==2:
                        with open(user_lock_file_path,'w') as list_user_lock_:
                            list_user_lock_.write(user_name + '\n')
                            print("{_username}已被锁定，请联系管理员!".format(_username = user_name))
                            sys.exit() 
                    count_1  += 1
                    if (3-count_1) > 0:
                        print("密码错误，请重试，你还有 %d 次机会!"% (3-count_1))

        #用户名不存在
        else:
            count  += 1
            if (3-count) > 0:
                print("用户不存在，请重试，你还有 %d 次机会!"% (3-count))
            else:
                print("拜拜!")
                #sys.exit()     
                
if __name__ == "__main__":
    main()
            
        
            
            
    