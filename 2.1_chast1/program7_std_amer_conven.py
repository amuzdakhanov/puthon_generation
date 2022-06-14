#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:42:56 2022

@author: ars
"""


def calculate (n):
    counter = 3
    len_n = len(n)
    rn = n[::-1]
    if len_n > 2:
        for i in range (len_n):
            if counter % 3 == 0:
                list_n.append(',')
                list_n.append(rn[i])
            
            else:
                list_n.append(rn[i])
            counter += 1
        if list_n[0]==',':
            del list_n[0]
        return list_n[::-1]
    elif len_n < 3:
        return list(n)


n = int(input())
flag = True
if  n < 0:
    flag = False
    n = str(n * (-1))
else:
    n = str(n)

list_n = []

if flag == True:
    print(*calculate(n),sep=(''))
else:
    print('-',*calculate(n),sep=(''))