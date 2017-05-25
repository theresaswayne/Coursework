# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:34:57 2016

@author: confocal
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing (>=) or monotonically decreasing (<=). 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    
    temp_run = []
    longest_run = []
    run_sum = 0
    end_index = 1
    Lc = L.copy
    print(Lc)
    n = len(Lc)
    print(str(n))

    # search for increasing runs beginning with each item
    for start_index in range(0,n-2):
        # search for increasing runs beginning with item 0
        temp_run = L[start_index:start_index+1]
        print("temp = ",temp_run)
        end_index = start_index + 1
        while end_index <= n+1:
            print("searching up to ",str(end_index))
            if temp_run[-1] <= L[end_index]:
                temp_run.append(L[end_index])
                print("run is now ",temp_run)
                end_index += 1
            else:
                if len(temp_run) - 1 > len(longest_run):
                    longest_run = temp_run[0:-1]
                print("longest for start ",str(start_index),longest_run)
                break
        if len(temp_run) > len(longest_run):
            longest_run = temp_run[:]
            print("longest for start ",str(start_index)," is ", longest_run)

    print("this is our best increasing run: ",longest_run)
    
    
    # calculate the sum
    for item in longest_run:
        run_sum += item
    
    # return the answer
    return run_sum


#
#    for i in range (0, n-1):
#        temp_inc = L[i]
#        for j in range (i+1, n):
#            if L[j] > L[j-1]:
#                temp_inc.append(L[j])
#                print(temp_inc)
#            else:
#                break

#    # identify runs
#    for first_i in range(0, len(Lc)):  # iterate over L
#        for end_i in range(first_i, len(Lc)-first_i):
#            
#            if Lc[end_i] <= Lc[end_i+1]:
#                incr_count += 1
#                decr_count = 0
#                temp_run.append(Lc[end_i])
#            else:
#                decr_count += 1
#                incr_count = 0
            
        # if L[i] <= L [i+1] then increment count for MIR, set MDR count to 0
        # else increment count for MDR and set MIR count to 0
            
# other ideas
# at each step copy a piece of the list
# extend it if the run continues
# if it doesn't continue compare to the stored longest run
# could search for IR and DR separately
            # start w a small piece (2) of the list and compare its penultimate to ultimate member, then add another to the end and repeat
    

# test
#L=[1,2,3,2]
#print(str(longest_run(L)))
## test 1
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
print(L)
n = len(L)
print(str(n))
print("Expected 26, actual: ",str(longest_run([L])))
#
## longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7] # longest run of monotonically decreasing numbers in L is [10, 4, 3]
## expected value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.
#
## test 2
#L = [5, 4, 10]
#print("Expected 9, actual: ",str(longest_run([L])))

# increasing  [4, 10] 
# decreasing numbers in L is [5, 4]
# expect 9 because the decreasing run occurs before the increasing run


