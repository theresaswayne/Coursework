# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:20:19 2016

@author: confocal
"""

warm = ['red', 'yellow', 'orange'] 
print(warm)
hot = warm
print(hot)
print("using warm.sort()...")
warm.sort() 
print(warm)
print(hot)
print("======================")
cool = ['grey', 'green', 'blue'] 
print(cool)
print("using sorted(cool)...")
sortedcool = sorted(cool) 
print(cool)
print(sortedcool)
