# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:56:18 2019

@author: Phalin Pancholi
"""

def narcissistic( value ):
    n = len(str(value))
    Sum = 0
    for i in range(n):
        a = str(value)[i]
        Sum += int(a)**n
    if Sum == value:
        return True
    else:
        return False
