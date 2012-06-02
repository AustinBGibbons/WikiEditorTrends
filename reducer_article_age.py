#!/usr/bin/env python
import sys

SECONDS_PER_WEEK = 60*60*24*7

'''
    @author : susan_biancani
    outputs tab delimited text: week, summary stats for age of edits in that week
    summary stats = count, sum, sumsq
    (Using count, sum, sumsq, you can calculate mean, st dev)
'''

def findFirstEdit(editTimes):
    return min(editTimes)

def collectWeekData(weeks, editTimes):
    if len(editTimes) == 0:
        return
    firstEdit = findFirstEdit(editTimes)
    for edit in editTimes:
        age = edit - firstEdit
        if not weeks.has_key(edit):
            weeks[edit] = [0.0, 0.0, 0.0]
        weeks[edit][0]+=1
        weeks[edit][1]+=age
        agesq = weeks[edit][2]
        weeks[edit][2]+=(age*age) 
        if agesq > weeks[edit][2]:
            sys.stderr.write("Underflow on " + str(firstEdit) + " " + str(edit))

# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4,
'comment':5, 'minor':6, 'user_id':7, 'user_text':8}

"""Each week is a list: [count, sum(age of edits), sumsq(age of edits)]"""
weeks = {}
editTimes = []
lastPage = -1
#filename = "C:/Users/Susan/Documents/CS341/WikiEditor/subset_test.txt"
#data = open(filename)
#for line in data.readlines():
for line in sys.stdin :
    line = line.strip('\n').split('\t')

    # gather article statistics and output
    page = line[get['page_id']+1]
    timestamp = line[get['timestamp']+1]
    weekTimestamp = int(timestamp)/SECONDS_PER_WEEK
    if lastPage != page:
        if lastPage < 0:
            lastPage = page
        else:
            #firstEdit = findFirstEdit(lastPage, editTimes)
            collectWeekData(weeks, editTimes)
            lastPage = page
            editTimes = []

    # collect edit time for a revision
    editTimes.append(weekTimestamp)
    
collectWeekData(weeks, editTimes)

for week in weeks:
    output = [str(week)] + [str(w) for w in weeks[week]]
    print '\t'.join(output)

#data.close()