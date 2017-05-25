# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:39:52 2016

@author: confocal
"""


class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that I believe that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + self.name + ' says: ' + stuff
        
        
##        As written, this code leads to an infinite loop when using the Arrogant Professor class.
#You change your mind, and now want the behavior as described in Part 1, except that you want:
#
#>>> ae.say('the sky is blue')
#eric says: It is obvious that I believe that eric says: the sky is blue
#
#>>> ae.lecture('the sky is blue')
#It is obvious that I believe that eric says: the sky is blue
#Change the definition of ArrogantProfessor so that the behavior described above is achieved.
#
ae = ArrogantProfessor('eric')
print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))
