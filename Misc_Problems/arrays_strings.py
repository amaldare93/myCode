from collections import Counter
'''
	1.1
	Implement an algorithm to determine if a string has all unique characters.
'''
def is_unique(string):
	count = Counter(string)
	if count.most_common(1)[0][1] > 1:
		return False
	return True

#print( is_unique("This is not unique") )

'''
	1.3
	Given two strings, write a method to decide if one is a permutation of the other.
'''
def isPermutation(string1, string2):
	count1 = Counter(string1)
	count2 = Counter(string2)
	if count1 == count2:
		return True
	else:
		return False

#print( isPermutation('doctorwho', 'torchwood') )

'''
	1.4
	Write a method to replace all spaces in a string with'%20'.
'''
def replace(string, this, that):
	parts = string.split(this)
	return that.join(parts)

#print( replace('Mr John Smith', ' ', '%20') )

'''
	1.5
	implement a method to perform basic string compression using the counts of repeated characters.
'''
def compress(string):
	count = 0
	comp_str = []
	for i in range(len(string)):
		count += 1
		if i+1 == len(string) or string[i+1] != string[i]:
			comp_str.append(string[i])
			comp_str.append(str(count))
			count = 0
	comp_str = ''.join(comp_str)

	if len(comp_str) < len(string):
		return comp_str
	else:
		return string 

#print( compress('aabcccccaaa') )

'''
	1.6
	Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
'''
def rotate_pic(pic):
	size = len(pic[0])-1
	newpic = [[0 for y in range(size+1)] for x in range(size+1)]
	for i in range(size+1):
		for j in range(size+1):
			newpic[j][size-i] = pic[i][j]
	return newpic

def print_matrix(matrix):
	for row in matrix:
		print(row)
	print('')

#pic = [[str(x) + str(y) for y in range(5)] for x in range(5)]
#print_matrix( pic )
#print_matrix( rotate_pic( pic ) )

'''
	1.7
	Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
'''
def zerows(matrix):
	m = len(matrix)
	n = len(matrix[0])
	rows = []
	cols = []
	print(m, n)
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				rows.append(i)
				cols.append(j)

	for i in range(m):
		for j in range(n):
			if i in rows:
				matrix[i][j] = 0
			elif j in cols:
				matrix[i][j] = 0

#matrix = [[x+1 for y in range(5)] for x in range(6)]
#matrix[2][3] = 0
#zerows( matrix )
#print_matrix( matrix )

'''
	1.8
	Assume you have a method isSubstring which checks if one word is a substring of another. 
	Given two strings, s i and s2, write code to check if s2 is a rotation of si using only one call to isSubstring
'''
def isSubstring(string1, string2):
	return True

def isRotation(string1, string2):
	string2 += string2
	if isSubstring(string1, string2):
		return True
	else:
		return False

#print( isRotation('anthony', 'honyant') )

'''
	Given a number n, find the largest number just smaller than n that can be formed using the same digits as n.
'''
def nextperm(n):
    
    def swap(string, ind1, ind2 ):
        temp = string[ind1]
        string[ind1] = string[ind2]
        string[ind2] = temp
    
    strng = list(str(n))
        # place next largest char at front
        # sort rest of string in descending order
    smallest = strng[-1]
    # scan each char in reverse
    for i in range(1,len(strng)+1):
        # when you find a char bigger than another
        if strng[-i] > smallest:
            # slice string there
            strngA = strng[:-i]
            strngB = strng[-i:]
            # place next largest (last char in string) char at front
            swap(strngB, 0, -1)
            # sort rest of string in descending order
            strngB2 = list(sorted(strngB[1:], reverse=True))
            return int(''.join(strngA + list(strngB[0]) + strngB2) )
        else:
            smallest = strng[-1]
    
    # if loop finishes and no char was bigger than a previous one,
    # then the string is completely sorted and can not be rearranged
    return n












