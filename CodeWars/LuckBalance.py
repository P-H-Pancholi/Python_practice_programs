# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:04:46 2019

@author: Phalin Pancholi
"""
def luckBalance(arr,k):
    """Assumes arr to be a list and k to be an int
        returns sum of elements in sorted order 
        upto k and subtracts
        the other ones
    """
    i = len(arr)
    arr.sort()
    Count = 0
    for j in range(i):
        if j >= (i-k):
            Count += arr[j]
        else:
            Count -= arr[j]
    return Count
            
n,k = map(int,input().split())
Sum = 0
arr = []
for j in range(n):
    m,it = map(int,input().split())
    if it == 0:
        Sum += m
    else:
        arr.append(m)
print(Sum + luckBalance(arr,k))
