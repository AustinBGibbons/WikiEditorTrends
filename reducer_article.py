#!/usr/bin/env python
import sys

'''
        @author : gibbons4
	see map.py
'''

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4,
'comment':5, 'minor':6, 'page_id':7, 'page_text':8, 'added_size':9,
'removed_size':10, 'added':11, 'removed':12, 'action':13}

#count the commits per editor
editorCommits = {}

pageInfo = []

for line in sys.stdin :
	line = line.strip('\n')
	line = line.split('\t')
	page = line[0]
	if user not in editorCommits : editorCommits[user] = 0
	pageInfo
	editorCommits[user] = editorCommits[user] + 1

for k in editorCommits : 
	print k+'\t'+str(editorCommits[k])
