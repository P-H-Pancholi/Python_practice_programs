# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:47:55 2019

@author: Phalin Pancholi
"""

def beautifullTriplets(a,d):
    """Assumes a to be list of int in increasing order and d to be an int
       returns number of triplets having the difference of d between them
    """
    
    n = len(a)
    Count = 0
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            if (a[j] - a[i]) > d:    #if the difference increases move to next value of i
                break
            if (a[j] - a[i]) == d:
                for k in range(j,n):
                    if ((a[j] - a[i]) == (a[k] - a[j])) and ((a[k] - a[j]) == d):
                        Count += 1
    return Count
s = input().split()
a = [int(x) for x in input().split()]
ans = beautifullTriplets(a, int(s[-1]))
print(ans)

                    


                    