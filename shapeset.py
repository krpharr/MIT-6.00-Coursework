from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
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
        
class ShapeSet:
	def __init__(self):
		"""
		Initialize any needed variables
		"""
		# TO DO
	def addShape(self, sh):
		"""
		Add shape sh to the set; no two shapes in the set may
		be equal
		sh: shape to be added
		"""
		print "adding ", sh
	def __iter__(self):
		"""
		Return an iterator that allows you to iterate over the
		set of shapes, one shape at a time
		"""
		# TO DO
	def __str__(self):
		"""
		Return the string representation for a set, which
		consists of the string representation of each shape,
		categorized by type.
		"""
		# TO DO

s = ShapeSet()
sq = Square(5)
s.addShape(sq)
