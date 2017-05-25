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
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: It is obvious that I believe that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + self.name + ' says: ' + stuff
        
        

# You change your mind once more. You want to keep the behavior from Part 2, but now you would like:
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

print(pe.say('the sky is blue'))
# Prof. eric says: I believe that eric says: the sky is blue 
#
print(ae.say('the sky is blue'))
#Prof. eric says: It is obvious that I believe that eric says: the sky is blue 
#Change the Professor class definition in order to achieve this. You may have to modify your implmentation for a previous part to get this to work.
