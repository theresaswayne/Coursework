# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:20:32 2016

@author: confocal
"""



def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    guessIndex = int(len(aStr)/2)
    
    if aStr == "":
        return False
    
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    elif char == aStr[guessIndex]:
        return True
    elif char < aStr[guessIndex]: # the char is earlier in the string
        return isIn(char, aStr[0:guessIndex]) # search 
    elif char > aStr[guessIndex]:
        return isIn(char, aStr[guessIndex:])

#test
#char = "t"
#aStr = "adefs"
#print(isIn(char, aStr))
