import sys

#year-month, <count>
for line in sys.stdin
	line  = line.rstrip('\n')
	line = line.split('\t')
	for i in range(0, len(line)) :
		summed += int(line[i])

	print line[0], summed
