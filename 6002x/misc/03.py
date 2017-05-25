import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    
    p = 1.0 - (CURRENTRABBITPOP/MAXRABBITPOP)
    rabbitsBorn = 0
    
    # enforce minimum population
    if CURRENTRABBITPOP < 10:
        CURRENTRABBITPOP = 10

    for rabbit in range(CURRENTRABBITPOP):        
        x = random.random()
        if x < p:
            rabbitsBorn += 1

    if rabbitsBorn + CURRENTRABBITPOP > MAXRABBITPOP:
        # enforce maximum population
        CURRENTRABBITPOP = MAXRABBITPOP
    else:
        CURRENTRABBITPOP += rabbitsBorn
    
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    foxesBorn = 0
    foxesDied = 0
    
    # enforce minimum population
    if CURRENTFOXPOP >= 10:
        for fox in range(CURRENTFOXPOP):
            # hunt
            p = CURRENTRABBITPOP/MAXRABBITPOP
            hunt = random.random()
            if hunt < p: # hunt successful
                CURRENTRABBITPOP -= 1
                
                # enforce minimum population
                if CURRENTRABBITPOP < 10:
                    CURRENTRABBITPOP = 10
                repro = random.random()
                if repro < 0.333333: # birth successful
                    foxesBorn += 1
            else: # hunt unsuccessful
                die = random.random()
                if die < 0.9:
                    foxesDied += 1
    CURRENTFOXPOP = CURRENTFOXPOP + foxesBorn - foxesDied
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = []
    fox_populations = []
    
    for step in range(numSteps):
        # rabbits reproduce
        rabbitGrowth()
        # foxes reproduce
        foxGrowth()
        # update after rabbits are eaten
        fox_populations.append(CURRENTFOXPOP)
        rabbit_populations.append(CURRENTRABBITPOP)
        
    return (rabbit_populations, fox_populations)

# -------- testing

timeSteps = 200
(rab,fox) = runSimulation(timeSteps)

# get curve fits
rabCoeff = pylab.polyfit(range(len(rab)), rab, 2)
foxCoeff = pylab.polyfit(range(len(fox)), fox, 2)

# plot raw data
pylab.plot(range(timeSteps),rab, 'r-', label = 'Rabbits')
pylab.plot(range(timeSteps), fox, 'b-', label = 'Foxes') 

# plot curve fits
pylab.plot(pylab.polyval(rabCoeff, range(len(rab))), 'r--', label = 'Rabbits, 2nd deg fit')
pylab.plot(pylab.polyval(foxCoeff, range(len(fox))), 'b--', label = 'Foxes, 2nd deg fit')


pylab.title('Predator-prey relationships')
pylab.xlabel('Time')
pylab.ylabel('Population')
pylab.legend(loc='best')
pylab.show()



