# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.name = "square"
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.name = "circle"
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: base of the triange
        height: height of the triange
        """
        self.name = "triangle"
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """
        Returns approximate area of the triangle
        """
        return .5*self.base*self.height
    def __str__(self):
        return 'Triangle with base %.2f and height %.2f ' %(self.base, self.height)
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height
#################
#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
	def __init__(self):
		"""
		shapes is an array of shapes in the set that pass the test
		"""
		self.shapes = []
		self.index = 0
	def addShape(self, sh):
		"""
		Add shape sh to the set; no two shapes in the set may be
		identical
		sh: shape to be added
		"""
		inSet = False
		for i in range(0, len(self.shapes)):
			if sh == self.shapes[i]: 
				inSet = True
				print "Unable to add to set: ", sh
		if not inSet: 
			self.shapes.append(sh)
			self.index = len(self.shapes)
	def __len__(self):
		return len(self.shapes)
	def __iter__(self):
		"""
		Return an iterator that allows you to iterate over the set of
		shapes, one shape at a time
		"""
		self.index = len(self.shapes)
		return self
	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.shapes[self.index]	
	def sort(self):
		"""
		sort set based on type and size of area
		"""
		self.shapes.sort()
		#self.shapes = sorted(self.shapes, key=lambda k: (k['name']))
	def __str__(self):
		"""
		Return the string representation for a set, which consists of
		the string representation of each shape, categorized by type
		(circles, then squares, then triangles)
		"""
		self.sort()
		s = ""
		for i in range(0, len(self.shapes)):
			s += "%s\n" % str(self.shapes[i])
		return s

#s = ShapeSet()
#t = Triangle(9, 6)
#sq = Square(6)
#c = Circle(4)
#c2 = Circle(4)
#s.addShape(t)
#s.addShape(sq)
#s.addShape(c)
#s.addShape(c2)
#print str(s)
#for i in s:
	#print i
#for i in s:
	#print i
		
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
	"""
	Returns a tuple containing the elements of ShapeSet with the
	   largest area.
	shapes: ShapeSet
	"""
	largest = 0.0
	largestShapes = ()
	for i in shapes:
		if i.area() > largest:
			largest = i.area()
	for i in shapes:
		if i.area() == largest:
			largestShapes += (i,)
	return largestShapes
		

#t = Triangle(6,6)
#c = Circle(1)
#ss = ShapeSet()
#ss.addShape(t)
#ss.addShape(c)
#largest = findLargest(ss)
#print largest
#print largest[0] is t
#print largest[0] is c

		
		

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    print "Loading shapes from file..."
    # inFile: file
    inFile = open(filename, 'r', 0)
    ss = ShapeSet()
    for line in inFile:
		s = line.strip("\n")
		s = s.split(",")
		if s[0] == "circle": ss.addShape(Circle(float(s[1])))
		if s[0] == "square": ss.addShape(Square(float(s[1])))
		if s[0] == "triangle": ss.addShape(Triangle(float(s[1]), float(s[2])))
    print "  ", len(ss), "shapes loaded."
    return ss

shapes = readShapesFromFile("shapes.txt")
print shapes
