VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
time_limit = 0.01


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

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
def str2list(s):
	"""returns list of characters in the string"""
	word = []
	for c in s:
		word.append(c)
	return word
	
def list2str(word):
	s = ""
	for c in word:
		s += c
	return s
	
def copyList(clist):
	nlist = []
	for i in clist:
		nlist.append(i)
	return nlist;
	
def sort_word(word):
	"""return LIST of word sorted from a-z
	"""
	w = []
	i = 0
	for l in word:
		w.append(l)
	selSort(w)
	return w
			
def selSort(L):
	for i in range(len(L) - 1):
		#print L
		minIndx = i
		minVal= L[i]
		j = i + 1
		while j < len(L):
			if minVal > L[j]:
				minIndx = j
				minVal= L[j]
			j = j + 1
		temp = L[i]
		L[i] = L[minIndx]
		L[minIndx] = temp
		


def solve_subs(word, d):
	"""word is a string , d is the DICT that stores all subs and their word scores
	"""
	w = str2list(word)
	if len(word) > 2:
		for i in range(0, len(w)):
			sub = copyList(w)
			del sub[i]
			selSort(sub)
			s = list2str(sub)
			if d.get(s, 0) == 0:
				d[s] = get_word_score(s, HAND_SIZE)
				print s
				solve_subs(s, d)
			


mylist =  str2list("randall")
d = {}
solve_subs(mylist, d)
print d
