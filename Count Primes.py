"""
Count Primes (Leet Code)

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4

Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

def countPrimes(n):
    if (n < 2):
        return 0
    currNumber = 2
    primeArr = []
    while (currNumber != n):
        notPrime = True
        for i in primeArr:
            if (currNumber % i == 0): # if one of the iterations is true, then currNumber is not a prime
                notPrime = False
                break
        if (notPrime):
            primeArr.append(currNumber)
        currNumber += 1
    return len(primeArr)
