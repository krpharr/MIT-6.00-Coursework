
def solve(numNuggets, SMALL=6, MEDIUM=9, LARGE=20):
	nSm = 0
	nMed = 0
	nLrg = 0
	#solve for large
	if numNuggets >= LARGE:
		if numNuggets%LARGE == 0:
			return (nSm, nMed, numNuggets/LARGE)
		for i in range(0, numNuggets//LARGE):
			nLrg = i + 1
			s = solve(numNuggets-(nLrg*LARGE))
			if s != (None, None, None):
				return (s[0], s[1], nLrg+s[2])
		nLrg = 0
	#solve for med
	if numNuggets >= MEDIUM:
		if numNuggets%MEDIUM == 0:
			return (nSm, numNuggets/MEDIUM, nLrg)
		for i in range(0, numNuggets//MEDIUM):
			nMed = i + 1
			s = solve(numNuggets-(nMed*MEDIUM))
			if s != (None, None, None):
				return (s[0], nMed+s[1], s[2])
		nMd = 0
	#solve for small
	if numNuggets >= SMALL:
		if numNuggets%SMALL == 0:
			return (numNuggets/SMALL, nSm, nLrg)
		for i in range(0, numNuggets//SMALL):
			nSm = i + 1
			s = solve(numNuggets-(nSm*SMALL))
			if s != (None, None, None):
				return (nSm+s[0], s[1], s[2])
		nSm = 0
	return (None, None, None)
		
for i in range(6, 200):
	print(i, solve(i))
