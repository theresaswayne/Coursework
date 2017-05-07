#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:24:04 2017

@author: T. Swayne
"""
import pylab

a = [1,2,3]
b = [3,3,3]
answer1 = a+b
#print("list addition",answer1)
aArray = pylab.array(a)
bArray = pylab.array(b)
answer2 = aArray+bArray
#print("array addition",answer2)
s = sorted(answer1)
#print("sorted",s)

sumA = sum(a)
print(sumA)
