#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 22:42:42 2017

@author: T. Swayne
"""

#
#If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
#If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
#If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]

# option 2 -- breadth-first search 
# because we want the fewest items that give the right total

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    import numpy as np

    def binArray(num, length):
        ''' converts num (integer) to numpy array
        whose elements comprise the binary 
        of the int, padded to length (integer)
        '''
        binList = list(bin(num)[2:])
        while len(binList) < length:
            binList.insert(0,'0')
        listInts = [int(item) for item in binList]
        listArray = np.array(listInts)
        return listArray
        
    numItems = len(choices)
    numCombos = 2**(numItems)

    choicesArray = np.array(choices)

    closestTotal = 0
    leastNumChosen = len(choices)+1
    bestSelection = np.array([])
    bestImperfect = np.array([0 for i in range(numItems)])
    
    for i in range(numCombos): # search all until find the best
        selection = binArray(i,numItems)
        
        # check if it meets the first criterion
        thisTotal = sum(selection * choicesArray)
        if thisTotal == total:
            # check if it is the best at second criterion
            if sum(selection) < leastNumChosen: # this is better than previous
                leastNumChosen = sum(selection)
                closestTotal = total
                bestSelection = selection
        elif (thisTotal < total and thisTotal > closestTotal): # closer but not going over
            closestTotal = thisTotal
            bestImperfect = selection
        else: # thisTotal went over
            continue # the for loop
    
    if bestSelection.size == 0: # empty
        # e.g. if every sum went over
        return bestImperfect
    else:
        return bestSelection

#choices = [1,1,1]
#total = 3

#choices = [1,1,3,5,3]
#total = 5
#choices = [1,2,2,3]
#total = 4
#print(find_combination(choices,total))
print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171))

# ---- grader responses
# fails on boundary conditions?

#Test: find_combination([10, 100, 1000, 3, 8, 12, 38], 1171)
#Your output:
#[]
#Correct output:
#array([1, 1, 1, 1, 1, 1, 1])
#
#print(find_combination([1, 3, 4, 2, 5], 16))
#Your output:
#[]
#Correct output:
#array([1, 1, 1, 1, 1])
#
#print(find_combination([4, 10, 3, 5, 8], 1))
#Test: find_combination([4, 10, 3, 5, 8], 1)
#Your output:
#[]
#Correct output:
#array([0, 0, 0, 0, 0])
#Test: find_combination([1, 81, 3, 102, 450, 10], 9)
#print(find_combination([1, 81, 3, 102, 450, 10], 9))
#Your output:
#[]
#Correct output:
#array([1, 0, 1, 0, 0, 0])
#
#Test: find_combination([1], 10)
#print(find_combination([1], 10))


#Your output:
#[]
#Correct output:
#array([1])