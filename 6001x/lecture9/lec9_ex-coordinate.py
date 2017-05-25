# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:50:15 2016

@author: theresa
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        '''
        self, other: coordinates
        returns True if the coordinates are the same
        '''
        coord_same = self.getX() == other.getX() and self.getY() == other.getY()
        return coord_same
    
    def __repr__(self):
        '''
        self: coordinate
        returns a string containing the essential information in self
        should output Coordinate(self.x,self.y)
        '''
        
        descrip = 'Coordinate('+ str(self.getX()) + ', ' + str(self.getY()) + ')'
        return descrip

a = Coordinate(8,7)
b = Coordinate(8,8)
print(a, b)
#if a == b:
#    print("same")
#else:
#    print("not same")
b = eval(repr(a))
#b = eval("Coordinate(8,7)")
print("reassigning b...")
#eval(b)
print(a,b)
print(b.getX())



