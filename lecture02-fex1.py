#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 23:32:06 2017

@author: theresa
"""

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # Instead of a bitwise binary shift as for 2 items,
            # you divide by 3**j to find location of item j
            if (int(i/(3**j)) % 3 == 0):
                continue
            elif (int(i/(3**j)) % 3 == 1):
                combo1.append(items[j])
            elif (int(i/(3**j)) % 3 == 2):
                combo2.append(items[j])
        yield (combo1, combo2)
        
# testing
items = ["bat", "ball", "glove"]

comboList = yieldAllCombos(items) # initialize the generator

for n in comboList: # get all the results the generator can yield
    print(n)
