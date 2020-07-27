# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:41:08 2020

@author: user
"""



fstream1 = open("c:\python\homework.txt" , mode ="x")
name = input("請輸入姓名:")   
birthday = input("請輸入生日:")
age = input("請輸入年齡:")
print("姓名:{0}\n生日:{1}\n年齡:{2}".format(name,birthday,age), file=fstream1)
fstream1.close()