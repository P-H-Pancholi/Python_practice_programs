# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:35:39 2019

@author: Phalin Pancholi
"""

class bigin(str):
    def __init__(self, s_int = ''):
        self.s_int = s_int
    def __gt__(self, other):
        if len(self.s_int) == len(other.s_int):
            return self.s_int > other.s_int
        else:
            return len(self.s_int) > len(other.s_int)
    def __lt__(self, other):
        if len(self.s_int) == len(other.s_int):
            return self.s_int < other.s_int
        else:
            return len(self.s_int) < len(other.s_int)        
    def setbigin(self, itera):
        self.s_int = itera
    def getbigin(self):
        return self.s_int
    def __str__(self):
        return (self.s_int)

t_list = []
i = int(input())
while i > 0:
    j = input()
    t_list.append(bigin(j))
    i = i - 1
t_list.sort()
for e in t_list:
    print(e)
    
        
