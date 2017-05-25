# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:09:02 2016

@author: theresa
"""

def newsearch(L, e):
    size = len(L)
    print(str(size))
    for i in range(size):
        print(i)        
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
    


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
 
L = [0,1]
e = 1

print("search found ",search(L,e))
print("newsearch found ",newsearch(L,e))