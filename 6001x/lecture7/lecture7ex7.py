# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:03:44 2016

@author: confocal
"""

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)
      
print(f(0))