from string import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExact(target,key):
	startpoint = ()
	i = 0
	while i != -1:
		i = target.find(key, i)
		if i != -1:	
			startpoint += (i,)
			i += 1
	return startpoint

def constrainedMatchPair(firstMatch,secondMatch,length):
	#n+m+1 = k
	matchedpair = ()
	for i in range(0, len(firstMatch)):
		for j in range(0, len(secondMatch)):
			if firstMatch[i] + length + 1 == secondMatch[j]:
				matchedpair += (firstMatch[i],)
	return matchedpair
		

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        #print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + (filtered, )
        #print target
        #print 'match1',match1
        #print 'match2',match2
        #print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
    
def subStringMatchExactlyOneSub(target,key):
	exactMatch = subStringMatchExact(target, key)
	oneSub = subStringMatchOneSub(key,target)
	solution = ()
	for i in range(0, len(oneSub)):
		foundelement = False
		for j in range(0, len(exactMatch)):
			if exactMatch[j] == oneSub[i]: foundelement = True
		if foundelement == False:
			solution += (oneSub[i],)
	return solution
			
print(target1, key12)
print(subStringMatchExactlyOneSub(target1,key12))	

    

