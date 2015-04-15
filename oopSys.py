from collections import deque
from queue import PriorityQueue
pid_counter = 0
print_count = 0

class System:
	def __init__(self, default=False):
		if default == True:
			self.n_disk = 1
			self.n_cylinder = 5
			self.n_CDRW = 1
			self.n_print = 1
			self.alpha = .5
			self.tao = 5
		else:
			print('Welcome to System Generation')
			self.n_disk = int(input('Disks: '))
			self.n_cylinder = int(input('# of Cylinders: '))
			self.n_CDRW = int(input('CD/RWs: '))
			self.n_print = int(input('Printers: '))
			self.alpha = float(input('History Parameter: '))
			self.tao = float(input('Initial Burst Estimate: '))

		self.cat = {}
		self.cat['r'] = Ready()
		self.cat['d'] = [Disk(i, self.n_cylinder) for i in range(1, self.n_disk+1)]
		self.cat['c'] = [CDRW(i) for i in range(1, self.n_CDRW+1)]
		self.cat['p'] = [Printer(i) for i in range(1, self.n_print+1)]

	def __getitem__(self, key):
		if len(key) > 1 and key[0] != 'r':
			return self.cat[ key[0] ][ int(key[1])-1 ]
		else:
			return self.cat[ key[0] ]

	def newProcess(self):
		self['r'].push( PCB() )

	def terminate(self):
		self['r'].pop()

	def interrupt(self, device): 
		self['r'].push( self[device].pop() )

	def snapshot(self, device):
		if device == 'r':
			scrollcheck()
			print('PID')
			self.cat['r'].snap()
		elif device == 'd' or device == 'c' or device == 'p':
			scrollcheck()
			print('{0:<4} {1:<16} {2:>10} {3:^1} {4:<10}'.format('PID', '| File name', '| Memstart', '| R/W', '| File Length'))
			[dev.snap() for dev in self.cat[device]]
		else:
			print('That is not a valid command. Try again.')

	def run(self):

		def switch(x):
			try:
				if x == 'exit': return
				elif x == 'A': self.newProcess()
				elif x == 't': self.terminate()
				# snapshot
				elif x[0] == 'S': self.snapshot(x[1:])
				# interrupt
				elif x.lower() != x and self[x.lower()] and not self[x.lower()].container.empty() and x != 'r':
					self.interrupt( x.lower() )
				# system call
				elif self[x] and x != 'r':
					self[x].systemCall( self['r'].pop() )

				else: print('That is not a valid command. Try again.')
				
			except IndexError:
				print('IndexError Exception: That is not a valid command. Try again.')
			except KeyError:
				print('KeyError Exception: That is not a valid command. Try again.')
			except ValueError:
				print('ValueError Exception: That is not a valid command. Try again.')
			except AttributeError:
				print('AttributeError Exception: That is not a valid command. Try again.')
		command = ''
		while command != 'exit':
			command = input('Enter Command: ')
			switch(command)

class PCB():
	def __init__(self, prio=0):
		global pid_counter
		self.pid = pid_counter
		self.priority = prio
		self.params = {'file_name': 'name', 'start_loc': 0, "r/w": 'w', 'file_length': 0}
		pid_counter += 1

	def __lt__(self, right):
		return (self.priority ,self.pid) < (right.priority ,right.pid)

class Componant:

	def push(self, pcb):
		self.container.put( pcb )

	def pop(self):
		return self.container.get() if not self.container.empty() else None

	def systemCall(self, pcb):
		if pcb != None:
			pcb.params['file_name'] = input('File Name: ')
			pcb.params['start_loc'] = input('Location: ')
			pcb.params['r/w'] = input('Read or Write? (r/w): ') if type(self) != Printer else 'w'
			pcb.params['file_length'] = input('File Length: ') if pcb.params['r/w'] == 'w' else ''
			self.push( pcb )


	def snap(self):
		global print_count
		print_count = 0

		scrollcheck()
		print('---' + self.key)
		for pcb in sorted(self.container.queue):
			scrollcheck()
			print('{0:<6} {1:<14} {2:>10} {3:^7} {4:>11}'.format(pcb.pid, pcb.params['file_name'], pcb.params['start_loc'], pcb.params['r/w'], pcb.params['file_length']))

class Ready(Componant):
	def __init__(self):
		self.container = PriorityQueue()
		self.key = 'r'

	def snap(self):
		global print_count
		print_count = 0

		scrollcheck()
		print('---' + self.key)
		scrollcheck()
		print(sorted(self.container.queue)[0].pid, '<-- in CPU') if not self.container.empty() else None
		for pcb in sorted(self.container.queue)[1:]:
			scrollcheck()
			print(pcb.pid)

class Disk(Componant):
	def __init__(self, id, cylinders):
		self.container = PriorityQueue()
		self.key = 'd' + str(id)
		self.cylinders = cylinders

class CDRW(Componant):
	def __init__(self, id):
		self.container = PriorityQueue()
		self.key = 'c' + str(id)

class Printer(Componant):
	def __init__(self, id):
		self.container = PriorityQueue()
		self.key = 'p' + str(id)

def scrollcheck():
	global print_count
	if print_count == 23:
		enter = input("press ENTER to see more ... ")
		print_count = 0
	print_count += 1


system = System(1)
system.run()











'''
class CPU():
	def __init__(self, id):
		self.key = 'cpu' # + str(id)
		self.container = deque('',1)

	def push(self, pcb):
		self.container.append(pcb)

	def pop(self):
		return self.container.pop()

	def snap(self):
		scrollcheck()
		print('---' + self.key)
		for pcb in self.container:
			scrollcheck()
			print(pcb.pid)
'''