# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:40:58 2019

@author: Phalin Pancholi
"""

def inversebit(s):
    if s == '0':
        return '1'
    else:
        return '0'
def decimaltobinary(n):
    s = ''
    if n == 0:
        return '0'
    if n > 0:
        while n != 0:
            s = s + str(n % 2)
            n = n // 2
        return s[::-1]
    if n < 0:
        s = decimaltobinary(abs(n))
        Bflag = False
        temp = []
        for char in s[::-1]:
            if Bflag:
                temp.append(inversebit(char))
            else:
                temp.append(char)
                if char == '1':
                    Bflag = True
        s = "".join(temp)
        return s[::-1]
    
