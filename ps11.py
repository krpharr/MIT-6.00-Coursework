# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import ps11_visualize
import matplotlib.pyplot as plt


import math
import random

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
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

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2
class Tile(object):
	def __init__(self, m, n):
		self.m = m  #tile array x
		self.n = n  #tile array y
		self.clean = False
	def positionInTile(self, position):
		if int(position.x) == self.m and int(position.y) == self.n:
			return True
		else: return False
	def cleanTile(self):
		self.clean = True 
	def dirtyTile(self):
		self.clean = False
	def isClean(self):
		return self.clean
	def getM(self):return self.m
	def getN(self):return self.n

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
		self.numTiles = width*height
		self.tiles = []
		for i in range(0, width):
			for j in range(0, height):
				self.tiles.append(Tile(i, j))
				
		
	def cleanTileAtPosition(self, pos):
		"""
		Mark the tile under the position POS as cleaned.
		Assumes that POS represents a valid position inside this room.
	
		pos: a Position
		"""
		for i in self.tiles:
			if i.positionInTile(pos):
				i.cleanTile()
				
	def isTileCleaned(self, m, n):
		"""
		Return True if the tile (m, n) has been cleaned.
	
		Assumes that (m, n) represents a valid tile inside the room.
	
		m: an integer
		n: an integer
		returns: True if (m, n) is cleaned, False otherwise
		"""
		for i in self.tiles:
			if i.getM() == m and i.getN() == n:
				return i.isClean()
	def dirtyRoom(self):
		for i in self.tiles:
			i.dirtyTile()
	def getNumTiles(self):
		"""
		Return the total number of tiles in the room.
	
		returns: an integer
		"""
		return self.numTiles
	def getNumCleanedTiles(self):
		"""
		Return the total number of clean tiles in the room.
	
		returns: an integer
		"""
		r = 0
		for i in self.tiles:
			if i.isClean(): r += 1
		return r
	def getRandomPosition(self):
		"""
		Return a random position inside the room.
	
		returns: a Position object.
		"""
		p = Position(random.randrange(0, self.width), random.randrange(0, self.height))
		return p
	def isPositionInRoom(self, pos):
		"""
		Return True if POS is inside the room.
	
		pos: a Position object.
		returns: True if POS is in the room, False otherwise.
		"""
		if pos.getX() >= 0.0 and pos.getX() < float(self.width):
			if pos.getY() >= 0.0 and pos.getY() < float(self.height):
				return True
		return False
	

class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = random.randrange(0, 360)
        self.position = room.getRandomPosition()
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction


class Robot(BaseRobot):
	"""
	A Robot is a BaseRobot with the standard movement strategy.
	
	At each time-step, a Robot attempts to move in its current
	direction; when it hits a wall, it chooses a new direction
	randomly.
	"""
	def updatePositionAndClean(self):
		"""
		Simulate the passage of a single time-step.
	
		Move the robot to a new position and mark the tile it is on as having
		been cleaned.
		"""
		newposition = self.position.getNewPosition(self.direction, self.speed)
		while not self.room.isPositionInRoom(newposition):
			self.direction = random.randrange(0, 360)
			newposition = self.position.getNewPosition(self.direction, self.speed)
		self.position = newposition
		self.room.cleanTileAtPosition(self.position)
			
# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
	"""
	Runs NUM_TRIALS trials of the simulation and returns a list of
	lists, one per trial. The list for a trial has an element for each
	timestep of that trial, the value of which is the percentage of
	the room that is clean after that timestep. Each trial stops when
	MIN_COVERAGE of the room is clean.
	
	The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
	each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.
	
	Visualization is turned on when boolean VISUALIZE is set to True.
	
	num_robots: an int (num_robots > 0)
	speed: a float (speed > 0)
	width: an int (width > 0)
	height: an int (height > 0)
	min_coverage: a float (0 <= min_coverage <= 1.0)
	num_trials: an int (num_trials > 0)
	robot_type: class of robot to be instantiated (e.g. Robot or
				RandomWalkRobot)
	visualize: a boolean (True to turn on visualization)
	"""
	robots = []
	room = RectangularRoom(width, height)
	for i in range(0, num_robots):
		robots.append(robot_type(room, speed))
	trial = []
	for i in range(0, num_trials):
		if visualize: anim = ps11_visualize.RobotVisualization(num_robots, width, height)
		j = []
		percentage = .01 * (float(room.getNumCleanedTiles()) * (100.0 / float(room.getNumTiles())))
		while percentage < min_coverage:
				for r in robots:
					r.updatePositionAndClean()
				percentage = .01 * (float(room.getNumCleanedTiles()) * (100.0 / float(room.getNumTiles())))
				j.append(percentage)
				if visualize: anim.update(room, robots)
		if percentage >= min_coverage:
			""" finished cleaning
			"""
			trial.append(j)
			if visualize: anim.done()
		room.dirtyRoom()
	return trial
			
		
	
# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
	"""
	How long does it take a single robot to clean 75% of each of the following types of rooms:
	5x5, 10x10, 15x15, 20x20, 25x25? Output a figure that plots the mean time (on the Y-axis)
	against the area of the room.
	""" 
	rm = 1 # 1 of 5 diff room sizes
	px = []
	py = []
	s = 5
	while rm <= 5:
		avg = runSimulation(1, 1.0, rm*s, rm*s, 1.0, 1, Robot, False)
		testavg = .75
		count = []
		for i in range(0, len(avg)):
			#print "trial ", i,
			c = 0
			for j in range(0, len(avg[i])):
				if avg[i][j] < testavg:
					c += 1
			count.append(c)
		t = 0
		for i in count:
			t += i
		a = t/len(count)
		px.append((rm*s)**2)
		print rm, s
		py.append(a)
		rm += 1
		
	print px, py
	plt.plot(px, py)
	#plt.plot([5, 20, 45, 80, 125] [32, 601, 2940, 9584, 23333]))
	plt.axis([25, 625, 0, 1000])
	plt.title('Time to clean 75% of room with 1 robot. Rooms of various sizes')
	plt.xlabel('Room area')
	plt.ylabel('Timesteps')
	plt.show()
-	

def showPlot2():
	"""
	Produces a plot showing dependence of cleaning time on number of robots.
	How long does it take to clean 75% of a 25x25 room with each of 1-10 robots? Output a
	figure that plots the mean time (on the Y-axis) against the number of robots.
	"""
	px = []
	py = []
	numbots = 1
	while numbots <= 10:
		print "Cleaning room with ", numbots, "robots..."
		avg = runSimulation(numbots, 1.0, 25, 25, 1.0, 1, Robot, False)
		testavg = .75
		count = []
		for i in range(0, len(avg)):
			#print "trial ", i,
			c = 0
			for j in range(0, len(avg[i])):
				if avg[i][j] < testavg:
					c += 1
			count.append(c)
		t = 0
		for i in count:
			t += i
		a = t/len(count)
		px.append(numbots)
		py.append(a)
		print px, py
		numbots += 1
		
	print px, py
	plt.plot(px, py)
	plt.axis([1, 10, 0, 1000])
	plt.title('Time to clean 75% of room with 1 robot. Rooms of various sizes')
	plt.xlabel('Number of Robots')
	plt.ylabel('Timesteps')
	plt.show()
	

def showPlot3():
	"""
	How long does it take two robots to clean 75% of rooms with dimensions 20x20, 25x16,
	40x10, 50x8, 80x5, and 100x4? (Notice that the rooms have the same area.) Output a
	figure that plots the mean time (on the Y-axis) against the ratio of width to height.
	Produces a plot showing dependence of cleaning time on room shape.
	"""
	x = [20,25,40,50,80,100]
	y = [20,16,10,8,5,4]
	px = []
	py = []
	for e in range(0, len(x)):
		print "Cleaning ", x[e], "x", y[e], "room"
		avg = runSimulation(2, 1.0, x[e], y[e], 1.0, 1, Robot, False)
		testavg = .75
		count = []
		for i in range(0, len(avg)):
			#print "trial ", i,
			c = 0
			for j in range(0, len(avg[i])):
				if avg[i][j] < testavg:
					c += 1
			count.append(c)
		t = 0
		for i in count:
			t += i
		a = t/len(count)
		px.append(x[e]/y[e])
		py.append(a)
		print px, py
		
	print px, py
	plt.plot(px, py)
	plt.axis([1, 25, 0, 500])
	plt.title('2 Robots cleaning %75 of rooms of same area with different widths and heights')
	plt.xlabel('Ratio of width to height')
	plt.ylabel('Timesteps')
	plt.show()



def showPlot4():
	"""
	Produces a plot showing cleaning time vs. percentage cleaned, for
	each of 1-5 robots.
	How does the time it takes to clean a 25x25 room vary as min_coverage changes? Output a
	figure that plots mean time (on the Y-axis) against the percentage cleaned, for each of 1-5
	robots. Your plot will have multiple curves.
	
	for i in range(numbots):
	    plot(x[i],y[i],label='robots: %d' % i
	legend(title='Trials')
	
	"""
	px = []
	py = []
	numbots = 1
	while numbots <= 5:
		print "Cleaning 25x25 room with ", numbots, "robots..."
		avg = runSimulation(numbots, 1.0, 25, 25, 1.0, 1, Robot, False)
		a = [] 
		tavg = []
		count = []
		for ta in range(25, 101, 5):
			tavg.append(ta * .01)
			_ta = ta * .01
			for i in range(0, len(avg)):
				#print "trial ", i,
				c = 0
				for j in range(0, len(avg[i])):
					if avg[i][j] < _ta:
						c += 1
				count.append(c)
			t = 0
			for i in count:
				t += i
			a.append(t/len(count))
		px.append(tavg)
		py.append(a)
		#print px, py
		numbots += 1
		
	#print px, py
	#plt.plot(px, py)
	for i in range(0, len(px)):
	    plt.plot(px[i],py[i],label='robots: %d' % (i+1))
	plt.legend(loc=2, title='Trials')
	
	plt.axis([.25, 1.0, 0, 1000])
	plt.title('Cleaning time vs. percentage cleaned, for each of 1-5 robots.')
	plt.xlabel('Percentage Cleaned')
	plt.ylabel('Timesteps')
	plt.show()
	


# === Problem 5

class RandomWalkRobot(BaseRobot):
	"""
	A RandomWalkRobot is a robot with the "random walk" movement
	strategy: it chooses a new direction at random after each
	time-step.
	"""
	def updatePositionAndClean(self):
		"""
		Simulate the passage of a single time-step.
	
		Move the robot to a new position and mark the tile it is on as having
		been cleaned.
		"""
		newposition = self.position.getNewPosition(self.direction, self.speed)
		while not self.room.isPositionInRoom(newposition):
			self.direction = random.randrange(0, 360)
			newposition = self.position.getNewPosition(self.direction, self.speed)
		self.position = newposition
		self.direction = random.randrange(0, 360)
		self.room.cleanTileAtPosition(self.position)


# === Problem 6

def showPlot5():
	"""
	Produces a plot comparing the two robot strategies.
	"""
	px = []
	py = []
	numbots = 1
	while numbots <= 5:
		print "Cleaning 25x25 room with ", numbots, "robots..."
		avg = runSimulation(numbots, 1.0, 25, 25, 1.0, 1, Robot, False)
		a = [] 
		tavg = []
		count = []
		for ta in range(25, 101, 5):
			tavg.append(ta * .01)
			_ta = ta * .01
			for i in range(0, len(avg)):
				#print "trial ", i,
				c = 0
				for j in range(0, len(avg[i])):
					if avg[i][j] < _ta:
						c += 1
				count.append(c)
			t = 0
			for i in count:
				t += i
			a.append(t/len(count))
		px.append(tavg)
		py.append(a)
		#print px, py
		numbots += 1
	px2 = []
	py2 = []
	numbots = 1
	while numbots <= 5:
		print "Cleaning 25x25 room with ", numbots, "robots..."
		avg = runSimulation(numbots, 1.0, 25, 25, 1.0, 1, Robot, False)
		a = [] 
		tavg = []
		count = []
		for ta in range(25, 101, 5):
			tavg.append(ta * .01)
			_ta = ta * .01
			for i in range(0, len(avg)):
				#print "trial ", i,
				c = 0
				for j in range(0, len(avg[i])):
					if avg[i][j] < _ta:
						c += 1
				count.append(c)
			t = 0
			for i in count:
				t += i
			a.append(t/len(count))
		px2.append(tavg)
		py2.append(a)
		numbots += 1
	
	plt.figure(1)
	for i in range(0, len(px)):
	    plt.plot(px[i],py[i],label='Robots: %d' % (i+1))
	    plt.plot(px2[i],py2[i],label='RandomWalkRobots: %d' % (i+1))
	plt.legend(loc=2, title='Trials')
	plt.axis([.25, 1.0, 0, 1000])
	plt.title('Cleaning time vs. percentage cleaned, \nRobot vs RandomWalkRobot, for each of 1-5 robots.')
	plt.xlabel('Percentage Cleaned')
	plt.ylabel('Timesteps')
	plt.show()
	
showPlot5()
