#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:28:22 2017

@author: T. Swayne
"""

from itertools import combinations

def powerSet(items):
#    if isinstance(items, str):
#        lst = list(items)
#    else:
    lst = items.copy()
    for i in range(len(lst)+1):
        for j in combinations(lst,i):
            yield (j)


# testing
items = ["bat"]

comboList = powerSet(items) # initialize the generator

for n in comboList: # get all the results the generator can yield
    print(n)
    