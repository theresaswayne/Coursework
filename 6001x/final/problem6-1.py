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
        return self.name + ' says: It is obvious that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff
        
        
# As written, this code leads to an infinite loop when using the Arrogant Professor class.
#
# Change the definition of ArrogantProfessor so that the following behavior is achieved:
#e = Person('eric') 
#le = Lecturer('eric') 
#pe = Professor('eric') 
ae = ArrogantProfessor('eric')
#
#print(e.say('the sky is blue'))
#eric says: the sky is blue
#
#print(le.say('the sky is blue'))
#eric says: the sky is blue
#
#print(le.lecture('the sky is blue'))
#I believe that eric says: the sky is blue
#
#print(pe.say('the sky is blue'))
#eric says: I believe that eric says: the sky is blue
#
#print(pe.lecture('the sky is blue'))
#I believe that eric says: the sky is blue
#
print(ae.say('the sky is blue'))
#eric says: It is obvious that eric says: the sky is blue

print(ae.lecture('the sky is blue'))
#It is obvious that eric says: the sky is blue