#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:07:20 2017

@author: confocal
"""
import numpy, pylab

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

# --- testing ---


lowTemps, highTemps = loadFile()
diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))
pylab.plot(range(1,32), diffTemps)