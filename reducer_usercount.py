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
	editorCommits[line[0]] = len(line)-1

print editorCommits
