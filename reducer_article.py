#!/usr/bin/env python
import sys

'''
        @author : gibbons4
	see map.py
'''

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4,
'comment':5, 'minor':6, 'user_id':7, 'user_text':8, 'added_size':9,
'removed_size':10, 'added':11, 'removed':12, 'action':13}


pageInfo = {}
lastPage = -1

for line in sys.stdin :
	line = line.strip('\n')
	line = line.split('\t')

	# collect edit info for a page
	page = line[0]
	user = line[get['user_id']+1]
	rev = line[get['rev_id']+1]
	processPage = False
	if lastPage != page:
		lastPage = page
		processPage = True

	# gather article statistics
	if processPage:
		for user_id in pageInfo:
			pageInfo['shit']='empty'
		pageInfo = {}

	# output edit statistics			 
	for rev in pageInfo: 
		print rev+'\t'+str(pageInfo[rev])

	editInfo = {}
	for key in get:
		print line
		editInfo[key] = line[get[key]+1]
	pageInfo[rev] = editInfo

