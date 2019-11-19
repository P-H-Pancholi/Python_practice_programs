# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:45:57 2019

@author: Phalin Pancholi
"""



def isSorted(arr):
    return arr == sorted(arr)
def gridChallenge(arr,n):
    for i in range(n):
        if not(isSorted(arr[i::n])):
            return "NO"
    return "YES"
i = int(input())
while i > 0:
    n = int(input())
    arr = []
    for j in range(n):
        temp_list = list(input())
        temp_list.sort()
        arr = arr + temp_list
    print(gridChallenge(arr,n))
    i -= 1

    