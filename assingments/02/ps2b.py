
def solve(numNuggets, SMALL=6, MEDIUM=9, LARGE=20):
	nSmall = 0
	nMedium = 0
	nLarge = 0

	#solve for large
	if numNuggets >= LARGE:
		if numNuggets%LARGE == 0:
			return (nSmall, nMedium, numNuggets//LARGE)
		for i in range(0, numNuggets//LARGE):
			nLarge = i + 1
			# recursion 
			s = solve(numNuggets-(nLarge*LARGE))
			if s != (None, None, None):
				return (s[0], s[1], nLarge+s[2])
		nLarge = 0

	#solve for med
	if numNuggets >= MEDIUM:
		if numNuggets%MEDIUM == 0:
			return (nSmall, numNuggets//MEDIUM, nLarge)
		for i in range(0, numNuggets//MEDIUM):
			nMedium = i + 1
			s = solve(numNuggets-(nMedium*MEDIUM))
			if s != (None, None, None):
				return (s[0], nMedium+s[1], s[2])
		nMd = 0

	#solve for small
	if numNuggets >= SMALL:
		if numNuggets%SMALL == 0:
			return (numNuggets//SMALL, nSmall, nLarge)
		for i in range(0, numNuggets//SMALL):
			nSmall = i + 1
			s = solve(numNuggets-(nSmall*SMALL))
			if s != (None, None, None):
				return (nSmall+s[0], s[1], s[2])
		nSmall = 0

	# if none can be solved for any size return:
	return (None, None, None)
		

