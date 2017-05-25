# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 09:07:39 2016

@author: theresa
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    
    d_intersect = {} #empty dict
    d_diff = {}
    
    #find intersection

    for key in d1:
        if key in d2:
            d_intersect[key] = f(d1[key],d2[key])

    # find diff
    
    for key in d1:
        if key not in d2:
            d_diff[key] = d1[key]

    for key in d2:
        if key not in d1:
            d_diff[key] = d2[key]
    
    return (d_intersect, d_diff)

# testing block

def f(x,y):
    '''
    x, y: ints
    returns sum
    '''
    return x + y

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))