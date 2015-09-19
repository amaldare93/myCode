import Structures
import random

'''
	3.2 
	How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? 
	Push, pop and min should all operate in O(1) time.
'''
class node_min(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.nextmin = None

class stack_min(object):
	def __init__(self):
		self.top = None
		self.min = None

	def push(self, data):
		temp = node_min(data)
		temp.next = self.top
		self.top = temp

		if self.top.next == None:
			self.min = self.top

		elif data < self.min.data:
			self.top.nextmin = self.min
			self.min = self.top
		
	def pop(self):
		if self.top != None:
			if self.top == self.min:
				self.min = self.min.nextmin

			temp = self.top
			self.top = self.top.next
			return temp.data
		return None

	def peek(self):
		return self.top.data if self.top != None else None

	def minimum(self):
		return self.min.data if self.top != None else None 

'''
	3.3
	Implement a data structure SetOfStacks that is composed of several stacks and should create a new stack once the previous one exceeds capacity.
 	Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''
class Node(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SetOfStacks(object):
	def __init__(self, threshold=10):
		self.threshold = threshold
		self.top = None
		self.set = [Structures.stack()]
		Structures.stack.length = 0

	def push(self, data):
		if self.set[-1].length == self.threshold:
			self.set.append(Structures.stack())
		self.set[-1].push(data)
		self.set[-1].length += 1


	def pop(self, index=-1):
		if len(self.set) != 0:
			result = self.set[index].pop()
			self.set[index].length -= 1
			if self.set[index].top == None:
				self.set.pop()
			return result
		else:
			return None

	def peek(self):
		return self.set[-1].peek()

'''
	3.4
	Towers of Hanoi
'''
class Hanoi(object):
	def __init__(self, n):
		self.n = n
		self.A = Structures.stack()
		self.B = Structures.stack()
		self.C = Structures.stack()
		[self.A.push(n-i) for i in range(n)]
		self.B.push(None)
		self.C.push(None)

	def solve(self):
		pass

'''
	3.5
	Implement a queue made of two stacks
'''	
class stackQueue(object):
    def __init__(self):
        self.enstack = Structures.stack()
        self.destack = Structures.stack()
        
    def enqueue(self, data):
        # push data to enstack
        self.enstack.push( data )
        
    def dequeue(self):
        # make sure / put elements are in destack
        if self.destack.top == None:
            while self.enstack.top != None:
                self.destack.push( self.enstack.pop() )
        # pop from destack
        return self.destack.pop()
        
    def peek(self):
        # make sure / put elements are in destack
        if self.destack.top == None:
            while self.enstack.top != None:
                self.destack.push( self.enstack.pop() )
        # peek at destack
        return self.destack.peek()

'''
	3.6 
   	Write a program to sort a stack in ascending order (with biggest items on top). 
   	You may use at most one additional stack to hold items, 
   	but you may not copy the elements into any other data structure (such as an array).
    The stack supports the following operations: push, pop, peek, and isEmpty.
'''
def stackSort(stackA):
    stackB = Structures.stack()
    # sort stack
    while not stackA.isEmpty():
        buff = stackA.pop()
        while not stackB.isEmpty() and buff > stackB.peek():
            stackA.push( stackB.pop() )
        stackB.push( buff )
    
    # transfer reverse sorted stack B to stack A
    while not stackB.isEmpty():
        stackA.push ( stackB.pop() )
    
    # cleanup
    del stackB


'''
	3.7 
	An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis. 
	People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, 
	or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
'''
class Pound():
    def __init__(self):
        self.cats = Structures.queue()
        self.dogs = Structures.queue()
        self.id = 0
        
    def impound(self, species):
        if species == 'cat':
            self.cats.enqueue(self.id)
            self.id += 1
        elif species == 'dog':
            self.dogs.enqueue(self.id)
            self.id += 1
        else:
            print('What the hell is that thing?')
        
    def adopt(self, species=None):
        if species == None:
            if self.cats.peek() < self.dogs.peek():
                return self.cats.dequeue()
            else:
                return self.dogs.dequeue()
        elif species == 'cat':
            return self.cats.dequeue()
        elif species == 'dog':
            return self.dogs.dequeue()
        else:
            print("We don't have any of those")
            return None



