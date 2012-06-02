#!/usr/bin/python
import sys

timeHisto = {}

for line in sys.stdin :
	line = line.rstrip('\n')
	line = line.split('\t')
	if line[0] not in timeHisto : timeHisto[line[0]] = 0
	for x in range(1, len(line)) :
		timeHisto[line[0]] += int(line[x])

	#print line

for key in timeHisto : 
	print key, timeHisto[key]
