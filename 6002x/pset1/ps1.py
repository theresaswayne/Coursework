###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1 SOLVED
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """ 

    cowsCopy = sorted(cows, key=cows.__getitem__, reverse = True)
#    print("Sorted cows are "+ str(cowsCopy))
    cowsLeft = cowsCopy[:] # clone the list
    allTripsResult = []
    thisTripResult = []
    tripWeight = 0.0

    while (len(cowsLeft) > 0):
        thisTripResult = []
        tripWeight = 0.0
        for nextCow in cowsCopy: # this has to be a sorted list
            if (nextCow in cowsLeft):
                # print("Checking "+nextCow+" weighing "+str(cows[nextCow]))
                if (tripWeight + cows[nextCow] <= limit):
                    thisTripResult.append(nextCow) # the name of the cow
                    tripWeight += cows[nextCow] # the weight of the cow
                    # print("Taking "+ str(thisTripResult) + " weighing " + str(tripWeight))
                    cowsLeft.remove(nextCow) # remove this one from consideration
        # when all of the cows have been checked once
        # print("This trip has "+ str(thisTripResult) + " weighing " + str(tripWeight))
        allTripsResult.append(thisTripResult)
        # print("All trips so far: "+ str(allTripsResult))
        # print("New trip started")

    return allTripsResult


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    cowNames = cows.keys()
    
    # step 1 -- enumeration
   
    def possible_alloc(items):
        ''' 
        generator for cow allocations
        note: this does not ensure that the allocations obey the weight limit
        input: list (strings)
        output: list of lists, each inner list being the cows on one trip
        '''
        
        for item in (get_partitions(items)):
            yield(item)
    
    allocations = possible_alloc(cowNames)
    
    #step 2 -- evaluate number of trips and compliance with weight limit
    # check the number of trips first because I expect it to save calculation time
    
    minTrips = len(cowNames) # the largest it could be -- one cow per trip
    bestAlloc = []
    for name in cowNames:
        bestAlloc.append([str(name)]) # the worst it could be -- one cow per trip
    # print("initial bestAlloc is "+str(bestAlloc))
    for alloc in allocations:
        trips = len(alloc) # each element of alloc is the list of cows on one trip; 
        # the number of elements is the number of trips
        if trips <= minTrips: # is it a candidate for the shortest trip?
            for trip in alloc:
                cowWeights = [cows[name] for name in trip]
                tripWeight = sum(cowWeights)
                if tripWeight > limit:
                    break # out of the trip loop, so check the next alloc
            else:
                minTrips = trips
                bestAlloc = alloc

    # print("Final best allocation is " + str(bestAlloc))
    # print("accomplished in "+str(minTrips)+ " trips")
    return bestAlloc
    

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#==============================================================================
# Testing whether we can load data 
#==============================================================================

cows = load_cows("ps1_cow_data.txt")
# print(cows)

limit = 20
#==============================================================================
# Testing part 1
#==============================================================================

# print(greedy_cow_transport({'Polaris': 20, 'Horns': 50, 'Miss Bella': 15, 'Louis': 45, 'Clover': 5, 'Milkshake': 75, 'Muscles': 65, 'Lotus': 10, 'MooMoo': 85, 'Patches': 60}, 100))
# Correct output:
# [['MooMoo', 'Miss Bella'], ['Milkshake', 'Polaris', 'Clover'], ['Muscles', 'Lotus'], ['Patches'], ['Horns', 'Louis']]

# print(greedy_cow_transport({'Buttercup': 72, 'Betsy': 65, 'Lilly': 24, 'Daisy': 50, 'Abby': 38, 'Rose': 50, 'Willow': 35, 'Patches': 12, 'Dottie': 85, 'Coco': 10}, 100))
# Correct output:
# [['Dottie', 'Patches'], ['Buttercup', 'Lilly'], 
# ['Betsy', 'Willow'], ['Daisy', 'Rose'], ['Abby', 'Coco']]
start = time.time()
print(greedy_cow_transport(cows, limit))
end = time.time()
print("For the greedy algorithm, time = " + str(end - start))

#==============================================================================
# Testing part 2
#==============================================================================

# testing import of partitions functions
# for item in (get_partitions(cows)):
#       print(item)
start = time.time()
print(brute_force_cow_transport(cows, limit))
end = time.time()
print("For the brute-force algorithm, time = " + str(end - start))

