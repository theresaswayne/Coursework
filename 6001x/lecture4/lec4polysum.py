# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:46:55 2016

@author: confocal
"""

import math # provides tan function and pi constant

def polysum(n,s):
    '''
    n = int, number of sides in a regular polygon
    s = float, length of each side of the polygon
    Returns the sum of the area and the square of the perimeter of the polygon
    '''
    perimeter = n*s
    area = (0.25 * n * s**2)/(math.tan(math.pi/n))
    ans = area + perimeter**2  # full precision
    roundAns = round(ans*10000)/10000 # restricts to 4 decimal places
    return roundAns


# testing
#n = 7
#s = 1
#print(polysum(n,s))
