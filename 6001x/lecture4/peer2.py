# -*- coding: utf-8 -*-
"""
@author: Andrew Sh
"""

import math

def polysum(n, s):
    '''
    n: int, number of sides
    s: int, length of each side
 
    returns: sum of the area and square of the perimeter of the regular polygon
    '''
    
    area = (0.25 * n * pow(s, 2)) / (math.tan(math.pi/n))   
    perimeter = s * n                                       
    answer = round((area + pow(perimeter, 2)), 4)    #makes up the sum and rounds it to 4 decimal places
    return answer