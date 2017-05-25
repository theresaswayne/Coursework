# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:47:46 2016

@author: confocal
"""

# Part 1
#def normalize(numbers):
#    max_number = max(numbers)
#    for i in range(len(numbers)):
#        numbers[i] /= float(max_number)
#    return numbers 
#
#try:
#      normalize([0, 0, 0])
#except ZeroDivisionError:
#      print('Invalid maximum element')


#Part 2
def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers     