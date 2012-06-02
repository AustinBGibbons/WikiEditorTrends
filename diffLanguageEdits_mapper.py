#!/usr/bin/python
import sys, gzip

def getTime(x) :
        start = x.find('>') + 1
        year = int(x[start:start+4])
        start = x.find('-') + 1
        month = int(x[start:start+2])
        #hardcoded for portugal!
        if (year <= 2000) : return -10
        return 12*(year - 2000) + (month - 1)

#def checkRobot(line) :
#	for robot in robots :
#		if robot in line : return False
#	return True

firstFlag = True
user = True
year = {}
age = {}
startTime = -1
lang = ''
firstLine = True
for line in sys.stdin :
	line = line.rstrip('\n')
	if firstLine and 'xml:lang=' in line :
		start = line.find('xml:lang=') + 10
		lang = line[start:start+2]	
		firstLine = False
	#if '\t' not in line :
	#	print 'xxxxxx_'+line + '\t' + str(5)
	if '<timestamp>' in line :
		time = getTime(line)
		if firstFlag : 
			startTime = time
			firstFlag = False
			if time not in year : year[time] = 0
		if time >= 11*12 and time < 12*12 and user:
			year[startTime] += 1
			t_age = time - startTime
			if t_age not in age : age[t_age] = 0
			age[t_age] += 1
	if 'bot' in line.lower() and ('<username>' in line or '<comment>' in line) :
		user = False
	if '</page>' in line :
		firstFlag = True
	if '</revision>' in line :
		user = True

for key in year :
	print lang + '_year_' + str(key) + '\t' + str(year[key])
for t_age in age : 
	print lang + '_age_' + str(t_age) + '\t' + str(age[t_age])

