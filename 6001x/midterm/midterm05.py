# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 00:41:51 2016

@author: theresa
"""
#
#Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32
#
#Hint: You will need to traverse both lists in parallel.
#
#This function takes in two lists of numbers and returns a number.

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    dot = 0
    for pos in range(0,len(listA)):
        dot += (listA[pos] * listB[pos])
    
    return dot

listA = [1,2,3]
listB = [4,5,6]
print(str(dotProduct(listA, listB)))
    