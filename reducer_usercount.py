#!/usr/bin/env python
import sys

'''
        @author : gibbons4
	see map.py
'''

#count the commits per editor
editorCommits = {}

for line in sys.stdin :
	line = line.strip('\n')
	line = line.split('\t')
	user = line[0]
	if user not in editorCommits : editorCommits[user] = 0
	editorCommits[user] = editorCommits[user] + 1

for k in editorCommits : 
	print k+'\t'+str(editorCommits[k])
