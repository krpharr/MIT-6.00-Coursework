# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.

def get_user_input():
	"""call recursively till a valid entry is entered"""
	c = raw_input("")
	if c in string.ascii_letters:
		c = string.lower(c)
	else:
		print "Invalid entry."
		return None
	return c
	
def evaluate_fragment(frag):
	"""looks for frag in word list plus one more character returns True if it is as word fragment
	"""
	if len(frag) == 1: return True
	for word in wordlist:
		if word[0:len(frag)] == frag and len(word) > len(frag):
			return True
	return False
	
				
def is_valid_word(word):
	valid = False
	for wrd in wordlist:
		if wrd == word:
			return True	
	return valid	
	
def is_frament_word(frag):
	"""is frag a word and is it 3 or more letters long"""
	if len(frag) <= 3: return False
	if len(frag) >= 3:
		if is_valid_word(frag):
			return True
	return False
		


# TO DO: your code begins here!
def ghost():
	player1 = "Player 1"
	player2 = "Player 2"
	cur_player = player1
	fragment = ""
	index = 0
	newgame = True
	play = True
	rules = "Rules of Ghost\n"
	rules += "Players form a word by alternating turns saying a letter, \n"
	rules += "which is added on to the end of the word fragment.\n" 
	rules += "There are two ways to lose Ghost:\n"
	rules += "1) Forming a word longer than 3 letters ('PEA' is ok, but 'PEAR' is not).\n"
	rules += "2) Creating a fragment (of any size) which cannot become a word by \n"
	rules += "adding more letters (for example, 'QZ').\n"
	
	
	print 
	print "Welcome to Ghost:"
	print
	print rules
		
	while play:
		if newgame:
			cur_player = player1
			newgame = False
			fragment = ""
			print "New Game!"
			print
			print "Player 1 goes first"
			print "Pick a letter."
		else:
			print "Current word fragment: '", fragment,"'"
			print cur_player, "'s turn.",
		
		c = get_user_input()
		
		fragment += c
		
		if evaluate_fragment(fragment) == False or is_frament_word(fragment) == True:
			s = ""
			if evaluate_fragment(fragment) == False:
				s = fragment, " is a bad word fragment."
			if is_frament_word(fragment) == True:
				s = fragment, " is a word longer than 3 letters."
			print cur_player, " loses!", s
			k = "q"
			while k != "n" and k != "." and k != 'r':
				k = raw_input("Press 'n' for new game, 'r' for rules and '.' to quit.")
			if k == ".":
				play = False
			if k == "n":
				newgame = True
			if k == "r":
				print
				print rules
				newgame = True
		else:
			if cur_player == player1:
				cur_player = player2
			else:
				cur_player = player1


			
		
wordlist = load_words()
ghost()

			
	
	
