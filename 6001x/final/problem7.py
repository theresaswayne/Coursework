# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:53:26 2016

@author: theresa
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    k = len(L)
    
    def f(x):
        ''' x: int or float argument
        returns the evaluation of a kth order polynomial '''
        answer = 0
        for index in range(0,k):
            exponent = k - index - 1
            answer += L[index] * (x**exponent)

        return answer
        
    return f


# tests: 0, length 0, empty sets, neg numbers, decimals
x = 5

# answer 14
L = [1]

## answer 1?
#L = []
#
## answer 2
#L = [2]
#
## answer 10
# L = [2, 0, 2]
#
## answer -3
#L = [-1, -1]


polynomial = general_poly(L)

print(str(polynomial(x)))