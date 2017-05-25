# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 07:38:42 2016

@author: theresa
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    guessedWord = ""
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessedWord += " _"
        else:
            guessedWord += letter
    
    return guessedWord
    
secretWord = 'bicycle' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'c']
print(getGuessedWord(secretWord, lettersGuessed))