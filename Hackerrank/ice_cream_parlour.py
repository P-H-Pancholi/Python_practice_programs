# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:21:30 2019

@author: Phalin Pancholi
"""

def icecreamparlour(m,arr):
    """ returns 1 based indices of a and b such that 
        a + b = m
    """
    for a in arr:
        i = arr.index(a)
        if (m - a) in arr[i+1:]:
            q = arr[i+1:].index(m-a)
            print(str( i + 1) + " " + str(q + i + 2))
            return
i = int(input())
while i > 0:
    m = int(input())
    n = int(input())
    arr = [int(x) for x in input().split()]
    icecreamparlour(m,arr)
    i = i - 1