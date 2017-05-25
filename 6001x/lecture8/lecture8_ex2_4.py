# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:21:01 2016

@author: confocal
"""

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
        


print(fancy_divide([0,2,4],1))
print("=======")
print(fancy_divide([0,2,4],4))
print("=======")
print(fancy_divide([0,2,4],0))
