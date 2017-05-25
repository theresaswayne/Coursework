# -*- coding: utf-8 -*-
def polysum(n,s):
    """
    """
    import math
    area = ((0.25*n*s**2)/math.tan(math.pi/n))
    perimeter = 0
    while n > 0:
        perimeter += s
        n -= 1
    return round(area + perimeter ** 2, 4)