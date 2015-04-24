"""
	Find the largest prime factor of 600851475143 (n)
"""
import math
def euler3(n):

	def isPrime(num):
		if num < 2: return False
		for i in range(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False 
		return True
	
	i = int(math.sqrt(n))
	if i % 2 == 0: i -= 1
	while i > 1:
		if isPrime(i) and n % i == 0:
			return i
		else:
			i -= 2
	print 'There are no prime factors'
	return 0

print euler3(600851475143)