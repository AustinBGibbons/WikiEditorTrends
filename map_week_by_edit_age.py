#!/usr/bin/env python
import sys

SECONDS_PER_WEEK = 60*60*24*7

'''
    @author : susan_biancani
    outputs tab delimited text: week (numerical) of this edit, page id, week this article was created 
    (first week is the week of a given edit)
        
'''

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'page_id':0, 'first_edit':1, 'edit_time':2}

for line in sys.stdin:
    line = line.strip('\n')
    fields = line.split('\t')
    page = fields[get['page_id']+1]
    
    if page != 'None' :
        first = int(fields[get['first_edit']])
        curr = int(fields[get['edit_time']])
        first_week = str(first/SECONDS_PER_WEEK)
        curr_week = str(curr/SECONDS_PER_WEEK)        
        data = [curr_week, page, first_week]
        print  '\t'.join(data)

