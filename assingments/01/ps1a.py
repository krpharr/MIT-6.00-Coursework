#Problem 1.
#Write a program that computes and prints the 1000th prime number.
import math

def isPrime(n):
  #
	# returns 1 if n is prime and 0 if not
  #
	if n < 2: return 0
	i = 2
	while i < int(n**0.5)+1: 
    #dont completely understand why but don't need to look past the square root of n
		if n%i == 0:
			return 0
		i = i + 1
	return 1

#index to count prime numbers found - [0] index is given, prime number 2
count = 1  
#current number to be tested - prime number 2 already given
cur = 3		
primeList = [2,]

while count < 1000:
  if isPrime(cur):
    primeList.append(cur)
    if count == 1000: 
      print('The 1000th prime number:', cur)
    count = count + 1
  cur = cur + 2

# print prime number list to verify data
# i = 1
# for n in primeList:
#   print(i, n)
#   i = i + 1


