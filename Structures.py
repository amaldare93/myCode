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

class stack(object):
	def __init__(self):
		self.top = None

	def push(self, data):
		temp = node(data)
		temp.next = self.top
		self.top = temp

	def pop(self):
		if self.top != None:
			temp = self.top
			self.top = self.top.next
			return temp.data
		return None

	def peek(self):
		return self.top.data if self.top != None else None

	def isEmpty(self):
		return self.top == None

class queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    class node(object):
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None
               
    def isEmpty(self):
        return self.size == 0
        
    def size(self):
        return self.size

    def enqueue(self, data):
        n = self.node( data )
        self.size += 1
        if self.size != 1:
            n.next = self.tail
            self.tail.prev = n
            self.tail = n
        else:
            self.head = n
            self.tail = n
    
    def dequeue(self):
        if self.size > 1:
            self.size -= 1
            result = self.head.data
            self.head = self.head.prev
            del self.head.next
            self.head.next = None
            return result
        elif self.size == 1:
        	self.size -= 1
        	result = self.head.data
        	del self.head
        	return result
        else:
            return None
            
    def peek(self):
        return self.head.data if self.size != 0 else None

class binTree(object):
	def __init__(self):
		self.root = None

	class node(object):
		def __init__(self, data=None):
			self.data = data
			self.left = None
			self.right = None

		def __lt__(self, rh):
			return self.data < rh.data
		    
		def __gt__(self, rh):
			return self.data > rh.data

	def height(self, node=1):
		# initial call
		if node == 1:
			return self.height(self.root)
		# recursion
		elif node != None:
			return max(self.height(node.left), self.height(node.right)) + 1
		# base case
		elif node == None:
			return 0

	def printIn(self, node=1):
		# initial call
		if node == 1:
			node = self.root
		# recursion
		if node != None:
			self.printIn(node.left)
			print(node.data)
			self.printIn(node.right)

	def contains(self, data):
		current = self.root
		while current != None:
			if data == current.data:
				return True
			elif data < current.data:
				current = current.left
			else: # data > current.data
				current = current.right
		return False

		    
	
class binSearchTree(binTree):
    
	def insert(self, data):
	# create new node with data
		n = self.node(data)

		# search for sorted position
		if self.root != None:
			current = self.root
			while current != None:
				if n < current:
					if current.left != None:
						current = current.left
					else:
						current.left = n
						return
				elif n > current:
					if current.right != None:
						current = current.right
					else:
						current.right = n
						return
				else:
					# ignore duplicates
					return
		else:
			self.root = n

	def remove(self, data):
		current = self.root
		while current != None:
			if data == current.data:
				#delete node
				pass	
			elif data < current.data:
				current = current.left
			else: # data > current.data
				current = current.right
		return False		


