# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:22:19 2019

@author: Phalin Pancholi
"""

def funnystring(s):
    temp_list = []
    rtemp_list = []
    for e in s:
        temp_list.append(ord(e))
    for e in s[::-1]:
        rtemp_list.append(ord(e))
    for i in range(0,len(s)-1):
        if abs(temp_list[i] - temp_list[i+1]) != abs(rtemp_list[i] - rtemp_list[i+1]):
            return False
    return True
i = int(input())
while i>0:
    s = input()
    myflag = funnystring(s)
    if myflag:
         print('Funny')
    else:
        print('Not Funny')
    i = i-1
