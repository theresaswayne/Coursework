#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 23:07:52 2017

@author: T. Swayne
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''

#    random.seed()
    sameColor = 0    
    for trial in range(numTrials):
        balls = [1,1,1,0,0,0]
        draw = random.sample(balls, 3)
#        print(draw)
        if sum(draw) == 3 or sum(draw) == 0:            
            sameColor += 1
    result = sameColor/numTrials
    return result
    

# ---- testing ----

# print(noReplacementSimulation(10))
results = []
for sampleSize in range (10, 1000, 10):
    estimate = noReplacementSimulation(sampleSize)
    results.append(estimate)
#    print(sampleSize, estimate)

print("average",sum(results)/len(results))
    
    
# 2 all one color
# 9 RRG (3 pairs of reds, 3 greens)
# 9 GGR
# answer should be 2/20 = 1/10