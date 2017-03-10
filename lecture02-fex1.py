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
    # this is the original code for 1 bag
    # generate all combinations of N items
    N = len(items)
    # print("N = "+str(N))
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        # print("i = "+ str(i))
        combo = []
        for j in range(N):
            # print("j = "+str(j))
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
    # note there are 3**N possible combinations for the 2-bag problem.
    # "You can imagine this by representing the two bags 
    # as a list of "trinary" bits, 0, 1, or 2 
    # (a 0 if an item is in neither bag; 1 if it is in bag1; 2 if it is in bag2). "
    
    
# testing
items = ["bat", "ball", "glove"]

comboList = yieldAllCombos(items) # initialize the generator

for n in comboList: # get all the results the generator can yield
    print(n)

# print(next(comboList))    
# print(next(comboList))

# TODO: figure out representation of 3 bits 
