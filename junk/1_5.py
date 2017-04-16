#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:25:49 2017

@author: T. Swayne
"""

# might need to use memoization here
# complexity O(n^2)
# can itertools help generate the subsets?
# or loop through list indices for start, stop

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    
    # ?? generate all subsequences and sums
    # every subsequence except those of len 1 is the combo of other sequences
    
    def max_sum(L_remaining, seqSum, memo = {}):
        ''' L_remaining, a list of integers
            seqSum, a memo supplied by recursive calls per lec02-3
            Returns the maximum sum of a contiguous subsequence in L_remaining
        '''
        
        