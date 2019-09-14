# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:02:28 2019

@author: Phalin Pancholi
"""
i = int(input())
for j in range(i):
    l = [int(x) for x in input().split()]
    l = sorted(l)
    n = int(len(l)//2)
    print(str(l[n]))
    