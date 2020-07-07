# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
time_limit = 0.01


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

def get_time_limit(points_dict, k):
	"""
	Return the time limit for the computer player as a function of the
	multiplier k.
	points_dict should be the same dictionary that is created by
	get_words_to_points.
	"""
	start_time = time.time()
	# Do some computation. The only purpose of the computation is so we can
	# figure out how long your computer takes to perform a known task.
	for word in points_dict:
		get_frequency_dict(word)
		get_word_score(word, HAND_SIZE)
	end_time = time.time()
	return (end_time - start_time) * k

def pick_best_word(hand, points_dict):
	"""
	Return the highest scoring word from points_dict that can be made with the
	given hand.
	Return '.' if no words can be made with the given hand.
	"""
	results = {}
	for word in points_dict:
		if is_valid_word(word, hand, points_dict):
			results[word] = results.get(word,0)+get_word_score(word, HAND_SIZE)
	high = 0
	bestword = ""
	r = ""
	for r in results:
		#print r, results[r]
		if results[r] > high:
			bestword = r
			high = results[r]
	if r != "":
		return bestword
	return "."		
		

def get_words_to_points(word_list):
	"""
	Return a dict that maps every word in word_list to its point value.
	"""
	pd = {}
	for w in word_list:
		pd[w] = pd.get(w, 0) + get_word_score(w, HAND_SIZE)
	return pd




def get_word_score(word, n):
	"""
	Returns the score for a word. Assumes the word is a
	valid word.
	
	The score for a word is the sum of the points for letters
	in the word, plus 50 points if all n letters are used on
	the first go.
	
	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
	
	word: string (lowercase letters)
	returns: int >= 0
	"""
	score = 0
	for c in word:
		score += SCRABBLE_LETTER_VALUES[c]
	if len(word) == n:
		score += 50
	return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
	"""
	Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 
	
	Updates the hand: uses up the letters in the given word
	and returns the new hand, without those letters in it.
	
	Has no side effects: does not mutate hand.
	
	word: string
	hand: dictionary (string -> int)    
	returns: dictionary (string -> int)
	"""
	# TO DO ...
	w = {}
	for c in word:
		w[c] = w.get(c, 0) + 1
	_hand = {}
	for letter in hand:
		_hand[letter] = hand.get(letter, 0) - w.get(letter, 0)
	newhand = {}
	for letter in _hand:
		if _hand.get(letter, 0) != 0:
			newhand[letter] = _hand.get(letter, 0)
	return newhand
		

		
		

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, points_dict):
	"""
	Returns True if word is in the word_list and is entirely
	composed of letters in the hand. Otherwise, returns False.
	Does not mutate hand or word_list.
	
	word: string
	hand: dictionary (string -> int)
	word_list: list of lowercase strings
	"""
	valid = False
	if points_dict.get(word, 0):
			valid = True
	w = get_frequency_dict(word)
	for letter in w:
		if hand.get(letter, 0) < w.get(letter, 0): 
			valid = False
	return valid
	


def play_hand(hand, points_dict):
	"""
	Allows the user to play the given hand, as follows:
	
	* The hand is displayed.
	
	* The user may input a word.
	
	* An invalid word is rejected, and a message is displayed asking
	  the user to choose another word.
	
	* When a valid word is entered, it uses up letters from the hand.
	
	* After every valid word: the score for that word and the total
	  score so far are displayed, the remaining letters in the hand 
	  are displayed, and the user is asked to input another word.
	
	* The sum of the word scores is displayed when the hand finishes.
	
	* The hand finishes when there are no more unused letters.
	  The user can also finish playing the hand by inputing a single
	  period (the string '.') instead of a word.
	
	* The final score is displayed.
	
.
	  word_list: list of lowercase strings
	"""
	totalscore = 0
	time_limit = get_time_limit(points_dict, 3)
	print "%.2f second time limit" % time_limit
	print "Current Hand: ", 
	display_hand(hand)
	startTime = time.time()
	guess = pick_best_word(hand, points_dict)
	while guess != ".":
		if is_valid_word(guess, hand, points_dict):
			endTime = time.time()
			s = get_word_score(guess, HAND_SIZE)
			totalTime = endTime-startTime
			if totalTime == 0: totalTime = 0.01
			print 'It took %.2f' %totalTime,
			print " seconds for Acer to provide the answer %s." % guess
			timeLeft = time_limit - totalTime
			if timeLeft >= 0:
				score  = s/totalTime
				totalscore += score
				print "%.2f seconds remaining." % timeLeft
				if len(guess) == len(hand):
					print guess, 'earned %.2f points' % score
					guess = "."
				else:
					hand = update_hand(hand, guess)
					print guess, 'earned %.2f points' % score
					print "Total points: %.2f" % totalscore
					print "Current Hand: ", 
					display_hand(hand)
					guess = pick_best_word(hand, points_dict)
			else:
				print 'Total time exceeds %.2f seconds. Acer scored %.2f points.' % (time_limit, totalscore)
				guess = "."
		else:
			print guess, "is invalid.",
			guess = pick_best_word(hand, points_dict)
	print "Total points: %.2f" % totalscore
	print "Round over...."



#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    firstTime = True
    hand = deal_hand(HAND_SIZE) # random init
    while True:
		if firstTime:
			firstTime = False
			cmd = raw_input('Enter n to deal a hand and begin, or e to end game: ')
		else:
			cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
		if cmd == 'n':
			hand = deal_hand(HAND_SIZE)
			play_hand(hand.copy(), points_dict)
			print
		elif cmd == 'r':
			play_hand(hand.copy(), points_dict)
			print
		elif cmd == 'e':
			break
		else:
			print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    play_game(points_dict)

