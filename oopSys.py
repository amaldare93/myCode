from collections import deque
from queue import PriorityQueue
print_count = 0


class System:
	def __init__(self, default=False):
		self.pid_counter = 0
		# QUICK GENERATION (no inputs )
		if default == True:
			self.n_disk = 1
			Disk.cylinders = 5
			self.n_CDRW = 1
			self.n_print = 1
			PCB.alpha = 0.5
			PCB.tao = 2.0

		# DEFAULT GENERATION (input parameters)
		else:
			print('Welcome to System Generation')
			def_except = 'Error: Value must be an integer > 0'

			self.n_disk = int(getInput('Disks: ', lambda x: int(x) > 0, def_except))
			Disk.cylinders = int(getInput('# of Cylinders: ', lambda x: int(x) > 0, def_except))
			self.n_CDRW = int(getInput('CDRWs: ', lambda x: int(x) > 0, def_except))
			self.n_print = int(getInput('Printers: ', lambda x : int(x) > 0, def_except))
			PCB.alpha = float(getInput('History Parameter: ', lambda x: 0 <= float(x) <= 1, 'Error: Value must be between 0 and 1'))
			PCB.tao = float(getInput('Initial burst estimate (ms): ', lambda x: float(x) > 0))

		self.numComplete = 0
		self.totalComplete = 0
		self.avgComplete = 0
		# Create queue objects
		self.cat = {}
		self.cat['r'] = Ready()
		self.cat['d'] = [Disk(i) for i in range(1, self.n_disk+1)]
		self.cat['c'] = [CDRW(i) for i in range(1, self.n_CDRW+1)]
		self.cat['p'] = [Printer(i) for i in range(1, self.n_print+1)]

	def __getitem__(self, key):
		# override x[index] operator
		if len(key) > 1 and key[0] != 'r':
			return self.cat[ key[0] ][ int(key[1])-1 ]
		else:
			return self.cat[ key[0] ]

	def newProcess(self):
		self['r'].push( PCB(self.pid_counter) )
		self.pid_counter += 1

	def terminate(self):
		temp = self['r'].pop()
		self.numComplete += 1
		self.totalComplete += temp.totalCPU
		self.avgComplete = self.totalComplete / self.numComplete
		print('Process #{0.pid} has been terminated\n\tTotal CPU time: {0.totalCPU}\n\tAverage CPU Burst: {0.avgBurst}'.format(temp))

	def interrupt(self, device):
		# stop current CPU process
		if not self['r'].container.empty():
			temp = self['r'].pop()	
			temp.intUpdate()
			self['r'].push( temp )

		if device[0] == 'd':
			temp = self[device].pop()
			temp.priority = temp.tao
			self[device].RWhead = temp.params['cylinder']
			self['r'].push( temp )
			self[device].WSTF()
		else:
			self['r'].push( self[device].pop() )

	def snapshot(self, device):
		scrollcheck()
		print('Average Total CPU Time of Completed Processes: ', self.totalComplete)
		if device == 'r':
			scrollcheck()
			print('{0:3} {3:5} {1:10} {2:10}'.format('PID', '| Total CPU', '| Avg Burst', '| Pri'))
			self.cat['r'].snap()
		elif device == 'd':
			scrollcheck()
			print('{0:3} {1:6} {2:11} {3:9} {4:5} {5:13} {6:11} {7:11}'.format('PID', '| Cyln', '| File Name', '| Mem Loc', '| R/W', '| File Length', '| Total CPU', '| Avg Burst'))
			[dev.snap() for dev in self.cat[device]]
		elif device == 'c' or device == 'p':
			scrollcheck()
			print('{0:3} {1:11} {2:9} {3:5} {4:13} {5:11} {6:11}'.format('PID', '| File Name', '| Mem Loc', '| R/W', '| File Length', '| Total CPU', '| Avg Burst'))
			[dev.snap() for dev in self.cat[device]]
		else:
			print('That is not a valid command. Try again.')

	def run(self):

		x = ''
		while x != 'exit':
			x = input('Enter Command: ')
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
				elif self[x] and x[0] != 'r':
					self[x].systemCall( self['r'].pop() )
				else: 
					raise#print('That is not a valid command. Try again.')
			except:
				raise#print('That is not a valid command. Try again.')

class PCB():
	def __init__(self, pid):
		self.pid = pid
		self.priority = self.tao
		self.totalCPU = 0
		self.numBursts = 0
		self.avgBurst = 0
		self.params = {'file_name': 'name', 'start_loc': 0, "r/w": 'w', 'file_length': 0}

	def __lt__(self, right):
		return (self.priority, self.pid) < (right.priority, right.pid)

	def sysUpdate(self):		
		t_prev = int(getInput('How long (ms) did current process use CPU?: ', lambda x : int(x) >= 0))

		# STF priority
		self.tao = (self.alpha * self.tao) + ((1 - self.alpha) * t_prev)
		self.priority = self.tao

		# proccess stats
		self.totalCPU += t_prev
		self.numBursts += 1
		self.avgBurst = self.totalCPU / self.numBursts

	def intUpdate(self):		
		t_prev = int(getInput('How long (ms) did current process use CPU?: ', lambda x : int(x) >= 0))

		# STF priority
		#self.tao = (self.alpha * self.tao) + ((1 - self.alpha) * t_prev)
		self.priority = self.tao - t_prev

		# proccess stats
		self.totalCPU += t_prev
		#self.numBursts += 1
		#self.avgBurst = self.totalCPU / self.numBursts
		
class Componant:

	def push(self, pcb):
		self.container.put( pcb )

	def pop(self):
		return self.container.get() if not self.container.empty() else None

	def isEmpty(self):
		return self.container.empty()

	def systemCall(self, pcb):
		if pcb != None:
			pcb.sysUpdate()
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
			print('{0:>3} {1:>11} {2:>9} {3:>5} {4:>13} {5:>11} {6:>11}'.format(pcb.pid, pcb.params['file_name'], pcb.params['start_loc'], pcb.params['r/w'], pcb.params['file_length'], pcb.totalCPU, pcb.avgBurst))

class Ready(Componant):
	def __init__(self):
		self.container = PriorityQueue()
		self.key = 'r'

	def snap(self):
		global print_count
		print_count = 0

		scrollcheck()
		print('---' + self.key)

		pcb = sorted(self.container.queue)[0]
		scrollcheck()
		print('{0:>3} {3:5} {1:>11} {2:>11}'.format(pcb.pid, pcb.totalCPU, pcb.avgBurst, pcb.priority), '<-- in CPU') if not self.container.empty() else None
		for pcb in sorted(self.container.queue)[1:]:
			scrollcheck()
			print('{0:>3} {3:5} {1:>11} {2:>11}'.format(pcb.pid, pcb.totalCPU, pcb.avgBurst, pcb.priority))

class Disk(Componant):
	def __init__(self, id):
		self.container = PriorityQueue()
		self.key = 'd' + str(id)
		self.RWhead = self.cylinders / 2
		self.M = 15

	def systemCall(self, pcb):
		if pcb != None:
			pcb.sysUpdate()
			pcb.params['cylinder'] = int(getInput('Cylinder #: ', lambda x: 0 <= int(x) <= self.cylinders, 'Cylinder does not exist'))
			pcb.params['file_name'] = input('File Name: ')
			pcb.params['start_loc'] = input('Location: ')
			pcb.params['r/w'] = input('Read or Write? (r/w): ')
			pcb.params['file_length'] = input('File Length: ') if pcb.params['r/w'] == 'w' else ''
			pcb.params['elapsed'] = 0
			self.push( pcb )
			self.WSTF()

	def snap(self):
		global print_count
		print_count = 0

		scrollcheck()
		print('---' + self.key)

		scrollcheck()
		for pcb in sorted(self.container.queue):
			scrollcheck()
			print('{0:>3} {1:>6} {2:>11} {3:>9} {4:>5} {5:>13} {6:>11} {7:>11}'.format(pcb.pid, pcb.params['cylinder'], pcb.params['file_name'], pcb.params['start_loc'], pcb.params['r/w'], pcb.params['file_length'], pcb.totalCPU, pcb.avgBurst))

	def WSTF(self):
		buff = []
		while not self.isEmpty():
			buff.append(self.pop())
		for pcb in buff:
			pcb.params['elapsed'] += 1
			pcb.priority = abs(self.RWhead - pcb.params['cylinder'])*((self.M - pcb.params['elapsed'])/self.M)
			self.push(pcb)	
		
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

def getInput(prompt, condition, exception='That is not a valid input'):
	while(True):
		try:
			var = input(prompt)
			if condition(var):
				return var
			else: raise
		except KeyboardInterrupt: raise
		except: raise#print(exception)

system = System(1)
system.run()
