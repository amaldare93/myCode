'''
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import math
def euler012(n=500):
	# generate triangular numbers
	i = 1
	tri = 0
	while True:
		#triangle number to be tested
		tri = i + tri
		count = 2
		root = math.sqrt(tri)
		# if tri is not a perfect square, it has an odd # of divisors
		if root % 1 == 0:
			count += 1
			root -= 1

		for f in range(2, math.floor(root)+1):
			if tri % f == 0:
				count += 2

		if count > 500: return tri
		i += 1

print( euler012() )