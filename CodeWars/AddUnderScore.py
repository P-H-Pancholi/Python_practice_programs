# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:12:31 2019

@author: Phalin Pancholi
"""

def to_underscore(string):
    if type(string) != str:
        return string
    s = str.lower(string[0][:])
    i = 0
    while i < len(string) - 1:
        i += 1
        if not(str.isupper(string[i])):
            s = s + string[i]
            continue
        s = s + "_" + str.lower(string[i])
    return s
