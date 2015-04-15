import fileinput

# append list of entire row of input to one position of triangle list
def process(line):
	triangle.append([int(i) for i in line.split()])

# return value of element at position (i, j) in the triangle
def tri(index):
	return triangle[index[0]][index[1]]

# return index of next node, iteration through each node in triangle
def next(index):
	if index[1] == index[0]:
		return(index[0]+1, 0)
	else:
		return (index[0], index[1]+1)

# return position of max parent of node
def max_parent(i, j):
	if j == 0:
		return (i-1, 0)
	elif j == i:
		return (i-1, j-1)
	else:
		return max((i-1, j-1), (i-1, j), key=lambda k:tri(k))

# return maximum total from the top to index
def max_sum_to(index):
	if index == (0, 0):
		return tri(index)
	else:
		return tri(index) + tri(max_parent(index[0], index[1]))

# process text file into 2dimensional array/list
rows = 0
triangle = []
for line in fileinput.input('triangle.txt'):
	process(line)
	rows += 1

# starting from first position
# for each number in triangle,
# 		replace value with max_sum_to that number
# return largest sum at end

index = (0, 0)
max_count = 0
while index != (rows,0):
	triangle[index[0]][index[1]] = max_sum_to(index)
	if triangle[index[0]][index[1]] > max_count :
		max_count = triangle[index[0]][index[1]]
	index = next(index)

print('max count =', max_count)











