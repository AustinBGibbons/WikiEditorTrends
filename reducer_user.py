#!/usr/bin/env python
import sys
from sets import Set

'''
        @author : davidvetrano
	see map.py
'''

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4,
'comment':5, 'minor':6, 'user_id':7, 'user_text':8}

def processAndOutput(user, revisions):
	output = [ user ]

	# number of pages edited
	pages = Set()
	for rev_id in revisions:
		revision = revisions[rev_id]
		pages.add(revision['page_id'])
	output.append(str(len(pages)))

	print '\t'.join(output)

revisions = {}
lastUser = -1

for line in sys.stdin :
	line = line.strip('\n').split('\t')

	user = line[0]
	if lastUser != user:
		if lastUser < 0:
			lastUser = user
			continue
		# process all revisions for a user
		processAndOutput(user, revisions)
		lastUser = user
		revisions = {}

	# collect revisions for a user
	rev = line[get['rev_id']+1]
	edit = {}
	for key in get:
		edit[key] = line[get[key]+1]
	revisions[rev] = edit

