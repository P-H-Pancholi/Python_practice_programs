# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:49:01 2019

@author: Phalin Pancholi
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 1:
        return aStr[0] == char
    else:
        n = len(aStr) 
        if aStr[n//2] == char:
             return True
        elif aStr[n//2] > char:
             return isIn(char, aStr[:n//2])
        else:
             return isIn(char, aStr[n//2:])
