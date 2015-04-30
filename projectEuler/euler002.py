''' 
	Find the sum of the even-valued terms in the Fibonacci sequence
	whose values do not exceed four million (n)
'''
def euler2(n):
	fib = list([1, 1])
	i = 2
	while fib[i-1] < n:
		fib.append( fib[i-1] + fib[i-2] )
		i += 1
	return sum([ i for i in fib if i % 2 == 0])

print euler2( 4000000 )