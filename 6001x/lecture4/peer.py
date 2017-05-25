# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 22:13:25 2016

@author: User
"""

import math
def polysum(n, s):
    x=round(0.25*n*s*s*(math.tan(math.pi/n))+n*n*s*s,4)
    return x

print(polysum(36, 82))
