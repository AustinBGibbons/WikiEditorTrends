#!/usr/bin/python

import sys

'''
	@author gibbons4, dvetrano
	May 11, 2012
	Finds the month, year an article was created
	Counts pageviews per month.
	prints hash screen in ugly format
'''

last_key = None
last_lang = None
views_current = None
time_current = None

for line in sys.stdin:
	parts = line.rstrip('\n').split('\t')

	key = parts[0]
	line_type = parts[1]
	value = int(parts[2])

	if key != last_key:
		if views_current is not None and time_current is not None:
			print last_lang+'\t'+str(time_current)+'\t'+str(views_current)

		time_current = None
		views_current = None

	if line_type == 'VIEWS':
		if views_current is None:
			views_current = value
		else:
			views_current += value
	elif line_type == 'TIME':
		time_current = value
	
	last_key = key
	last_lang = key.split(':')[0]

