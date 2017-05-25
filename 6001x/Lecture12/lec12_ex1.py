# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:16:15 2016

@author: theresa
"""

num = 1
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    val = L[L[val]]
    print(val)
print("final ",val)
    