#!/usr/bin/python

import sys, urllib2

def parseCreationParts(parts):
	lang = None
	name = ''
	time = 0

	if '.' not in parts[0]:
		lang = parts[0].split('.')[0]
		name = urllib2.unquote(parts[1]).strip()
		time = int(parts[2])

	return lang, name, time

def parsePageviewParts(parts):
	lang = None
	name = ''
	views = 0

	if '.' not in parts[0]:
		lang = parts[0].split('.')[0]
		name = urllib2.unquote(parts[1]).strip()
		views = int(parts[2])

	return lang, name, views

for line in sys.stdin:
	parts = line.rstrip('\n').split()

	if len(parts) == 3:
		lang, name, time = parseCreationParts(parts)

		if lang is None:
			continue

		print (lang+':'+urllib2.quote(name))+'\tTIME\t'+str(time)
	elif len(parts) == 4:
		lang, name, views = parsePageviewParts(parts)

		if lang is None:
			continue

		print (lang+':'+urllib2.quote(name))+'\tVIEWS\t'+str(views)

