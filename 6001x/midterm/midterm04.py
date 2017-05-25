# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 23:10:35 2016

@author: theresa
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    import math
    
    if num == 1:
        return 0
    if num < base: # it's going to be either 1 or 0
        if base - num < num - 1:
            return 1
        else:
            return 0
    
    max_exp = int(math.pow(num, 1/base)) + 2 # next bigger integer

    exponent = max_exp # answer is going to be closer to max_exp than to 1
    
    while num - (base ** exponent) < 0: # haven't gotten below the number yet
        exponent -= 1

    if abs(num - (base ** exponent)) > abs(num - (base ** (exponent+1))):
        return exponent + 1
    else:
        return exponent


base = 4
num = 160
print("answer = " + str(closest_power(base, num)))