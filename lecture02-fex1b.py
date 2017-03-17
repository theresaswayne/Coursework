#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 23:32:06 2017

@author: theresa
"""
# Practice using the itertools module instead of 
# binary representation of the combinations

def powerSet(items):
    '''
    generator to produce all possible combinations
    from a set of items
    items: list
    each time called, produces a list representing one combination
    '''
    from itertools import chain, combinations
    N = len(items)
    combo = []
    # itertools.combinations produces sets of a specific size
    # the r loop gives all possible set sizes ≤ the number of items
    # chain.from_iterable 'flattens' the list -- no internal tuples or lists 
    for combo in chain.from_iterable(combinations(items, r) for r in range(N+1)):
        yield combo

# testing
items = ["bat", "ball", "glove"]

comboList = powerSet(items) # initialize the generator

for n in comboList: # get all the results the generator can yield
    print(n)
