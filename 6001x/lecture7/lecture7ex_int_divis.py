# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:56:51 2016

@author: confocal
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0

    while x >= a:
        count += 1
        x = x - a
    return count
    

print(integerDivision(5,3))
