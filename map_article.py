#!/usr/bin/env python
import sys

'''
	@author : gibbons4
	Short script to count edits by page id	
'''

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4,
'comment':5, 'minor':6, 'user_id':7, 'user_text':8}

for line in sys.stdin:
	line = line.strip('\n')
	fields = line.split('\t')
	page = fields[get['page_id']]
	if page != 'None' :
		print  page + '\t' + line

