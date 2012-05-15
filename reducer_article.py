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

def processAndOutput(page, pageInfo):
	output = [ page ]

	# number of unique registered users
	users = Set()
	for rev_id in pageInfo:
		revision = pageInfo[rev_id]
		user = revision['user_id']
		if user != 'None': users.add(user)
	output.append(str(len(users)))

	print '\t'.join(output)

pageInfo = {}
lastPage = -1

for line in sys.stdin :
	line = line.strip('\n').split('\t')

	# gather article statistics and output
	page = line[get['page_id']+1]
	if lastPage != page:
		if lastPage < 0:
			lastPage = page
			continue
		processAndOutput(page, pageInfo)
		lastPage = page
		pageInfo = {}

	# collect edit info for a revision
	rev = line[get['rev_id']+1]
	editInfo = {}
	for key in get:
		editInfo[key] = line[get[key]+1]
	pageInfo[rev] = editInfo

