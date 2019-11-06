# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:26:48 2019

@author: Phalin Pancholi
"""

def decimaltobinary(n):
    """ Converts decimal into binary
    """
    s = ''
    if n > 0:
        while n != 0:
            s = s + str(n % 2)
            n = n // 2
        return s[::-1]
n = int(input())
if n == 0:
    i = 0
else:
    s = decimaltobinary(n)
    i = s.count('0')   #xor and add will be equal for nos with following property
                       #no of zeros in one binary no = no of ones in other 
print(2**i)            #binary no