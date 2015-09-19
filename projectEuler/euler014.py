'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def euler014(limit=1000000):
	currentStart = 13
	longestLength = 1
	record = {}
	# loop from 13 to 1000000
	while currentStart < limit:
		n = currentStart
		currentLength = 1
		# create sequence (stops at 1)
		while n != 1:
			if n % 2 == 0:
				n = int(n / 2)
			else:
				n = 3 * n + 1

			# dynamic programming check
			if n in record.keys():
				print('using record for', n)
				currentLength += record[n]
				n = 1
			else:
				currentLength += 1
		record[currentStart] = currentLength

		#update longestLength
		if currentLength > longestLength:
			longestLength = currentLength
			largestStart = currentStart

		currentStart += 1
	return largestStart

print(euler014())
# 837799
