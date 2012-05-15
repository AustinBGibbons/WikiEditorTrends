#!/usr/bin/python

import sys

#cat_file = open(sys.argv[1], 'r')
links_file = open(sys.argv[1], 'r')

#categories = {}
#bad_cats = 0
bad_cls = 0

#for line in cat_file:
#	cats = line[30:].split('),(')
#	for cat in cats:
#		if len(cat) == 0: continue
#		if cat[0] == '(':
#			cat = cat[1:]
#		if cat[-1] == ')':
#			cat = cat[0:-1]
#		cat = cat.split(',')
#		if len(cat) != 6:
#			bad_cats = bad_cats + 1
#			continue
#		categories[int(cat[0])] = cat[1][1:-1];
#
#cat_file.close()

#print "Success! Loaded "+str(len(categories))+" categories. Ignored "+str(bad_cats)+" bad categories."

for line in links_file:
	if line[0:11] != 'INSERT INTO': continue

	cls = line[35:].split('),(')
	for cl in cls:
		if len(cl) == 0: continue
		if cl[0] == '(':
			cl = cl[1:]
		if cl[-1] == ')':
			cl = cl[0:-1]
		cl = cl.split(',')
		if len(cl) != 7:
			bad_cls = bad_cls + 1
			continue
		
		from_page = cl[0]
		print from_page + '\t' + cl[1][1:-1]		

links_file.close()

