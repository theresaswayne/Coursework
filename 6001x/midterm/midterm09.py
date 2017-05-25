# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 23:56:06 2016

@author: theresa
"""

#Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''

    flatList = []
    for thing in aList:
        if (type(thing) == str) or (type(thing) == int): #base case, already flat
            flatList.append(thing) # adds the thing itself to the list
            
        elif type(thing) == list: 
            flatList.extend(flatten(thing)) # adds *elements of* thing to the list
            
    return flatList
    
# testing area

L = [[[[[5,6]],[6,7]],8,9,'the',[]]]
# L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

M = flatten(L)
print(M)
