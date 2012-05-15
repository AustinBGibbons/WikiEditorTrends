#!/usr/bin/env python
import sys
from sets import Set
import math

'''
    @author : susan_biancani
    outputs tab delimited file: week, timestamp of first edit, time of each edit 
'''


def stDev(values, mean):
    n = len(values)
    return math.sqrt(sum((x-mean)**2 for x in values) / n)


# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'curr_week':0, 'page':1, 'first_week':2}

def processAndOutput(week, firstWeeks):
    if len(firstWeeks) == 0: #Only one line in the data for that week
        avgWeek = float(week)
        stDevWeeks = 0.0
    else:
        avgWeek = float(sum(firstWeeks))/len(firstWeeks)
        stDevWeeks = stDev(firstWeeks, avgWeek)
        
    output = [ week, str(avgWeek), str(stDevWeeks) ]
    print '\t'.join(output)

firstWeeks = []
lastWeek = -1

for line in sys.stdin :
    line = line.strip('\n').split('\t')
    # gather article statistics and output
    #week = line[get['curr_week']+1]
    week = line[get['curr_week']]
    if lastWeek != week:
        if lastWeek < 0:
            lastWeek = week
            continue
        processAndOutput(week, firstWeeks)
        lastWeek = week
        firsttWeeks = []

    # collect edit time for a revision
    firstWeeks.append(int(line[get['first_week']] ))
    #firstWeeks.append(int(line[get['first_week']+1] ))
    

