#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:25:49 2017

@author: T. Swayne
"""

# complexity O(n^2)

# --- begin correct solution ---
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    max_sum = 0
    for start_index in range(0, len(L)):
        for stop_index in range(start_index+1, len(L)+1):
            subseq = L[start_index:stop_index]
            subseq_sum = sum(subseq)
            if subseq_sum > max_sum:
                max_sum = subseq_sum
    return max_sum

# --- end correct solution ---

#    def max_sum(L_remaining, seqSum, memo = {}):
#        ''' L_remaining, a list of integers
#            seqSum, a memo giving the sum of subsequences, supplied by recursive calls per lec02-3
#            Returns the maximum sum of a contiguous subsequence in L_remaining
#        '''

# --- testing ---

import random
L = [1,2,3,-4,6]
print(max_contig_sum(L))  

L = []
nValues = 1000
for i in range(nValues):
    L.append(random.randint(-50,+50))
print(max_contig_sum(L))  
