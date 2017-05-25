# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:06:59 2016

@author: theresa
"""




def genPrimes():
    num = 2
    while True:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime == True:
            yield num
        num += 1

max = 100
         
mygen = genPrimes()

for iter in range(1,max+1):
    print(mygen.__next__())
