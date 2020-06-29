from math import *
from ps1a import isPrime

##Problem 2.
##Write a program that computes the sum of the logarithms of all the primes from 2 to some
##number n, and print out the sum of the logs of the primes, the number n, and the ratio of these
##two quantities. Test this for different values of n.
##You should be able to make only some small changes to your solution to Problem 1 to solve this
##problem as well.
##Hints:
##While you should see the ratio of the sum of the logs of the primes to the value n slowly get
##closer to 1, it does not approach this limit monotonically.

logsum = 0
MAXNUM = 2000

for i in range(2, MAXNUM+1) :
	if isPrime(i):
		print(i, log(i))
		logsum += log(i)	

print('')
print('logsum: ', logsum)
print('max prime: ', MAXNUM)
print('ratio: ', logsum/MAXNUM)
print('')