# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:42:32 2016

@author: confocal
"""
high = 100 # highest possible number is 99 but they say use 100
low = 0
guess = 0
feedback = ""

print("Please think of a number between 0 and 100!")

while feedback != "c":
    
    # generate guess midway between high and low
    guess = int(low + (high - low)/2)
#    print(str(high), str(low), str(guess))
    
    print("Is your secret number "+str(guess)+"?")
    
    # collect feedback
    feedback = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if feedback != "h" and feedback != "l" and feedback != "c":
        print("Sorry, I did not understand your input.")
    elif feedback == "h":
        # modify high
        high = guess
#        print(str(high), str(low), str(guess))
    elif feedback == "l":
        # modify low
        low = guess
#        print(str(high), str(low), str(guess))
print("Game over. Your secret number was: " + str(guess))
