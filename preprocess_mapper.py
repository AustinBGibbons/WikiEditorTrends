#!/usr/bin/python
import sys, gzip, calendar, datetime, urllib2

def parse(time) :
	return datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ").utctimetuple()

def getTime(time) :
	start = time.find('>') + 1
	end = time.rfind('<')
	#return calendar.timegm(dateutil.parser.parse(time[start:end]).utctimetuple())
	return calendar.timegm(parse(time[start:end]))

firstFlag = True
user = True
startTime = -1
lang = ''
title = ''
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
		#time = getTime(line)
		time = getTime(line)
		if firstFlag : 
			startTime = time
			firstFlag = False
			#if time not in year : year[time] = 0
			time_0 = time
	if '<title>' in line:
		start = line.find('>') + 1
		end = line.rfind('<')
		title = urllib2.quote(line[start:end])
	if '</revision>' in line :
		print lang, title, time_0, time, 1 if user else 0
		user = True
	if 'bot' in line.lower() and ('<username>' in line) :
		user = False
	if '</page>' in line :
		firstFlag = True
	if '</mediawiki>' in line :
		firstLine = True	

