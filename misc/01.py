#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:15:14 2017

@author: T. Swayne
"""

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    import random
    
    allTheSame = 0
    
    for i in range(numTrials):
        bucket = [0,0,0,0,1,1,1,1] # 0 represents red, 1 represents green
        samp = random.sample(bucket, 3)
        if (sum(samp) == 0 or sum(samp) == 3): # all the same color
            allTheSame += 1
    result = allTheSame/numTrials
    return result

numTrials = 1
answer = drawing_without_replacement_sim(numTrials)
print(answer, answer * 7)

