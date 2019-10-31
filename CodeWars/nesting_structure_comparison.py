# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:05:20 2019

@author: Phalin Pancholi
"""

def same_structure_as(original,other):
    """Assumes original and other to be a list
        returns true if both the list has same nesting structure
    """
    if type(original) != type(other):
        return False
    if len(original) != len(other):
        return False
    i = min(len(original),len(other))
    for j in range(i):
        if type(original[j]) != type(other[j]) and (type(original[j]) == list or type(other[j]) == list):
            return False
        if type(original[j]) == list:
            return same_structure_as(original[j],other[j])
    return True
