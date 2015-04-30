'''
	Find the largest palindrome made from the product of two 3-digit numbers
'''
def euler4():

	def isPalindrome( x ):
		return str(x) == str(x)[::-1]
	products = []
	[[products.append(i * j) for i in range(99, 1000)] for j in range(99, 1000)]
	
	for prod in sorted(products, reverse=True):
		if isPalindrome(prod):
			return prod
	return False

print(euler4())