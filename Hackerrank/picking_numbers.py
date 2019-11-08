# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:21:42 2019

@author: Phalin Pancholi
"""

def pickingnumbers(arr):
    """Returns length of maximum subarray of arr such that
       the absolute difference between its all element is 1
    """
    temp = []
    Sum = 0
    max_sum = 0
    for e in arr:
        if e not in temp:
            Sum = arr.count(e) + arr.count(e+1)
            temp.append(e)
            if(Sum > max_sum):
                max_sum = Sum
    print(max_sum)
    return max_sum

i = int(input())
a = list(map(int,input().split()))
pickingnumbers(a)