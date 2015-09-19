'''
	What is the smallest positive number that is divisible by all of the numbers from 1 to 20 ?
'''
def euler5(n):

	num = 20
	i = 11
	while i < 21:
		if num % i != 0:
			i = 11
			num += 20
		else:
			i += 1
	return num

print(euler5(20))
# 232792560
