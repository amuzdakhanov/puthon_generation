#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:56:38 2022

@author: ars
"""

n = int(input())
k = int(input())
list_n = [int(i) for i in range(1,n+1)]
len_n = len(list_n)
while len_n > 1:
    for i in range(k-1):
        list_n.append(list_n[i])
    del list_n[:k]
    len_n -= 1
print(*list_n)
