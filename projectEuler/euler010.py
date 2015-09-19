'''
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

	Find the sum of all the primes below n=two million.
'''

import math
def euler10(n=2000000):
	def isNextPrime(num):
		for prime in primes:
			if prime > math.sqrt(num):
				break
			if num % prime == 0:
				return False
		primes.append(num)
		return True

	primes = [2, 3]
	primeSum = 5
	i = 5
	while i < n:
		if isNextPrime(i): primeSum += i
		if isNextPrime(i+2): primeSum += i+2
		i += 6

	return primeSum

print(euler10())
# 142913828922
