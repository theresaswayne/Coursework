# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 07:43:26 2016

@author: theresa
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    import string # to get list of letters

    availLett = ""
    
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            availLett += letter

    return availLett
    
secretWord = 'bicycle' 
lettersGuessed = ['x','d','e', 'i', 'k', 'p', 'r', 's', 'c']
print(getAvailableLetters(lettersGuessed))
