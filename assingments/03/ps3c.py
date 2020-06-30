from string import *
from ps3b import subStringMatchExact

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

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
    print('breaking key',key,'into',key1,key2)
    # match1 and match2 are tuples of locations of start of matches
    # for each substring in target
    match1 = subStringMatchExact(target,key1)
    match2 = subStringMatchExact(target,key2)
    # when we get here, we have two tuples of start points
    # need to filter pairs to decide which are correct
    filtered = constrainedMatchPair(match1,match2,len(key1))
    allAnswers = allAnswers + (filtered, )
    print(target)
    print('match1',match1)
    print('match2',match2)
    print('possible matches for',key1,key2,'start at',filtered)
  return allAnswers
    
subStringMatchOneSub(key11,target1)
