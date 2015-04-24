'''
Zombit monitoring
=================

The first successfully created zombit specimen, Dolly the Zombit, needs constant monitoring, and Professor Boolean has tasked the minions with it. Any minion who monitors the zombit records the start and end times of their shifts. However, those minions, they are a bit disorganized: there may be times when multiple minions are monitoring the zombit, and times when there are none!

That's fine, Professor Boolean thinks, one can always hire more minions... Besides, Professor Boolean can at least figure out the total amount of time that Dolly the Zombit was monitored. He has entrusted you, another one of his trusty minions, to do just that. Are you up to the task?

Write a function answer(intervals) that takes a list of pairs [start, end] and returns the total amount of time that Dolly the Zombit was monitored by at least one minion. Each [start, end] pair represents the times when a minion started and finished monitoring the zombit. All values will be positive integers no greater than 2^30 - 1. You will always have end > start for each interval.

'''

def answer(intervals):
	# your code here
	condensedIntervals = []
	sortedIntervals = sorted(intervals)
	condensedIntervals.append(sortedIntervals[0])

	changed = False
	while changed == False:
		for interval in sortedIntervals[1:]:
			flag = False
			for condensed in condensedIntervals:

				start = condensed[0]
				end = condensed[1]

				# if interval is completely within condensed interval
				# 	interval is redundent, so do nothing
				if start <= interval[0] <= end and start <= interval[1] <= end:
					flag = True

				# if interval starts within condensed, but ends outside 
				# 	extend condensed to new end time
				elif start <= interval[0] <= end:
					condensed[1] = interval[1]
					flag = True

			# if interval is not within any condensed interval
			#	create new condensed interval 
			# 	raise changed flag to restart process to double check for additional condensement
			if flag == False:
				condensedIntervals.append(interval)
				changed = True

		if changed == False:
			break
		else:
			changed = False

	return sum([interval[1] - interval[0] for interval in condensedIntervals]) 

print(answer([[1, 3], [4, 6], [7, 10], [8, 11], [1, 5]]))








