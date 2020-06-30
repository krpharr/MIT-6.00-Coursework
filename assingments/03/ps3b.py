from string import *

def subStringMatchExact(target,key):
	startpoint = ()
	i = 0
	while i != -1:
		i = target.find(key, i)
		if i != -1:	
			startpoint += (i,)
			i += 1
	return startpoint
	

