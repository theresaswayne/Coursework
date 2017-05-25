# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 23:15:40 2016

@author: theresa
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    # preserve elements such that g(f(i)) is True

    Saved_elements = [] # list to store the saved elements
    
    for i in L: # ok to iterate over the list because not changing it now
        if g(f(i)):
            Saved_elements.append(i) 
    
    # mutate L to include only those saved values

    L_copy = L[:] # clone of L to iterate while we mutate L    
       
    for i in L_copy: # iterate over the clone
        if i not in Saved_elements:
            L.remove(i)
        
    # find the largest element in the resulting list
     
    if L == []:  # empty list 
        return -1
    else:
        return max(L)


# testing area

def f(i):
    return i * -1
def g(i):
    return i < 5

L = [6,-10,10,0,5]
print(applyF_filterG(L, f, g))
print(L)