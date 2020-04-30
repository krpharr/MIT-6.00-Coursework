 #Problem 1.
#Write a program that computes and prints the 1000th prime number.
import math

def isPrime(n):
	#returns 1 if n is prime and 0 if not
	if n < 2: return 0
	i = 2
	while i < int(n**0.5)+1: #dont completely understand why but don't need to look past the square root of n
		if n%i == 0:
			return 0
		i = i + 1;
	return 1;

count = 1  #count which prime number we are on.  Starting with 2
cur = 3		#current number being tested

print 'Processing'   #doing something

while count < 1000:
	if isPrime(cur):
		count = count + 1
		if count == 1000: 
			print 'The 1000th prime number:', cur
	cur = cur + 2
		



