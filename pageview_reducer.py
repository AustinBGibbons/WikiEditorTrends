#!/usr/bin/python
import sys

summed = 0
key = -1
#year-month, <count>
for line in sys.stdin :
	line  = line.rstrip('\n')
	line = line.split('\t')
	if key != line[0] :
		if key != -1 : print key, summed
		key = line[0]
		summed = 0
	for i in range(1, len(line)) :
		summed += int(line[i])

print key, summed
