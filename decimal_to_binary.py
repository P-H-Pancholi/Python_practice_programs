# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:40:58 2019

@author: Phalin Pancholi
"""

num = int(input("Enter the number: "))
if num < 0:
    IsNeg = True
    num = abs(num)
else:
    IsNeg = False
result = " "
if num == 0:
    result = '0'
while num > 0:
    result = result + str(num % 2)
    num = num//2
if IsNeg:
    result = "-" + result
print(result)
    
    