# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 18:36:17 2016

@author: theresa
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        '''
        self, other: intsets
        returns a new intSet containing elements that appear in both sets.
        s1.intersect(s2) returns a new intSet of integers that appear 
        in both s1 and s2. (what should happen if s1 and s2 have no 
        elements in common?)
        '''
        new_set = intSet()

        for element in self.vals:
            if other.member(element):
                new_set.insert(element)
        return new_set

    def __len__(self):
        '''
        len(s) should return the number of elements in s
        '''
        return len(self.vals)
        
s1 = intSet()
s2 = intSet()

for i in range(1,40):
    s1.insert(i)
    s2.insert(i+20)
    s2.insert(i+50)

# print(s1, s2)
# print(s1.intersect(s2))
print(len(s1))
print(len(s2))
