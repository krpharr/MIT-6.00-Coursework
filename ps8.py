# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
	"""
	Returns a dictionary mapping subject name to (value, work), where the name
	is a string and the value and work are integers. The subject information is
	read from the file named by the string filename. Each line of the file
	contains a string of the form "name,value,work".
	
	returns: dictionary mapping subject name to (value, work)
	"""
	
	# The following sample code reads lines from the specified file and prints
	# each one.
	d = {}
	inputFile = open(filename)
	for line in inputFile:
		s = line.strip("\n")
		s = s.split(",")
		d[s[0]] = (int(s[1]), int(s[2]))
		
	inputFile.close()
	return d


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
	"""
	Returns a dictionary mapping subject name to (value, work) which includes
	subjects selected by the algorithm, such that the total work of subjects in
	the dictionary is not greater than maxWork.  The subjects are chosen using
	a greedy algorithm.  The subjects dictionary should not be mutated.
	
	subjects: dictionary mapping subject name to (value, work)
	maxWork: int >= 0
	comparator: function taking two tuples and returning a bool
	returns: dictionary mapping subject name to (value, work)
	"""
	d = {}
	solve_subs(subjects, maxWork, comparator, d)
	return d

def solve_subs(subjects, maxWork, comparator, d):
	"""
	"""
	i = True
	hours = 0
	for s in subjects:
		if i:
			best = subjects[s]
			bestsub = s
			#print "best", best
			i = False
		if comparator(subjects[s], best):
			if subjects[s][1] <= maxWork:
				best = subjects[s]
				bestsub = s
	if best[1] <= maxWork:			
		d[bestsub] = subjects[bestsub]
		hours = d[bestsub][1]
		#print d[bestsub]
	sub = subjects.copy()
	del sub[bestsub]
	if len(sub):
		#print sub
		solve_subs(sub, maxWork-hours, comparator, d)
				
	
#subjects = loadSubjects("small_subject_catalog.txt")
subjects = loadSubjects("subjects.txt")
printSubjects(subjects)


#print "Value"
#courses = greedyAdvisor(subjects, 15, cmpValue)
#printSubjects(courses)
#courses = greedyAdvisor(subjects, 15, cmpWork)
#print "Work"
#printSubjects(courses)
#courses = greedyAdvisor(subjects, 15, cmpRatio)
#print "Ratio"
#printSubjects(courses)
	

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    print "calculating..."
    startTime = time.time()
    bfa = bruteForceAdvisor(subjects, 18)
    endTime = time.time()
    print bfa
    print "%.4f" % (endTime-startTime)


# Problem 3 Observation
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
# 11 hours to do catalog of 200 class
# 4 secs for catalog of 100
# tres exponential

#bruteForceTime()

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
	"""
	Returns a dictionary mapping subject name to (value, work) that contains a
	set of subjects that provides the maximum value without exceeding maxWork.
	
	subjects: dictionary mapping subject name to (value, work)
	maxWork: int >= 0
	returns: dictionary mapping subject name to (value, work)
	"""
	nameList = subjects.keys()
	tupleList = subjects.values()
	d = {}
	v = []
	w = []
	for t in tupleList:
		v.append(t[0])
		w.append(t[1])
	m = {}
	outputSubjects = {}
	res, classlist = fastMaxVal(w, v, len(v)-1, maxWork, m) 
	for i in classlist:
			outputSubjects[nameList[i]] = tupleList[i]
	#for i in m:
	#	print "name:", i, "value:",m[i]
	#bestSubset, bestSubsetValue = \
			#dpAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0, d)
	#for i in bestSubset:
		#outputSubjects[nameList[i]] = tupleList[i]
	return outputSubjects

def fastMaxVal(w, v, i, aW, m):
	#global numCalls
	#numCalls += 1
	try: return m[(i, aW)]
	except KeyError:
		if i == 0:
			if w[i] <= aW:
				m[(i, aW)] = v[i]
				return v[i], [i]
			else:
				m[(i, aW)] = 0
				return 0, []
		without_i, courselist = fastMaxVal(w, v, i-1, aW, m)
		if w[i] > aW:
			m[(i, aW)] = without_i, courselist
			return without_i, [i-1]
		else: with_i, courselist = v[i] + fastMaxVal(w, v, i-1, aW - w[i], m)
		res = max(with_i, without_i)
		m[(i, aW)] = res, courselist
	return res, classlist

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    print "calculating..."
    startTime = time.time()
    dpa = dpAdvisor(subjects, 20)
    endTime = time.time()
    #printSubjects(dpa)
    print "%.4f" % (endTime-startTime)

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

dpTime()
