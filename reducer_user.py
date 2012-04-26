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

def parseDiffs(diffs):
	diffList = []
	for diff in diffs:
		diffParts = diff.split(':')
		if len(diffParts) != 3: continue
		diffList.append({
			'position': diffParts[0],
			'type': ('ADD' if diffParts[1]=='1' else 'REMOVE'),
			'text': diffParts[2][2:-1].decode('string_escape') 
		})
	return diffList

def processAndOutput(user, revisions):
	output = [ user ]

	# number of pages touched
	pages = Set()
	for rev_id in revisions:
		revision = revisions[rev_id]
		pages.add(revision['page_id'])
	output.append(str(len(pages)))

	# number of additions and removals
	numAdditions = 0
	numRemovals = 0
	for rev_id in revisions:
		revision = revisions[rev_id]
		diffs = parseDiffs(revision['user_text'])
		for diff in diffs:
			if diff['type'] == 'ADD':
				numAdditions = numAdditions + 1
			else:
				numRemovals = numRemovals + 1
	output.append(str(numAdditions))
	output.append(str(numRemovals))

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
		if key == 'user_text':
			edit[key] = [ line[i] for i in range(get[key]+1, len(line)-1) ]
		else:
			edit[key] = line[get[key]+1]
	revisions[rev] = edit

