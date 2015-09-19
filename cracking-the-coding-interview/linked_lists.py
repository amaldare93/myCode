import random
from collections import OrderedDict
import math
import Structures

palindrome = Structures.linked_list()
for i in range(10):
	palindrome.appendBack(i)
for i in range(10):
	palindrome.appendBack(9-i)

unsorted = Structures.linked_list()
for i in range(20):
	unsorted.appendBack(random.randint(0,10))

sorted = Structures.linked_list()
for i in range(10):
	sorted.appendBack(i)

'''
	2.1
	Write code to remove duplicates from an unsorted linked list.
'''
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

'''
	2.2
	Implement an algorithm to find the kth to last element of a singly linked list.
'''
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

'''
	2.3
	Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node
'''
def delete_node(node):
	current = node
	while current.next.next != None:
		current.data = current.next.data
		current = current.next
	current.data = current.next.data
	current.next = None



#delete_node( sorted.search(5) )
#sorted.printList()

'''
	2.4
	Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
'''
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

'''
	2.5
	You have two numbers represented by a linked list, where each node contains a single digit. 
	The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
	Write a function that adds the two numbers and returns the sum as a linked list.
'''
def list_add(left, right):

	l = left.head
	r = right.head
	carry = 0
	sum = Structures.linked_list()

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

def rev_add_double(left, right):
	l = left.tail
	r = right.tail
	carry = 0
	sum = Structures.linked_list()

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

def rev_add_single(left, right):
	# make even length 
	if left.size() > right.size():		
		for i in range(left.size() - right.size()):
			right.appendFront(0)
	elif right.size() > left.size():
		for i in range(right.size() - left.size()):
			left.appendFront(0)
	
	sum = Structures.linked_list()
	# recursive definition
	def add_digits(sum, l, r):
		# base case. ones place
		if l.next == None:
			psum = l.data + r.data
			sum.appendFront(psum % 10)
			return math.floor(psum / 10)

		psum = l.data + r.data + add_digits(sum, l.next, r.next)
		sum.appendFront(psum % 10)
		return math.floor(psum / 10)

	sum.appendFront(add_digits(sum, left.head, right.head))

	# cleanup
	while sum.head.data == 0:
		sum.delete(sum.head)
	return sum

#A = Structures.linked_list()
#A.appendBack(6)
#A.appendBack(1)
#A.appendBack(7)

#B = Structures.linked_list()
#B.appendBack(1)
#B.appendBack(0)
#B.appendBack(0)
#B.appendBack(0)
#list_add(A, B).printList()
#rev_add_double(A, B).printList()
#rev_add_single(A, B).printList()

'''
	2.6
	Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.
'''
def isloop(list):
	fastRunner = list.head.next.next
	slowRunner = list.head.next
	headRunner = list.head


	while fastRunner != slowRunner and fastRunner != None and fastRunner.next != None:
		fastRunner = fastRunner.next.next
		slowRunner = slowRunner.next

	if fastRunner == None or fastRunner.next == None:
		return None

	while slowRunner != headRunner:
		slowRunner = slowRunner.next
		headRunner = headRunner.next

	return slowRunner

#sorted.tail.next = sorted.head.next
#print( isloop(sorted) )

'''
	2.7 
	Implement a function to check if a linked list is a palindrome
'''
def isPalindromeD(list):
    front = list.head
    back = list.tail
    while front != back and front.prev != back:
        if front.data == back.data:
            front = front.next
            back = back.prev
        else:
            return False
    return True

def isPalindromeS(list):
    current = list.head
    result = True
    backwards = Structures.linked_list()
    
    while current != None:
        backwards.appendFront(current.data)
        current = current.next
        
    current = list.head
    backptr = backwards.head
    while current != None:
        if current.data == backptr.data:
            current = current.next
            backptr = backptr.next
        else:
            result = False
            break

    # memory management
    while backwards.head != None:
        backwards.delete(backwards.head)
    return result






