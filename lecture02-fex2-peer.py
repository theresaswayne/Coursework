#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 20:44:15 2017

@author: T. Swayne
"""

# -*- coding: utf-8 -*-
from itertools import chain, combinations


def powerset_generator(i):
    for subset in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
        yield set(subset)

# testing
items = ["bat", "ball", "glove"]

comboList = powerset_generator(items) # initialize the generator

for n in comboList: # get all the results the generator can yield
    print(n)