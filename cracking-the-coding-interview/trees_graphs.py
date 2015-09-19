import Structures
import random


randTree = Structures.binSearchTree()
[randTree.insert(random.randint(1, 100)) for _ in range(100)]

balTree = Structures.binSearchTree()
balTree.insert(10)
balTree.insert(5)
balTree.insert(1)
balTree.insert(7)
balTree.insert(11)
balTree.insert(13)
balTree.insert(12)

'''
	4.1 
	Implement a function to check if a binary tree is balanced. 
	For the purposes of this question, a balanced tree is defined to be a tree such that
	the heights of the two subtrees of any node never differ by more than one.
'''
def isBalanced(tree):
	# if tree is empty, still return True
	if tree.root == None:
		return True

	# recursive definition
	def isBal(node):
		if node != None:
			lh = isBal(node.left)
			rh = isBal(node.right)
			return max(lh, rh) + 1 if abs(lh - rh) < 2 else False

		elif node == None:
			return 0

	# initial call
	return True if isBal(tree.root) else False

'''
	4.2 
	Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''
graphDirect = {
	'A': ['B', 'C'],
	'B': ['C', 'D'],
	'C': ['D'], 
	'D': ['C'],
	'E': ['F'],
	'F': ['C']
}

def isPath(graph, start, goal):
	if start not in graph or goal not in graph: return False
	if start == goal: return True

	frontier = Structures.queue()
	explored = []

	# first step
	if goal in graph[start]: return True
	[frontier.enqueue(next) for next in graph[start]]
	explored.append(start)

	# rest of steps
	while not frontier.isEmpty():
		current = frontier.dequeue()
		if current not in explored:
			if goal in graph[current]: return True
			[frontier.enqueue(next) for next in graph[current]]
			explored.append(current)
	return False



'''
	4.3 
	Given a sorted (increasing order) array with unique integer elements, 
	write an algorithm to create a binary search tree with minimal height.
'''
def makeTree(arr, node=1, tree=None):
	# initial call
	if node == 1:
		tree = Structures.binSearchTree()
		tree.root = tree.node()
		tree.root.data = makeTree( arr, tree.root, tree )
		return tree
	# recursive calls
	else:
		if len(arr) > 3:
			node.left = tree.node()
			node.right = tree.node()
			node.left.data = makeTree( arr[:int(len(arr)/2)], node.left, tree ) 
			node.right.data = makeTree( arr[int(len(arr)/2)+1:], node.right, tree )
			return arr[int(len(arr)/2)]
		# base cases
		elif len(arr) == 3:
			node.left = tree.node()
			node.right = tree.node()
			node.left.data = arr[0]
			node.right.data = arr[2]
			return arr[1]
		elif len(arr) == 2:
			node.right = tree.node()
			node.right.data = arr[1]
			return arr[0]
		else:
			return arr[0]

#array = [i for i in range(50)]
#makeTree(array).printIn()


'''
	4.4 
	Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
	(e.g., if you have a tree with depth D, you'll have D linked lists).
'''
def listify(tree):
	lists = []
	frontier = Structures.queue()
	buff = Structures.queue()

	frontier.enqueue(tree.root)
	
	while not frontier.isEmpty():
		lists.append(Structures.linked_list())
		while not frontier.isEmpty():
			buff.enqueue( frontier.dequeue() )
		while not buff.isEmpty():
			node = buff.dequeue()
			if node.left != None: frontier.enqueue( node.left )
			if node.right != None: frontier.enqueue( node.right )
			lists[-1].appendBack(node.data)

	return lists
	
#[list.printList() for list in randTrees]

'''
	4.5 
	Implement a function to check if a binary tree is a binary search tree.
'''
def isBST(tree):
	pass


'''
	4.6 
	Write an algorithm to find the'next'node (i.e., in-order successor) of a given node in a binary search tree. 
	You may assume that each node has a link to its parent.
'''



'''
	4.7 
	Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
	Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
'''
def LCA(tree, A, B):
	def searchPath(node, current, path, tree=tree,):
		if current != None:
			print(node.data, current.data, path)
			if current == node:
				return path
			else:
				path.append('l')
				searchPath(node, current.left, path)
				path[-1] = 'r'
				searchPath(node, current.right, path)



	pathA = []
	pathB = []
	pathA = searchPath(A, tree.root, [])
	pathB = searchPath(B, tree.root, [])

	print(pathA, pathB)

#LCA(balTree, balTree.root.left.left, balTree.root.left.right)

'''
	4.8 
	You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes.
	Create an algorithm to decide if T2 is a subtree of T1.
	A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. 
	That is, if you cut off the tree at node n, the two trees would be identical.
'''



'''
	4.9 
	You are given a binary tree in which each node contains a value. 
	Design an algorithm to print all paths which sum to a given value. 
	The path does not need to start or end at the root or a leaf.
'''


'''
	17.13
	Implement a method to convert a binary search tree into a doubly linked list. 
	The values should be kept in order and the operation should be performed in place (that is,on the original data structure).
'''
def listify( node, direction=None):
	# in order traversal
	if node.left == None and node.right == None:
		return node
	elif node.left == None:
		rightList = listify( node.right )
		print(node.data, rightList)
		rightList.left = node
		node.right = rightList
		
	elif node.right == None:
		leftList = listify( node.left )
		print(node.data, leftList)
		leftList.right = node
		node.left = leftList
		
	else:
		leftList = listify( node.left, 'l' )
		print(node.data, leftList)
		leftList.right = node
		node.left = leftList
		
		rightList = listify( node.right, 'r' )
		print(node.data, rightList)
		rightList.left = node
		node.right = rightList

		if direction == 'l':
			return rightList
		elif direction == 'r':
			return leftList
		
listify(balTree.root)







