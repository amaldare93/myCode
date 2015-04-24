"""
	Find the sum of all the multiples of 3 or 5 below 1000 (n)
"""
def euler1( n ):
	return sum([ i for i in range(n) if i % 3 == 0 or i % 5 == 0])

print euler1( 1000 )