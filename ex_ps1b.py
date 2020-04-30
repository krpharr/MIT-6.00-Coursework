from math import *


def isPrime(n):
    # 0 and 1 are not prime
    if n < 2:
        return False
    # 2 is prime
    if n == 2:
        return True
    # all other even numbers are not prime
    if not n & 1:       
        return False
    # range start at 3, and go to square root of n
    for i in range(3, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
 
def logPrimes(n):
    # list to hold prime numbers
    primeNums = []
    # iterator for while loop
    iter = 2
    # used to store the sum of logs
    sum = 0
     
    while iter < n:
        # if iter is prime
        if isPrime(iter):
            # add it to the list
            primeNums.append(iter)
            # increment sum of logs
            sum += log(iter)
        else:
            pass
        iter += 1
        print "N:",n,"Sum:",sum,"Ratio:",(sum / n)
    # print n, total sum, and ratio of sum and n
    print "N:",n,"Sum:",sum,"Ratio:",(sum / n)
    
logPrimes(100)
