from math import *

##Problem 2.
##Write a program that computes the sum of the logarithms of all the primes from 2 to some
##number n, and print out the sum of the logs of the primes, the number n, and the ratio of these
##two quantities. Test this for different values of n.
##You should be able to make only some small changes to your solution to Problem 1 to solve this
##problem as well.
##Hints:
##While you should see the ratio of the sum of the logs of the primes to the value n slowly get
##closer to 1, it does not approach this limit monotonically.

def isPrime(n):
	#returns 1 if n is prime and 0 if not
	if n < 2: return 0
	i = 2
	while i < int(n**0.5)+1: #dont completely understand why but don't need to look past the square root of n
		if n%i == 0:
			return 0
		i = i + 1;
	return 1;

logsum = 0;
MAXNUM = 100

for i in range(2, MAXNUM+1) :
	if isPrime(i):
		logsum += log(i)	

print logsum, logsum/MAXNUM
