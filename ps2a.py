
def solve(numNuggets):
	nSm = 0
	nMed = 0
	nLrg = 0
	#solve for large
	if numNuggets >= 20:
		if numNuggets%20 == 0:
			return (nSm, nMed, numNuggets/20)
		for i in range(0, numNuggets/20):
			nLrg = i + 1
			s = solve(numNuggets-(nLrg*20))
			if s != (None, None, None):
				return (s[0], s[1], nLrg+s[2])
		nLrg = 0
	#solve for med
	if numNuggets >= 9:
		if numNuggets%9 == 0:
			return (nSm, numNuggets/9, nLrg)
		for i in range(0, numNuggets/9):
			nMed = i + 1
			s = solve(numNuggets-(nMed*9))
			if s != (None, None, None):
				return (s[0], nMed+s[1], s[2])
		nMd = 0
	#solve for small
	if numNuggets >= 6:
		if numNuggets%6 == 0:
			return (numNuggets/6, nSm, nLrg)
		for i in range(0, numNuggets/6):
			nSm = i + 1
			s = solve(numNuggets-(nSm*6))
			if s != (None, None, None):
				return (nSm+s[0], s[1], s[2])
		nSm = 0
	return (None, None, None)
			



for i in range(6, 201):
	print i, solve(i)
