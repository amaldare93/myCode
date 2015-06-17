import queue, math, collections
print_count = 0

class System:
	# System Generation
	def __init__(self, flag=False):
		self.pid_counter = 0

		# Quick Gen (no user input)
		if(flag):
			self.n_disk      = 1
			self.n_cylinders = [100]
			Disk.M           = 5
			self.n_CDRW      = 1
			self.n_print     = 1
			PCB.alpha        = 0.5
			PCB.tao          = 1
			Memory.memTotal  = 2048
			PCB.maxSize      = 2048
			Memory.pageSize  = 128

		# Normal Generation
		else:
			print('Welcome to System Generation')
			def_except   = 'Error: Value must be an integer > 0'
			defCondition = lambda x: int(x) > 0

			self.n_disk      = int(getInput('Disks: ', defCondition, def_except))
			self.n_cylinders = [int(getInput('Cylinders for d{}: '.format(n+1), defCondition, def_except)) for n in range(self.n_disk)]
			Disk.M           = int(getInput('Max time for disk starvation: ', defCondition, def_except))
			self.n_CDRW      = int(getInput('CDRWs: ', defCondition, def_except))
			self.n_print     = int(getInput('Printers: ', defCondition, def_except))
			PCB.alpha        = float(getInput('History Parameter: ', lambda x: 0 <= float(x) <= 1, 'Error: Value must be between 0 and 1'))
			PCB.tao          = float(getInput('Initial burst estimate (ms): ', lambda x: float(x) > 0))
			while True:
				Memory.memTotal = int(getInput('Total System Memory (words): ', defCondition, def_except ))
				PCB.maxSize     = int(getInput('Max process size (words): ', lambda x: int(x) <= Memory.memTotal , 'Error: Max process size must be <= Total system memory ({})'.format(Memory.memTotal)))
				Memory.pageSize = int(getInput('Page size (words):', lambda x: math.log2(int(x)) % 1 == 0, 'Error: Page size must be a power of 2' ))
				if Memory.memTotal % Memory.pageSize == 0:
					break
				else:
					print( 'Error: page size must evenly divide memory size of ({})'.format(Memory.memTotal) )

		# Initialize syatem stats
		self.numComplete   = 0
		self.totalComplete = 0
		self.avgComplete   = 0

		# Create queue objects
		self.cat = {}
		self.cat['m'] = Memory()
		self.cat['r'] = Ready()
		self.cat['d'] = [Disk(i+1, self.n_cylinders[i]) for i in range(self.n_disk)]
		self.cat['c'] = [CDRW(i) for i in range(1, self.n_CDRW+1)]
		self.cat['p'] = [Printer(i) for i in range(1, self.n_print+1)]

	# Index operator for choosing queues
	def __getitem__(self, key):
		# override x[index] operator
		if len(key) > 1 and key[0] != 'r':
			return self.cat[ key[0] ][ int(key[1])-1 ]
		else:
			return self.cat[ key[0] ]

	# creates new process
	def newProcess(self):
		# stop current process
		if not self['r'].isEmpty():
			temp = self['r'].pop()
			temp.intUpdate()
			self['r'].push( temp )

		# create new PCB
		size = int(getInput('Size of new process (words): ', lambda x: int(x) > 0))

		# send to memory unit
		if size <= PCB.maxSize:
			# create PCB
			pcb = PCB(self.pid_counter, size)
			self.pid_counter += 1

			# if pcb went to memory (not job pool)
			if self.cat['m'].addProcess( pcb ):
				# add to ready queue
				self['r'].push( pcb )
		else:
			print('Process rejected: too large')

	# terminates process currently in CPU
	def terminate(self):
		mem = self.cat['m']
		temp = self['r'].pop()
		# update system stats
		temp.sysUpdate()
		self.numComplete += 1
		self.totalComplete += temp.totalCPU
		self.avgComplete = self.totalComplete / self.numComplete
		print('Process #{0.pid} has been terminated\n\tTotal CPU time: {0.totalCPU}\n\tAverage CPU Burst: {0.avgBurst}'.format(temp))

		# free memory
		mem.removeFromMem(temp)
		# load from job pool
		[self.cat['r'].push(pcb) for pcb in mem.popFromPool()]

	# process coming in to ready queue from a device queue
	def interrupt(self, device):
		# stop current CPU process
		if not self['r'].container.empty():
			temp = self['r'].pop()
			temp.intUpdate()
			self['r'].push( temp )

		# if coming from disk, set RWhead and do WSTF
		if device[0] == 'd':
			temp = self[device].pop()
			temp.priority = temp.tao
			self[device].RWhead = temp.params['cylinder']
			self['r'].push( temp )
			self[device].WSTF()
		# else just send back to ready queue
		else:
			self['r'].push( self[device].pop() )

	# prints information to screen
	def snapshot(self, device):
		global print_count
		print_count = 0

		printScroll('Average Total CPU Time of Completed Processes: {}'.format( self.totalComplete ))
		# READY QUEUE
		if device == 'r':
			printScroll('PID | Total CPU | Avg Burst | Pri | Page Table   ')
			self.cat['r'].snap()
		# DISK / CDRW / PRINTER QUEUES
		elif device in 'cpd':
			printScroll('PID | File Name | Mem Loc | R/W | Length | Total CPU | Avg Burst | Page Table   ')
			[dev.snap() for dev in self.cat[device]]
		# MEMORY
		elif device == 'm':
			mem = self.cat['m']
			printScroll('Memory Available: {}'.format(mem.memAvail))
			printScroll('Frames Available: {}'.format(list(mem.freeFrameList)))
			printScroll('|  Frame Table  ||    Job Pool   |')
			printScroll('| frame |  pid  ||  pid  |  size |')
			printScroll(' ________________________________')
			for i in range(len(mem.frameTable)):
				printScroll('|{0:6} |{1:6} ||{2:6} |{3:6} |'.format(i,
																	mem.frameTable[i] if mem.frameTable[i] != None else '',
																	mem.jobPool[-i-1].pid if len(mem.jobPool) > i else '',
																	mem.jobPool[-i-1].size if len(mem.jobPool) > i else ''))
			if len(mem.jobPool) > len(mem.frameTable):
				for i in range(len(mem.frameTable, len(mem.jobPool))):
					printScroll('|{0:6} |{1:6} ||{2:6} |{3:6} |'.format('', '', mem.jobPool[i], mem.jobPool[i].size))
		else:
			print('That is not a valid command. Try again.')

	# Main Loop of system (takes and executes user commands)
	def run(self):

		''''
		__System Calls__
		t  = terminate process in CPU
		dx = send current process to Disk x
		px = send current process to Printer x
		cx = send current process to CDRW x

		__Interrupts__
		A  = create new process
		Dx = finish I/O on Disk x
		Px = finish I/O on Printer x
		Cx = finish I/O on CDRW x

		__Snapshots__
		Sr = show ready queue + CPU
		Sm = show frame table + job pool
		Sd = show disk queues
		Sp = show print queues
		Sc = show CDRW queues

		exit = exit program
		'''

		x = ''
		while x != 'exit':
			x = input('Enter Command: ')
			try:
				if x == 'exit': return
				elif x == 'A': self.newProcess()
				elif x == 't': self.terminate()
				elif x[0] == 'S': self.snapshot(x[1:])
				elif x.lower() != x and self[x.lower()] and not self[x.lower()].container.empty() and x != 'r':
					self.interrupt( x.lower() )
				elif self[x] and x[0] != 'r':
					self[x].systemCall( self['r'].pop() )
			except:
				print('That is not a valid command. Try again.')
# Process Control Block
class PCB():
	def __init__(self, pid, size):
		self.pid       = pid
		self.size      = size
		self.priority  = self.tao
		self.totalCPU  = 0
		self.numBursts = 0
		self.avgBurst  = 0
		self.params    = {'file_name': 'name', 'start_loc': 0, "r/w": 'w', 'file_length': 0}
		self.pageTable = []

	def __lt__(self, right):
		return (self.priority, self.pid) < (right.priority, right.pid)

	def sysUpdate(self):
		t_prev = int(getInput('How long (ms) did current process use CPU?: ', lambda x : int(x) >= 0))

		# STF priority
		self.tao = (self.alpha * self.tao) + ((1 - self.alpha) * t_prev)
		self.priority = self.tao

		# proccess stats
		self.totalCPU  += t_prev
		self.numBursts += 1
		self.avgBurst  = self.totalCPU / self.numBursts

	def intUpdate(self):
		t_prev = int(getInput('How long (ms) did current process use CPU?: ', lambda x : int(x) >= 0))

		# STF priority
		self.priority = self.priority - t_prev

		# proccess stats
		self.totalCPU += t_prev

# Parent Class to all queues
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
			pcb.params['file_name']   = input('File Name: ')[:9]
			pcb.params['start_loc']   = input('Location: ')
			pcb.params['r/w']         = getInput('Read or Write? (r/w): ', lambda x : x in ('r', 'w', 'R', 'W'), 'Must enter "r" or "w"') if type(self) != Printer else 'w'
			pcb.params['file_length'] = input('File Length: ') if pcb.params['r/w'] == 'w' else ''
			self.push( pcb )

	def snap(self):
		printScroll('---' + self.key)
		for pcb in sorted(self.container.queue):
			printScroll('{0:>3} {1:>11} {2:>9} {3:>5} {4:>8} {5:>11} {6:>11.2f}'.format(pcb.pid, pcb.params['file_name'], pcb.params['start_loc'], pcb.params['r/w'], pcb.params['file_length'], pcb.totalCPU, pcb.avgBurst))

class Ready(Componant):
	def __init__(self):
		self.container = queue.PriorityQueue()
		self.key = 'r'

	def snap(self):
		comma = ' '
		printScroll('---' + self.key)
		if not self.container.empty():
			pcb = sorted(self.container.queue)[0]
			printScroll('{0:3} {1:11} {2:11.2f} {3:5.1f} {4:15}  {5}'.format(pcb.pid, pcb.totalCPU, pcb.avgBurst, pcb.priority, '  ['+comma.join([str(x) for x in pcb.pageTable])+']', '<' ))
			for pcb in sorted(self.container.queue)[1:]:
				printScroll('{0:3} {1:11} {2:11.2f} {3:5.1f} {4:15}'.format(pcb.pid, pcb.totalCPU, pcb.avgBurst, pcb.priority,  '  ['+comma.join([str(x) for x in pcb.pageTable])+']'))

class Disk(Componant):
	def __init__(self, id, n_cylinders):
		self.container = queue.PriorityQueue()
		self.key       = 'd' + str(id)
		self.cylinders = n_cylinders
		self.RWhead    = self.cylinders / 2


	def systemCall(self, pcb):
		if pcb != None:
			pcb.sysUpdate()
			pcb.params['cylinder']    = int(getInput('Cylinder #: ', lambda x: 0 <= int(x) <= self.cylinders, 'Cylinder does not exist'))
			pcb.params['file_name']   = input('File Name: ')[:9]
			pcb.params['start_loc']   = input('Location: ')
			pcb.params['r/w']         = getInput('Read or Write? (r/w): ', lambda x : x in ('r', 'w', 'R', 'W'), 'Must enter "r" or "w"')
			pcb.params['file_length'] = input('File Length: ') if pcb.params['r/w'] == 'w' else ''
			pcb.params['elapsed']     = 0
			pcb.priority              = abs(self.RWhead - pcb.params['cylinder'])
			self.push( pcb )

	def snap(self):
		printScroll('---' + self.key)
		for pcb in sorted(self.container.queue):
			printScroll('{0:>3} {1:>11} {2:>9} {3:>5} {4:>8} {5:>11} {6:>11.2f}'.format(pcb.pid, pcb.params['file_name'], pcb.params['start_loc'], pcb.params['r/w'], pcb.params['file_length'], pcb.totalCPU, pcb.avgBurst))

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
		self.container = queue.Queue()
		self.key       = 'c' + str(id)

class Printer(Componant):
	def __init__(self, id):
		self.container = queue.Queue()
		self.key       = 'p' + str(id)

class Memory():
	def __init__(self):
		self.key           = 'm'
		self.frameTable    = [None for _ in range(int(self.memTotal / self.pageSize))]
		self.freeFrameList = collections.deque(range(len(self.frameTable)))
		self.memAvail      = self.memTotal
		self.jobPool       = []

	# Decide if process goes to memory or job pool
	def addProcess(self, pcb):
		if pcb.size <= self.memAvail:
			self.addToMem(pcb)
			inMemory = True
		else:
			self.addToPool(pcb)
			inMemory = False
		return inMemory

	# Add process to memory
	def addToMem(self, pcb):
		nPages = math.ceil(pcb.size / self.pageSize)
		for page in range(nPages):
			frame = self.freeFrameList.popleft()
			pcb.pageTable.append(frame)
			self.frameTable[frame] = pcb.pid
			self.memAvail -= self.pageSize

	# Add process to job pool
	def addToPool(self, pcb):
		pcb.priority = pcb.size
		self.jobPool.append(pcb)
		self.jobPool.sort()

	# remove process from memory (termination)
	def removeFromMem(self, pcb):
		# remove from frame table
		for frame in pcb.pageTable:
			self.frameTable[frame] = None
			self.freeFrameList.append(frame)
			self.memAvail += self.pageSize

	# pop process from job pool and put into memory
	def popFromPool(self):
		pcbs = []
		length = len(self.jobPool)
		for i in range(length):
			job = self.jobPool[length - i - 1]
			if job.size <= self.memAvail:
				pcb = job
				self.jobPool.remove(job)
				pcb.priority = pcb.tao
				self.addToMem(pcb)
				pcbs.append(pcb)
		return pcbs


## Helper Functions
# prints a string and makes sure output doesnt scroll past 24 lines at a time
def printScroll(string):
	global print_count
	if print_count == 23:
		enter = input("press ENTER to see more ... ")
		print_count = 0
	print_count += 1
	print(string)

# gets user input with verification and retries until input is valid
def getInput(prompt, condition, exception='That is not a valid input'):
	while(True):
		try:
			var = input(prompt)
			if condition(var):
				return var
			else: raise
		except KeyboardInterrupt: raise
		except: print(exception)

system = System()
system.run()
