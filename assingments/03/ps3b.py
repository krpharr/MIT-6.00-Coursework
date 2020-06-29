from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExact(target,key):
	startpoint = ()
	i = 0
	while i != -1:
		i = find(target, key, i)
		if i != -1:	
			startpoint += (i,)
			i += 1
	return startpoint
	
print target1, key10
print subStringMatchExact(target1,key10)
print target1, key11
print subStringMatchExact(target1,key11)
print target1, key12 
print subStringMatchExact(target1,key12)
print target1, key13 
print subStringMatchExact(target1,key13)
print target2, key10
print subStringMatchExact(target2,key10)
print target2, key11
print subStringMatchExact(target2,key11)
print target2, key12 
print subStringMatchExact(target2,key12)
print target2, key13 
print subStringMatchExact(target2,key13)
