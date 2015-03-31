import random
from collections import OrderedDict
import math

class node(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.prev = None

class linked_list(object):
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def appendFront(self, thing):
		# create node for data
		if type(thing) != type(node()):
			thing = node(thing)

		# if list is empty
		if not self.head:
			self.head = thing
			self.tail = thing

		else:
			thing.next = self.head
			self.head.prev = thing
			self.head = thing

	def appendBack(self, thing):
		# create node for data
		if type(thing) != type(node()):
			thing = node(thing)

		# if list is empty
		if not self.head:
			self.head = thing
			self.tail = thing

		else:
			self.tail.next = thing
			thing.prev = self.tail
			self.tail = thing

	def insertAfter(self, node, newThing):
		# create node for data
		if type(thing) != type(node()):
			thing = node(thing)
			
		# if adding to end
		if node == self.tail:
			node.next = newThing
			newThing.prev = node
			self.tail = newThing

		else:
			newThing.next = node.next
			newThing.prev = node
			node.next.prev = newThing
			node.next = newThing

	def delete(self, thing):
		# if list is empty
		if self.head == None:
			return

		# if thing data, find node
		if type(thing) != type(node()):
			thing = self.search(thing)

		# if thing is only node in list
		if self.head == self.tail == thing:
			self.head = None
			self.tail = None
			del thing
			return

		# if thing is head
		if thing == self.head:
			self.head = thing.next
			self.head.prev = None
			del thing
			return

		# if thing is tail
		if thing == self.tail:
			self.tail = thing.prev
			self.tail.next = None
			del thing
			return

		# else
		thing.prev.next = thing.next
		thing.next.prev = thing.prev
		del thing
		return

	def printList(self):
		current = self.head
		buff = []
		while(current != None):
			buff.append(current.data)
			current = current.next
		print(buff)

	def search(self, data):
	 	current = self.head
	 	while(current != None):
	 		if(current.data == data):
	 			return current
	 		else:
	 			current = current.next
	 	return False

	def size(self):
		if self.head == None:
			return 0
		current = self.head
		count = 0
		while(current != None):
			count += 1
			current = current.next
		return count



unsorted = linked_list()
for i in range(20):
	unsorted.appendBack(random.randint(0,10))

sorted = linked_list()
for i in range(10):
	sorted.appendBack(10-i)

# 2.1
#	Write code to remove duplicates from an unsorted linked list.
def remove_duplicates(list):
	current = list.head
	count = OrderedDict()

	while current != None:
		count[current.data] = current.data
		list.delete(current)
		current = current.next

	for data in count:
		list.appendBack(data)


#unsorted.printList()
#remove_duplicates(unsorted)
#unsorted.printList()

# 2.2
#	Implement an algorithm to find the kth to last element of a singly linked list.
def kth_last(k, list):
	last = list.head
	klast = list.head
	for i in range(k):
		if last != None:
			last = last.next
	while last != None:
		klast = klast.next
		last = last.next
	return klast.data

#sorted.printList()
#print( 'kth last element is: ', kth_last(5, sorted) )

# 2.3
#	Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node
def delete_node(node):
	current = node
	while current.next.next != None:
		current.data = current.next.data
		current = current.next
	current.data = current.next.data
	current.next = None



#delete_node( sorted.search(5) )
#sorted.printList()

# 2.4
#	Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
def partition(list, val):
	current = list.head
	end = list.tail

	while current != end:
		if current.data >= val:
			list.appendBack( current.data )
			list.delete(current)
		current = current.next

#partition(unsorted, 7)
#unsorted.printList()

# 2.5
#	You have two numbers represented by a linked list, where each node contains a single digit. 
#		The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
#		Write a function that adds the two numbers and returns the sum as a linked list.

A = linked_list()
A.appendBack(1)
A.appendBack(0)
A.appendBack(0)

B = linked_list()
B.appendBack(2)
B.appendBack(9)
B.appendBack(5)

def list_add(left, right):

	l = left.head
	r = right.head
	carry = 0
	sum = linked_list()

	while l != None or r != None:
		if l == None:
			psum = r.data + carry
			r = r.next
		elif r == None:
			psum = l.data + carry
			l = l.next
		else:
			psum = l.data + r.data + carry
			l = l.next
			r = r.next

		sum.appendBack(psum % 10)
		carry = math.floor(psum / 10)

	if carry != 0:
		sum.appendBack(carry)
	return sum

#list_add(A, B).printList()

def rev_add_double(left, right):
	l = left.tail
	r = right.tail
	carry = 0
	sum = linked_list()

	while l != None or r != None:
		if l == None:
			psum = r.data + carry
			r = r.prev
		elif r == None:
			psum = l.data + carry
			l = l.prev
		else:
			psum = l.data + r.data + carry
			l = l.prev
			r = r.prev

		sum.appendFront(psum % 10)
		carry = math.floor(psum / 10)

	if carry != 0:
		sum.appendFront(carry)
	return sum

#rev_add_double(A, B).printList()

def rev_add_single(left, right):
	for i in range(math.abs(left.size() - right.size())):
		print(i)


rev_add_double(A, B)
# 6 -> 1 -> 7
# 2 -> 9 -> 5
#-------------
#           









