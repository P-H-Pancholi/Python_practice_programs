# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:28:48 2020

@author: Phalin Pancholi
"""

def in_array(array1,array2):
    """returns sorted array of the strings present in array1 
        and are substrings of strings in array2
    """
    s = []
    for char1 in array1:
        for char2 in array2:
            if char1 in char2:
                if char1 not in s:
                    s.append(char1)
    return sorted(s)