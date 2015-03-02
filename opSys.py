from collections import deque
pid_counter = 0

#FUNCTIONS
## generates queues for hardware
def queue_gen(ch, num):
	key = str(ch + str(num))
	sys[key] = deque()

## new PCB
def new_PCB():
	global pid_counter
	sys['r'].appendleft({'pid': pid_counter, 'params': {'file_name': ' ', 'start_loc': 0, "r/w": '', 'file_length': ''}})
	pid_counter += 1

## snapshot
def snapshot():
	queue = input("which queue do you want to see? ")

	# safeguard
	if queue == "all":
		for q in sys:
			print(q, ":", list(sys[q]), '->')
	elif queue not in sys: 
		print("that device is not in the system")
	else:
		print(list(sys[queue]), '->')

## makes sure CPU is always full
def cpu_check(cpu):
	if len(sys[cpu]) == 0 and len(sys['r']) != 0:
		sys[cpu].append(sys['r'].pop())

## terminate process
def terminate(cpu):
	if len(sys[cpu]) != 0:
		sys[cpu].pop()

## interpret command
def interpret(command):
	if command in sys:
		send_proc('cpu1', command)
	elif command.lower() in sys:
		finish_proc(command.lower())
	else: print('that is not a valid command')

## send process from cpu to queue
def send_proc(cpu, queue):
	if len(sys[cpu]) != 0:
		tmp = sys[cpu].pop()

		tmp['params']['file_name'] = input("file name: ")

		tmp['params']['start_loc'] = input("starting location: ")

		if 'p' in queue: 
			tmp['params']['r/w'] = 'w'
		else:
			tmp['params']['r/w'] = input("read or write? (r/w): ")

		if tmp['params']['r/w'] == 'w':
			tmp['params']['file_length'] = input("file length: ")

		sys[queue].appendleft(tmp)

def finish_proc(queue):
	if len(sys[queue]) != 0:
		sys['r'].appendleft(sys[queue].pop())

#system generation
##user input
'''
print('Welcome to System Generation')
n_disk = int(input('How many disks are there?: '))
n_CDRW = int(input('How many CD/RW are there?: '))
n_print = int(input('How many printers are there?: '))
'''
n_cpu = 1
n_disk = 1
n_CDRW = 1
n_print = 1

##generate queues

sys = {}
queue_gen('r', '')
for i in range(1, n_cpu+1):
	queue_gen('cpu', i)
for i in range(1, n_disk+1):
	queue_gen('d', i)
for i in range(1, n_CDRW+1):
	queue_gen('c', i)
for i in range(1, n_print+1):
	queue_gen('p', i)



##init system commands
def switch(x): 
	if x == 'A': new_PCB()
	elif x == 'S': snapshot()
	elif x == 't': terminate('cpu1')
	elif len(x) > 1: interpret(x)
	elif x == 'exit': return
	else: print("that is not a valid command")
	#'help': commands(),

#running
command = ' '
print("Starting system. enter 'help' for list of commands")
while(command != 'exit'):
	command = input("enter command: ")
	switch(command)
	cpu_check('cpu1')


