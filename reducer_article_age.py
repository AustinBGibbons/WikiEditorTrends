#!/usr/bin/env python
import sys
from sets import Set

'''
    @author : susan_biancani
    outputs tab delimited text: page id, timestamp of first edit, time of each edit 
'''

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4,
'comment':5, 'minor':6, 'user_id':7, 'user_text':8}

def processAndOutput(page, editTimes):
    first = min(editTimes)
    
    for time in editTimes:
        output = [ page, str(first) ]
        output.append(str(time))
        print '\t'.join(output)

editTimes = []
lastPage = -1

for line in sys.stdin :
    line = line.strip('\n').split('\t')

    # gather article statistics and output
    page = line[get['page_id']+1]
    if lastPage != page:
        if lastPage < 0:
            lastPage = page
            continue
        processAndOutput(page, editTimes)
        lastPage = page
        editTimes = []

    # collect edit time for a revision
    editTimes.append(int(line[get['timestamp']+1] ))
    

