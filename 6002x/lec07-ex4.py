#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:06:14 2017

@author: T. Swayne
"""

# lec07-ex4
# Compute the coefficient of variation 
# of [10, 4, 12, 15, 20, 5] to 3 decimal places.

def CoeffOfVar(L):
    ''' 
    L: list of floats 
    Returns the coefficient of variation of the values in L. 
    Return float('NaN') if L is empty.
    stdev = sqrt((summation of (t-mean)**2)/n)
    coefficient of variation is standard deviation divided by mean. 
    '''
    import numpy as np
    
    if len(L) == 0:
        return float('NaN')
    else:
        n = len(L)

    meanVal = np.mean(L)
#    print("mean",str(meanVal))
    
    sumSquaredDiffs = 0
    for x in L:
        sumSquaredDiffs += (x - meanVal)**2
    
#    print("sum",str(sumSquaredDiffs))
    
    result = (np.sqrt(sumSquaredDiffs/n))/meanVal
    return result


# --- testing ---

# L = ['a', 'z', 'p']
# L = ['apples', 'oranges', 'kiwis', 'pineapples']
#L = []
L = [10, 4, 12, 15, 20, 5]

# print("%.3f" % CoeffOfVar(L)) # note this truncates, does not round!
print(round(CoeffOfVar(L), 3))
