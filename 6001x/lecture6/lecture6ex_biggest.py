# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 06:42:25 2016

@author: theresa
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    
    longest = 0
    if aDict == {}: # empty
        return None
    keys = aDict.keys()
    for item in keys:
        if len(aDict[item]) > longest:
            longest = len(aDict[item])
            longest_key = item
    return longest_key
    
        

#If there are no values in the dictionary, biggest should return None.

animals = {'d':['donkey','dingo','dog'], 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'],'e':['x','y']}

L = {}

print(biggest(animals))