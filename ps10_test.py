import ps10; reload(ps10)
from ps10 import *

def isClose(float1, float2):
    """
    Helper function - are two floating point values close?
    """
    return abs(float1 - float2) < .01

def testResult(boolean):
    """
    Helper function - print 'Test Failed' if boolean is false, 'Test
    Succeeded' otherwise.
    """
    if boolean:
        print 'Test Succeeded'
    else:
        print 'Test Failed'

def testHand():
    """
    Test the hand class. Add your own test cases
    """
    h = Hand(8, {'a':3, 'b':2, 'd':3})
    h.update('bad')
    testResult(h.containsLetters('aabdd') and not h.isEmpty())
    h.update('dad')
    testResult(h.containsLetters('ab') or not h.isEmpty())
    h.update('ab')
    testResult(h.isEmpty())

def testPlayer():
    """
    Test the Player class. Add your own test cases.
    """
    p = Player(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(type(p.getHand()) == Hand)
    p.addPoints(5.)
    p.addPoints(12.)
    testResult(isClose(p.getPoints(), 17))

def testComputerPlayer():
    """
    Test the ComputerPlayer class. Add your own test cases.
    """
    wordlist = Wordlist()
    p = ComputerPlayer(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(getWordScore(p.pickBestWord(wordlist)) == getWordScore('abode'))

def testAll():
	"""
	Run all Tests
	"""
	
	#h = Hand(3, {'a':2, 's':1})
	#h2 = Hand(3, {'a':1, 's':2})
	#h3 = Hand(3, {'s':2, 'a':1})
	#print h, h2, h3
	#print h == h2
	#print h2 == h3
	#print h2.containsLetters("ass")
	#print h.containsLetters("ass")
	#h.update("as")
	#print h.isEmpty()
	#print h
	#h.update("a")
	#print h.isEmpty()
	#print h
	
	
	testHand()
	
	testPlayer()
	
	# print 'PROBLEM 4 -----------------------------------------'
	testComputerPlayer()
	
testAll()
	
