# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:55:09 2019

@author: Phalin Pancholi
"""

def marcscakewalk(arr):
    arr.sort(reverse = True)
    i = 0
    Sum = 0
    for e in arr:
        temp = e *(2**i)
        Sum += temp
        i += 1
    return Sum

n = int(input())
arr = list(map(int,input().split()))
print(marcscakewalk(arr))
    