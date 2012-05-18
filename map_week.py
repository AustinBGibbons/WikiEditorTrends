#!/usr/bin/env python
import sys
SECONDS_PER_WEEK = 60*60*24*7

'''
    @author : biancani
    outputs tab delimited text: week (numerical), rest of line 
'''

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4,
'comment':5, 'minor':6, 'user_id':7, 'user_text':8}

for line in sys.stdin:
    line = line.strip('\n')
    fields = line.split('\t')
    timestamp = fields[get['timestamp']]
    if timestamp != 'None':
        week = str(int(timestamp)/SECONDS_PER_WEEK) 
        print  week + '\t' + line

