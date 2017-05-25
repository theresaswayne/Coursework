# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:39:55 2016

@author: confocal
"""

from ps4a import * 
from ps4b import *
# print(getWordScore("e",10))
# print(getWordScore("ee",3))

# hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# displayHand(hand)
# hand = updateHand(hand, 'lail')
# displayHand(hand)
# hand = updateHand(hand, 'lail')
# displayHand(hand)

#print(calculateHandlen(hand))

wordList = loadWords()
#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
#playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
#playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 10)
#playHand({'n':1, 'e':1, 't':1}, wordList, 3)

# playGame(wordList)

# print(compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6))

# compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)