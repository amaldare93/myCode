from collections import deque
pid_counter = 0
print_count = 0
#FUNCTIONS
## generates queues for hardware
def queue_gen(ch, num):
	key = str(ch + str(num))
	sys[key] = deque()
	#dev_cat[ch].append(key)

## new PCB
def new_PCB():
	global pid_counter
	sys['r'].appendleft({'pid': pid_counter, 'file_name': ' ', 'start_loc': 0, "r/w": '', 'file_length': ''})
	pid_counter += 1

def scrollcheck():
	global print_count
	if print_count == 23:
		enter = input("press ENTER to see more ... ")
		print_count = 0
	print_count += 1

## snapshot
def snapshot(queue):
	global print_count
	print_count = 0

	if queue == 'd': num = n_disk
	elif queue == 'c': num = n_CDRW
	elif queue == 'p': num = n_print

	if queue == "all":
		snapshot('r')
		snapshot('d')
		snapshot('c')
		snapshot('p')

	elif queue == 'r':
		scrollcheck()
		print('PID')
		for q in ('cpu1', 'r'):
			scrollcheck()
			print('---' + q)
			for pcd in reversed(sys[q]):
				scrollcheck()
				print(pcd['pid'])
	else:
		queues = [str(queue + str(i)) for i in range(1, num+1)]
		scrollcheck()
		print('{0:<4} {1:<16} {2:>10} {3:^1} {4:<10}'.format('PID', '| File name', '| Memstart', '| R/W', '| File Length'))
		for q in queues:
			scrollcheck()
			print('---' + q)
			for pcd in reversed(sys[q]):
				scrollcheck()
				print('{0:<6} {1:<14} {2:>10} {3:^7} {4:>11}'.format(pcd['pid'], pcd['file_name'], pcd['start_loc'], pcd['r/w'], pcd['file_length']))


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

		tmp['file_name'] = input("file name: ")

		tmp['start_loc'] = input("starting location: ")

		if 'p' in queue: 
			tmp['r/w'] = 'w'
		else:
			tmp['r/w'] = input("read or write? (r/w): ")

		if tmp['r/w'] == 'w':
			tmp['file_length'] = input("file length: ")

		sys[queue].appendleft(tmp)

def finish_proc(queue):
	if len(sys[queue]) != 0:
		sys['r'].appendleft(sys[queue].pop())

#system generation
##user input
print('Welcome to System Generation')

n_cpu = 1
n_disk = int(input('How many disks are there?: '))
n_CDRW = int(input('How many CD/RW are there?: '))
n_print = int(input('How many printers are there?: '))

##generate queues

sys = {}
dev_cat = {}
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
	elif x == 'exit': return
	elif x == 'Sr': snapshot('r')
	elif x == 'Sd': snapshot('d')
	elif x == 'Sc': snapshot('c')
	elif x == 'Sp': snapshot('p')
	elif x == 'Sall': snapshot('all')
	elif x == 't': terminate('cpu1')
	elif len(x) > 1: interpret(x)
	else: print("that is not a valid command")

#running
command = ' '
print("Starting system. enter 'help' for list of commands")
while(command != 'exit'):
	command = input("enter command: ")
	switch(command)
	cpu_check('cpu1')


