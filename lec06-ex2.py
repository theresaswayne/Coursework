#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:51:28 2017

@author: confocal
"""
#
import random

mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)


## Code Sample A
#mylist = []
#
#for i in range(random.randint(1, 10)):
#    random.seed(0)
#    if random.randint(1, 10) > 3:
#        number = random.randint(1, 10)
#        if number not in mylist:
#            mylist.append(number)
#print(mylist)


# Code Sample B
#mylist = []
#
#random.seed(0)
#for i in range(random.randint(1, 10)):
#    if random.randint(1, 10) > 3:
#        number = random.randint(1, 10)
#        mylist.append(number)
#    print(mylist)