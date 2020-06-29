from string import *

def countSubStringMatch(target,key):
	i = 0
	numMatch = 0
	while i != -1:
		i = target.find(key, i)
		if i != -1:	
			numMatch += 1
			i += 1
	return numMatch
	
def countSubStringMatchRecursive (target, key):
	numMatch = 0
	i = 0
	i = target.find(key, i)
	if i != -1:
		numMatch = 1
		s = target[i+1:len(target)]
		numMatch += countSubStringMatchRecursive(s, key)
	return numMatch
	
print(countSubStringMatch("qwertyqwertyqwertyqwertyqwerty", "ert"))
print(countSubStringMatchRecursive("qwertyqwertyqwertyqwertyqwerty", "ert"))



