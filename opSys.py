import queue
pid_counter = 0

#FUNCTIONS
##generates queues for hardware
def queue_gen(ch, num):
	key = str(ch + str(num))
	sys[key] = queue.Queue()
	#switch[key] = send()

##new PCB
def new_PCB():
	global pid_counter
	sys['r'].put({'pid': pid_counter, 'params': { }})
	pid_counter += 1

## snapshot
def snapshot():
	queue = input("which queue do you want to see? ")

	# safeguard
	if queue not in sys: 
		print("that device is not in the system")
	return

	for i in range(sys[queue].qsize()):
		tmp = sys[queue].get()
		print(tmp['pid'])
		sys[queue].put(tmp)


#system generation
##user input
'''
print('Welcome to System Generation')
n_disk = int(input('How many disks are there?: '))
n_CDRW = int(input('How many CD/RW are there?: '))
n_print = int(input('How many printers are there?: '))
'''

n_disk = 1
n_CDRW = 1
n_print = 1

##generate queues

sys = {}
queue_gen('r', '')
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

	#'help': commands(),




#running
command = ' '
print("Starting system. enter 'help' for list of commands")
while(command != 'exit'):
	command = input("enter command: ")
	switch(command)



