#!/usr/bin/env python
import sys

'''
	@author : gibbons4
	Short script to count edits by user id	
'''

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title:3', 'timestamp':4, \
'comment':5, 'minor':6, 'user_id':7, 'user_text':8, 'added_size':9, \
'removed_size':10, 'added':11, 'removed':12, 'action':13}

# count the edits per user
#editorCounts = {}

for line in sys.stdin:
	line = line.strip('\n')
	line = line.split('\t')
	user = line['user_id']
	print  user + '\t'

	'''
	if user not in editorCounts :
		editorCounts[user] = 0
	editorCounts[user] = editorCounts[user]+1
	'''
