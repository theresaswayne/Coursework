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
    print("N = "+str(N))
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        # Vary something to get each possibility, one at a time
        for j in range(N):
            print("i = "+ str(i),"j = "+str(j),"test = "+str(int(i/(3**(N-j)))))
            # Test condition to see where to put items
            if (int(i/(3**j)) % 3 == 0):
                continue
            elif (int(i/(3**j)) % 3 == 1):
                combo1.append(items[j])
            elif (int(i/(3**j)) % 3 == 2):
                combo2.append(items[j])
        yield (combo1, combo2)
        
    # note there are 3**N possible combinations for the 2-bag problem.
    # "You can imagine this by representing the two bags 
    # as a list of "trinary" bits, 0, 1, or 2 
    # (a 0 if an item is in neither bag; 1 if it is in bag1; 2 if it is in bag2). "
    # Try to represent as a list of length N
    # where each element i is the location of items[i]. 
    # Go through this list and if the element is 1 
    # append the corresponding item to bag1 etc.
    
#    Use modulo 3
#But instead of a bitwise binary shift you divide by 3 to some power
# int(i/3) % 3

# int(i/(3**(N-j) % 3
#Loop j from 0 to N+1
#Look at i/(3^(N-j)) % 3
#
#That gives you the location of item j


# testing
items = ["bat", "ball", "glove"]

comboList = yieldAllCombos(items) # initialize the generator

for n in comboList: # get all the results the generator can yield
    print(n)

# print(next(comboList))    
# print(next(comboList))

# TODO: figure out representation of 3 bits 
