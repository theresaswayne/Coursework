# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = [6, 5]
y = type(x)
print(y)

if isinstance(x, int):
    print("it's an int")
elif isinstance(x, str):
    print("it's a str")
else:
    print("something else")
    
if type(x) == int:
    print("it's still an int")

if type(x) == str:
    print("it's still a str")

if type(x) == list:
    print("it's a list")
