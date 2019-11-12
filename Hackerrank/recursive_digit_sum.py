# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def super_digit(m,n):
    """Returns the sum of digits recursively of 
       number m concatinated n times 
    """
    s = str(m)
    if len(s) == 1:
        if n == 1:
            return m
        return super_digit(m*n,1)
    else:
        Sum = 0
        for char in s:
            Sum = Sum + int(char)
        m = Sum
        return super_digit(m,n)

m,n = map(int,input().split())
print(super_digit(m,n))

            
