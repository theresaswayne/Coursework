# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        # tcs: using formula cos(angle) = delta_x/(distance traveled)
        # tcs: speed = distance because 1 time unit has elapsed
        delta_y = speed * math.cos(math.radians(angle)) 
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y) # specified decimal places


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        tileList = [(x, y) for x in range(0, self.width) for y in range(0, self.height)]
        # print(tileList)
        self.cleanMap = {tile:False for tile in tileList}
        # print(self.cleanMap)

    def Tile(self, pos):
        """ 
        converts the float coordinates in pos to integer coordinates marking a tile
        pos: a Position
        returns a tuple of 2 integers m, n denoting a tile (named after the upper left corner)
        Note that positions on the extreme edge are not allowed in the problem
        -- that is, in a 2x2 room (2.00, 2.00) is not in the room.
        """
        m = math.floor(pos.getX())
        n = math.floor(pos.getY())
        return (m, n)
        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        
        (m, n) = self.Tile(pos)
        self.cleanMap[(m, n)] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.cleanMap[(m,n)]
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # Add up the True values for each key in the dict
        
        return sum(self.cleanMap.values()) # True is an integer of value 1

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # random.seed() # initialize the randomness every time called
        randX = random.random()*self.width
        randY = random.random()* self.height
        return Position(randX,randY)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.getX() >= 0 and pos.getY() >= 0:
            if pos.getX() < self.width and pos.getY() < self.height:
                return True
            else:
                return False
        else:
            return False


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        
        # random position: 2 random floats within the range [0,w), [0, h)
        # random.seed() # initialize the randomness every time called
        posX = random.random() * room.width
        posY = random.random() * room.height
        
        self.Pos = Position(posX,posY)

        # random direction: random integer [0, 360)
        self.Dir = random.randrange(0,360) # note that lowercase dir is reserved
        
        # clean the tile it is on using cleanTileAtPosition
        room.cleanTileAtPosition(self.Pos)
        

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.Pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.Dir

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        newX = position.getX()
        newY = position.getY()
        self.Pos = Position(newX, newY)

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.Dir = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


# Uncomment this line to see your implementation of StandardRobot in action!
##testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    raise NotImplementedError

# Uncomment this line to see how much your simulation takes on average
##print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#===========================================
# Testing
#===========================================

# ==== Playing with Position class ====
#x=1
#y=1
#angle = 88
#speed = 5
#pos = Position(x,y)
#print(pos)
#pos = Position.getNewPosition(pos,angle, speed)
#print(pos)
#currx = pos.getX()
#print("%0.2f" % currx) # print with precision but leave value intact

# ==== Testing Problem 1 -- Rectangular Room ====

#random.seed(0) # for predictable testing
#w = 2
#h = 2
#room = RectangularRoom(w,h)

# ---- get numTiles ----
#todo = room.getNumTiles()
#print(str(todo))

# ---- isPositionInRoom ----
#x=2.00
#y=2.00
#pos = Position(x,y)
#print(room.isPositionInRoom(pos))

# ---- getRandomPosition, getNumTiles, getNumCleanedTiles,  ---
# ---- cleanTileAtPosition, isTileCleaned ----

#for i in range (0,10):
#    pos = room.getRandomPosition()
#    x = pos.getX()
#    y = pos.getY()
#    print(pos, "is in room?", room.isPositionInRoom(pos))
#    print("There are",str(room.getNumTiles()), "tiles, of which", \
#          str(room.getNumCleanedTiles()), "are clean.")
#    print("For position",pos,"the tile is"+str(room.Tile(pos)))

#    (m,n) = room.Tile(pos)

#    if room.isTileCleaned(m,n): # test isTileCleaned
#        print("clean!")
#    else:
#        print("dirty!")
#        if i%2 == 0: # clean some of the tiles
#            room.cleanTileAtPosition(pos)
#        if room.isTileCleaned(m,n):
#            print("now clean!")
#        else:
#            print("still dirty!")

# ====== Testing Problem 2 -- Robot =======

random.seed(0) # for predictable testing
w = 2
h = 2
speed = 1
x=1.40
y=1.60
newDirection = 95
newPos = Position(x,y)
#print("the position chosen is", newPos)
room = RectangularRoom(w,h)

# ----- initializing a Robot -----
robbie = Robot(room, speed) 

# ---- testing 'getters'----
pos = robbie.getRobotPosition() 
direct = robbie.getRobotDirection()
print("Initial position, direction are", str(pos), str(direct))

# ---- testing 'setters' ----
#robbie.setRobotPosition(newPos)
#robbie.setRobotDirection(newDirection)
#pos = robbie.getRobotPosition()
#direct = robbie.getRobotDirection()
#print("New position, direction are", str(pos), str(direct))

#  --- testing if the initial tile is cleaned ----
(m,n) = room.Tile(pos)
if room.isTileCleaned(m,n): # test isTileCleaned
    print("initial position clean!")
else:
    print("initial position dirty!")
    

