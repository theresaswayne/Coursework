#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:25:12 2017

@author: T. Swayne
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    
    # iterate through L as L[i]
    import math
    total = 0
    sum_mult = 0
    
    for i in L:
        
        m_test = math.floor((s-total)/i)
        if total + (i*m_test) == s:
            # finished
            total += i*m_test
            sum_mult += m_test
            return sum_mult
        elif total > s:
            # continue to the next element of L (???)
            continue
        elif total < s:
            # keep going
            total += i*m_test
            sum_mult += m_test
    
    # at this point we have tried all of L
    return "no solution"
        
        
# --- testing ---

L = [10,9,8,5,2]
s = 2042
print("the solution is",greedySum(L, s))

