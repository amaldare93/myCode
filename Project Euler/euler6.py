'''
	Find the difference between the sum of the squares of the first n=100 natural #s and the square of the sum.
'''

def euler6(n):
	return sum(range(1, n+1))**2 - sum([i**2 for i in range(1, n+1)])


print(euler6(100))