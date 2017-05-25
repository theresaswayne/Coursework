#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:06:14 2017

@author: T. Swayne
"""

# lec07-ex3

def stdDevOfLengths(L):
    ''' 
    Write a function, stdDevOfLengths(L) that takes in a list of strings, L, 
    and outputs the standard deviation of the lengths of the strings. 
    Return float('NaN') if L is empty.
    stdev = sqrt((summation of (t-mean)**2)/n)
    '''
    import numpy as np
    
    lengths = []
    for str in L:
        lengths.append(len(str))
    
    if len(lengths) == 0:
        return float('NaN')
    else:
        n = len(lengths)

    meanLength = np.mean(lengths)
    
    sumSquaredDiffs = 0
    for x in lengths:
        sumSquaredDiffs += (x - meanLength)**2
    
    result = np.sqrt(sumSquaredDiffs/n)
    return result


# --- testing ---

# L = ['a', 'z', 'p']
# L = ['apples', 'oranges', 'kiwis', 'pineapples']
L = []
print(stdDevOfLengths(L))
