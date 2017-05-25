# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:52:12 2016

@author: theresa
"""

foo = {'u': [10, 15, 5, 2, 6], 'B': [15], 'C':[3,5]}

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: str, how many values are in the dictionary.
    '''
    total = 0
    for item in aDict:
        if len(aDict[item]) == 1:
            total += 1
        else:
            total += len(aDict[item])
    return total

answer = str(how_many(foo))
print("total = "+answer)