# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:02:58 2020

@author: user
"""


fstream1 = open("c:\python\homework1.txt" , mode ="a")
information = input("輸入資料:")
print(information, file=fstream1)
fstream1.close()
































