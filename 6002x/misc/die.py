#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:24:38 2017

@author: T. Swayne
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# use only pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show
# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """

    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.hist(values,numBins)
    pylab.show()
    
#    import matplotlib.pyplot as plt
#    plt.plot([1,2,3,4])
#    pylab.ylabel(yLabel)
#    plt.show()
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    t = 0
    longestRuns = []
    for trial in range(numTrials):
        r = 0
        rolls = []
        runLength = 1
        longestRun = 1
        t += 1
        #print("trial",t)
        for roll in range(numRolls):
            r += 1
            #print("roll",r)
            thisRoll = die.roll()
            #print("rolled",thisRoll)
            rolls.append(thisRoll)
            # see if you are in a run
            if (len(rolls) > 1 and thisRoll == rolls[-2]):
                runLength += 1
                #print(rolls,"current runLength =",runLength)
                # if so see if you have the longest run
                longestRun = max([runLength,longestRun])
                # update longest run length if needed
            else:
                runLength = 1
                
        #print("longest run for trial",t,"was",longestRun)
        # store longest run in longestRuns
        longestRuns.append(longestRun)
    
    # calculate the mean
    meanVal, stdDev = getMeanAndStd(longestRuns)
    #print("mean length = ",round(meanVal,3))
    
    # make the histogram
    makeHistogram(longestRuns, 10, "length of longest run","frequency")
    return round(meanVal,3)
      
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
# should be 5.312
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 5, 5))

#for i in range(1000):
#    values.append(random.random()) 

#makeHistogram(values, 20, "values","freq")

    