def selSort(L):
	for i in range(len(L) - 1):
		print L
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
		
def testSelSort():
	test1 = ['r', 'a', 'n', 'd', 'a', 'l', 'l']
	raw_input('run selective test 1')
	selSort(test1)
	test2 = [6,1,2,3,4,5]
	raw_input('run selective test 2')
	selSort(test2)
	test3 = [6,5,4,3,2,1]
	raw_input('run selective test 3')
	selSort(test3)

testSelSort()
