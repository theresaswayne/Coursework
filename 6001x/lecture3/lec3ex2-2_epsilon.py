# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:25:18 2016

@author: confocal
"""
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        print(str(guess))
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))