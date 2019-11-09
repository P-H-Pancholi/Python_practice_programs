# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:17:17 2019

@author: Phalin Pancholi
"""

def jumpingonclouds(l):
    Count = 0
    n = 0
    if l[0] == 1:
        n = 1
    while(n+2 < len(l)):
        if l[n+2] == 0:
            Count += 1
            n += 2
        else:
            Count += 1
            n += 1
    if n < (len(l) - 1):
        Count += 1
    return Count

n = int(input())
s = [int(x) for x in input().split()]
ans = jumpingonclouds(s)
print (ans)
