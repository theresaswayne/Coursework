#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:27:57 2017

@author: T. Swayne
"""


import random
import pylab as plt

random.seed()
# random.seed(0)

n = 10

# generate some random (or not) numbers

def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return random.randrange(0, 100, 2)

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 21, 2)

mySamples = []
for i in range(0, n):
    mySamples.append(i)

myRands = []
for i in range(0, n):
    # myRands.append(genEven()) # ex 2
    # myRands.append(deterministicNumber()) # ex 3-1
    myRands.append(stochasticNumber()) # ex 3-2

# plot the selected numbers
plt.plot(mySamples, myRands)

# TODO: plot the histogram
# TODO: (?) measure the randomness
