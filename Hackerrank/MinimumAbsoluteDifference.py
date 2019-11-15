# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:34:08 2019

@author: Phalin Pancholi
"""

def minimumAbsoluteDifference(arr):
    temp = sorted(arr)
    n = len(arr)
    Min = abs(arr[0] - arr[1])
    for i in range(n - 1):
        diff = abs(temp[i] - temp[i+1])
        if diff <= Min:
            Min = diff
    return Min

n = int(input())
arr = list(map(int,input().split()))
print(minimumAbsoluteDifference(arr))