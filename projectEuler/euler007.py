'''
	What is the n=10001th prime number?
'''

import math

def euler7(n):
	def isPrime(num):
		if num == 2 or num == 3:
			return True
		elif num < 2 or num % 2 == 0 or num % 3 == 0:
			return False
		else:
			i = 5
			root = math.sqrt(num)
			while i <= root:
				if num % i == 0: return False
				elif num % (i+2) == 0: return False
				i += 6
			return True

	primeCount = 2
	i = 5
	while True:
		if isPrime(i):
			primeCount += 1
			if primeCount == n: return i
		if isPrime(i+2):
			primeCount += 1
			if primeCount == n: return i+2
		i += 6
	return False

print(euler7(1000))
# 7919
