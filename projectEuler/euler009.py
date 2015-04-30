'''
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
	
	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.
'''

def euler9():
	a = 1
	b = 2
	c = 3
	triples = []
	while a < 1000:
		while b < 1000 and c > b:
			c = 1000 - a - b
			if a**2 + b**2 == c**2:
				return a * b * c
			b += 1
		a += 1
		b = a+1	

print( euler9() )
# 31875000