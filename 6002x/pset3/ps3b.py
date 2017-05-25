#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:37:47 2017

@author: T. Swayne
"""

# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
#import matplotlib.pyplot as plt
# import numpy as np
import pylab
# pylab is a single namespace for numpy and matplotlib but the matplotlib docs recommend separate import

# random.seed(0)

# for comparison, to get "correct" results from 
# SimpleVirus, Patient, ResistantVirus, TreatedPatient:
# comment out all those classes, then uncomment the following:
# (note requires pytnon 35 doesn't work with 36)
# from ps3b_precompiled_35 import *

''' 
Begin helper code
'''
class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """
'''
End helper code
'''

#
# --- PROBLEM 1 --- 
#

class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        
    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        x = random.random()
        if x <= self.getClearProb():
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        x = random.random()
        p = self.getMaxBirthProb()*(1.0-popDensity)
        if x <= p:
            return SimpleVirus(self.getMaxBirthProb(),self.getClearProb())
        else:
            raise NoChildException()



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    When defining a Patient class member variable 
    to store the viruses list representing the virus population, 
    please use the name self.viruses in order for your code 
    to be compatible with the grader
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)       


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        viruses = self.getViruses()[:] # copy of list
        
        # testing
        #clearedCount = 0
        #reproCount = 0
        
        # check for clearance        
        for particle in viruses:
            if particle.doesClear():

                # testing
                #clearedCount +=1

                self.viruses.remove(particle) # from original list

        # decide reproduction based on new density
        
        popDensity = len(self.viruses)/self.getMaxPop()
                
        # check for reproduction
        unclearedViruses = self.getViruses()[:]
        for particle in unclearedViruses: # copy of list
            try:
                self.viruses.append(particle.reproduce(popDensity)) # the attribute

                # testing
                #reproCount += 1

            except NoChildException:
                continue
        # print(clearedCount,"cleared and",reproCount,"reproduced")
        return len(self.viruses)
                    
#
# --- PROBLEM 2 ---
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
        
    Use pylab to produce a plot (with a single curve) that displays 
    the average result of running the simulation for many trials. 
    Make sure you run enough trials so that the resulting plot 
    does not change much in terms of shape and time steps taken 
    for the average size of the virus population to become stable. 
    
    Don't forget to include axes labels, a legend for the curve, 
    and a title on your plot.

    You should call simulationWithoutDrug with the following parameters:
    
    numViruses = 100
    maxPop (maximum sustainable virus population) = 1000
    maxBirthProb (maximum reproduction probability for a virus particle) = 0.1
    clearProb (maximum clearance probability for a virus particle) = 0.05
    
    Thus, your simulation should be instantiatating one Patient 
    with a list of 100 SimpleVirus instances. 
    Each SimpleVirus instance in the viruses list should 
    be initialized with the proper values for maxBirthProb and clearProb.
    """

    timesteps = 300
    #timesteps = 10
    
    # storing results
    #TODO: try a numpy array that can probably be 
    #     appended to and averaged more directly.
    
    resultsByTrial = []
    # list of lists;  inner list = all the results from a certain trial
    # r[N] = [TNt1, TNt2...TNtn] T=trial, N=numTrials, t=timepoint, n=numTimepoints
    
    for i in range(numTrials):
        # create viruses
        viruses = []
        for i in range(numViruses):
            viruses.append(SimpleVirus(maxBirthProb,clearProb))
        
        # testing append
        #print("created",len(viruses),"viruses")
        
        # create patient with said viruses
        pat = Patient(viruses, maxPop)
        
        trialResults = []
        
        for j in range(timesteps):
            pat.update()
            # print("viruses at time",j,"=",pat.getTotalPop(),"out of max",pat.getMaxPop())
            
            # save results: population over time
            trialResults.append(pat.getTotalPop())
        
        resultsByTrial.append(trialResults)
        
    # calculate average population at each timestep
    averageByTime = []
    
    for i in range(timesteps):
        sumTrials = 0
        for j in range(numTrials):
            sumTrials += resultsByTrial[j][i] # the ith timepoint in the jth trial
        timeAverage = sumTrials/numTrials
        # print("average for time",i,"=",timeAverage)
        averageByTime.append(timeAverage)

    pylab.figure(1)
    pylab.plot(range(timesteps), averageByTime, label = 'Virus population') # simple plot
    pylab.title('Virus population in untreated patient')
    pylab.xlabel('time, h')
    pylab.ylabel('No. of viruses, average of '+str(numTrials)+' trials')
    pylab.legend(loc='best')
    pylab.show()

    return
#
# --- PROBLEM 3 ---
#
#The __init__ method of ResistantVirus should directly 
#call the __init__ method of SimpleVirus via the 
#line "SimpleVirus.__init__(self, <appropriate parameters>)".
        

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self,maxBirthProb,clearProb)
        self.resistances = resistances
        self.mutProb = mutProb
        
    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        return self.resistances.get(str(drug), False)
#        try:
#            return self.resistances[drug]
#        except KeyError:
#            return False

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # check if drugs block reproduction
        totalResistance = 0

        for drug in activeDrugs:
            totalResistance += self.isResistantTo(drug)
        #print("virus is resistant to",totalResistance,"drugs out of",len(activeDrugs))
        if totalResistance < len(activeDrugs):
            # print("cocktail worked")
            raise NoChildException() # no reproduction
        else: 
            # reproduce according to maxBirthProb and popDensity
            x = random.random()
            p = self.getMaxBirthProb()*(1.0-popDensity)
            #print("x=",x,"p=",p)
            if x <= p:
                #print("reproducing!")
                # chance for mutation of resistance genes
                newResistances = self.getResistances().copy() # copy not ref to orig
                for drug in newResistances:
                    #print("current resistance to",drug,": ",newResistances[drug])
                    m = random.random()
                    if m <= self.getMutProb():
                        newResistances[drug] = not newResistances[drug]
                        #print("new resistance to",drug,": ",newResistances[drug])
                return ResistantVirus(self.getMaxBirthProb(),self.getClearProb(), newResistances, self.getMutProb())
            else: # didn't hit probability of reproducing
                raise NoChildException()             

# --- PROBLEM 4 ---
#
class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self, viruses, maxPop)
        self.drugs = []
       

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

    # check if a dictionary contains a value already
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        resistantVirusPop = 0
        index = 0
        for virus in self.getViruses():
            index += 1
            totalResistance = 0
            for drug in drugResist:
                #print("virus", index, "resistant to",drug,"?",virus.isResistantTo(drug))
                if virus.isResistantTo(drug):
                    totalResistance += 1
            #print("virus is resistant to",totalResistance,"drugs out of",len(drugResist))
            if totalResistance == len(drugResist): # this virus is resistant to every drug
                resistantVirusPop +=1
        
        return resistantVirusPop


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        viruses = self.getViruses()[:] # copy of list
        
        # testing
        #clearedCount = 0
        #reproCount = 0
        
        # check for clearance        
        for virus in viruses:
            if virus.doesClear():

                # testing
                #clearedCount +=1

                self.viruses.remove(virus) # from original list

        # decide reproduction based on new density
        popDensity = len(self.viruses)/self.getMaxPop()
        
        # check for reproduction
        unclearedViruses = self.getViruses()[:]
        drugs = self.getPrescriptions()
        #print("current prescriptions =",drugs)
        for virus in unclearedViruses: # copy of list
            try:                              
                self.viruses.append(virus.reproduce(popDensity,drugs)) 
                #reproCount += 1

            except NoChildException:
                continue
        # print(clearedCount,"cleared and",reproCount,"reproduced")
        return len(self.viruses)

#
# --- PROBLEM 5 ---
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    drug = 'guttagonol' # has to be a string to get the prescriptions to turn out right
    # but is taken apart into letters in the resistance check
    timestepsNoDrug = 150
    timestepsDrug = 150
    
    allResultsTotal = []
    allResultsResistant  = []
    
    for i in range(numTrials):
        # create num viruses
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb,clearProb, resistances, mutProb))

        # create patient with said viruses
        pat = TreatedPatient(viruses, maxPop)
        
        trialResultsTotal = []
        trialResultsResistant = []
    
        # run timecourse
        for j in range(timestepsNoDrug):
            pat.update()
            #print("at time",j,"there are",pat.getResistPop([drug])," resistant out of",pat.getTotalPop(),"total")
            trialResultsTotal.append(pat.getTotalPop())
            trialResultsResistant.append(pat.getResistPop([drug]))
        
        # drug phase
        pat.addPrescription(drug) # DEBUG -- here you add a prescription 
        #print("current prescriptions (simul)",pat.getPrescriptions())
        
        for j in range(timestepsDrug):
            pat.update()
            #print("at time",j,"there are",pat.getResistPop([drug])," resistant out of",pat.getTotalPop(),"total")
            trialResultsTotal.append(pat.getTotalPop())
            trialResultsResistant.append(pat.getResistPop([drug])) # brackets are essential!!
        
        allResultsTotal.append(trialResultsTotal)
        allResultsResistant.append(trialResultsResistant)
    
    # after all trials, calculate average per timestep
    averageByTimeTotal = []
    averageByTimeResistant = []
    timestepsTotal = timestepsNoDrug + timestepsDrug
        
    for i in range(timestepsTotal):
        sumTrialsTotal = 0
        sumTrialsResistant = 0
        for j in range(numTrials):
            sumTrialsTotal += allResultsTotal[j][i] # the ith timepoint in the jth trial
            sumTrialsResistant += allResultsResistant[j][i]
            # TODO: to make this easier, plot a tuple?
        timeAverageTotal = sumTrialsTotal/numTrials
        timeAverageResistant = sumTrialsResistant/numTrials
        #print("average for time",i,"=",timeAverageResistant, "resistant out of",timeAverageTotal)
        averageByTimeTotal.append(timeAverageTotal)
        averageByTimeResistant.append(timeAverageResistant)
        #print(averageByTimeResistant)
    
    pylab.figure(1)
    # red dashes, blue squares and green triangles
    #plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    pylab.plot(range(timestepsTotal), averageByTimeTotal, 'r--', label = 'Total virus population') # simple plot
    pylab.plot(range(timestepsTotal), averageByTimeResistant, 'g^', label = 'Resistant virus population') # simple plot
    pylab.title('Virus populations in drug-treated patient')
    pylab.xlabel('time, h')
    pylab.ylabel('No. of viruses, average of '+str(numTrials)+' trials')
    pylab.legend(loc='best')
    pylab.show()
     

# --- testing simpleVirus ---

#birth = 1.0
#clear = 0.0
#popDensity = 0.99
#simp = SimpleVirus(birth,clear)
#
## testing getters
#print("Max birth probability:",simp.getMaxBirthProb())
#print("Clear probability:",simp.getClearProb())
#print("Population density:",popDensity)

# testing doesClear
#for i in range(1,100):
#    print("trial",i,"clearance:",simp.doesClear())

# testing reproduce
#noRepro = 0
#for i in range(1,100):
#    try:
#        print("trial",i)
#        simp.reproduce(popDensity)
#    except NoChildException:
#        noRepro += 1
#        continue
#print("no reproduction in",noRepro,"trials")

# --- testing Patient ---

#viruses = []
#numViruses = 50
#maxPop = 100

# create a list of identical viruses
#for i in range(numViruses):
#    viruses.append(SimpleVirus(birth,clear))


# create patient
#pat = Patient([simp], maxPop)

#print("viruses in patient",pat.getTotalPop())
#print("max viruses in patient",pat.getMaxPop())

#for i in range(1,100):
#    pat.update()
#    print("viruses in patient",pat.getTotalPop())

# --- testing simulation without drug ---

#numViruses = 100
#maxPop = 1000
#maxBirthProb = 0.1
#clearProb = 0.05
#numTrials = 100
#
## run simulation
#simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)

# --- testing resistant virus class ---

#maxBirthProb = 0.8
#clearProb = 0.2
#resistances = {'guttagonol':True,'vodka':True}
#mutProb = 0.8
#
#resist = ResistantVirus(maxBirthProb,clearProb, resistances, mutProb)

# testing getters
#print("Max birth probability:",resist.getMaxBirthProb())
#print("Clear probability:",resist.getClearProb())
#print("Mutation frequency:",resist.getMutProb())
#print("Resistances:",resist.getResistances())
#print("Resistant to guttagonol?",resist.isResistantTo('guttagonol'))
#print("Resistant to vodka?",resist.isResistantTo('vodka'))

# testing reproduction
#
#popDensity = 0.5
#activeDrugs = ['guttagonol']
#noRepro = 0
#for i in range(1,100):
#    try:
#        print("trial",i)
#        resist.reproduce(popDensity, activeDrugs)
#    except NoChildException:
#        noRepro += 1
#        continue
#print("no reproduction in",noRepro,"trials")


# --- testing treated patient ---

viruses = []

numViruses = 100
maxPop = 1000

maxBirthProb = 0.1
clearProb = 0.05
resistances = {'guttagonol':False}
#resistances = {}
mutProb = 0.005

numTrials = 2
#
#drugQuery1 = ['aspirin']
#drugQuery2 = ['guttagonol']

##create a list of identical viruses
#for i in range(numViruses):
#    viruses.append(ResistantVirus(maxBirthProb,clearProb, resistances, mutProb))

#create patient
#pat = TreatedPatient(viruses, maxPop)

# test getters and prescriptions
#print("viruses in patient:",pat.getTotalPop())
#print("resistant to",drugQuery1,":",pat.getResistPop(drugQuery1))
#print("resistant to",drugQuery2,":",pat.getResistPop(drugQuery2))
#print("max viruses in patient:",pat.getMaxPop())
#print("active prescriptions:",pat.getPrescriptions())

#print("adding some prescriptions...")
#pat.addPrescription('aspirin')
#print("active prescriptions:",pat.getPrescriptions())
#pat.addPrescription('aspirin')
#print("active prescriptions:",pat.getPrescriptions())
#print("resistant to",drugQuery1,":",pat.getResistPop(drugQuery1))
#print("resistant to",drugQuery2,":",pat.getResistPop(drugQuery2))

#for i in range(1,150):
#    pat.update()
#    print(pat.getResistPop(drugQuery2),"resistant out of",pat.getTotalPop(), "total")
#
#pat.addPrescription('guttagonol')
#print("now treating with",pat.getPrescriptions())
#
#for i in range(1,150):
#    pat.update()
#    print(pat.getResistPop(drugQuery2),"resistant out of",pat.getTotalPop(), "total")


# --- testing simulation with drug

# run simulation
simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials)

