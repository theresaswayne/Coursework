#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:38:40 2017

@author: confocal
"""

# accessing variables set within function

x= []
print("before function",x)

def changeX():
    x.append(6)
    print("inside function", x)

print("before execution", x)
changeX()
print("after execution",x)

# Functions can do stuff with variables in the main program

print("a function with an argument")

y=[]
z=[]
print("before function",y)

def changeY(z):
    z.append(7)
    print("inside function", y, z) # this function accessed y and changed it

print("before execution", y)
changeY(y)
print("after execution",y, z) # z is an argument to the function -- doesn't change outside the function
