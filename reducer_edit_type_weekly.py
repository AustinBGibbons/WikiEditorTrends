#!/usr/bin/env python
import sys

SECONDS_PER_WEEK = 60*60*24*7

'''
    @author : susan_biancani
    outputs tab delimited text: week, counts of [articles edited, adds, dels],sum and sumsq of [added words, deleted words, net added]
'''
def parseDiffs(diffs):
    numAdds = numDels = lenAdd = lenDel = 0
    for diff in diffs:
        diffParts = diff.split(':',2) # Don't split into more than 3 parts
        if len(diffParts) != 3: 
            continue
        text = diffParts[2][2:-1].decode('string_escape').translate(None, '\n*').split(' ')
        #st = text.index("'") + 1
        #en = text.index("'", st)
        #text = text[st, en].translate(None, '\n*').split(' ')
        if diffParts[1] == '1':
            numAdds += 1
            lenAdd += len(text)
        elif diffParts[1] == '-1':
            numDels += 1
            lenDel += len(text)
        else:
            sys.stderr.write("Unknown edit type: " + diff)

    return [numAdds, numDels, lenAdd, lenDel]

def isRevert(comment):
    comment = comment.lower()
    if comment.find('revert') > -1 or comment.find('revers') >-1:
        return 1
    else: return 0

def collectWeekData(editData, weeks):
    """ an entry in weeks is: counts of [articles edited, adds, dels],sum and sumsq of [added words, deleted words, net added]"""
    assert len(editData) > 0 
        
    for edit in editData:
        week, numAdds, numDels, lenAdd, lenDel, revert = edit
        #age = week - firstEdit
        netAdd = lenAdd - lenDel
        if not weeks.has_key(week):
            weeks[week] = [0.0]*10
        weeks[week][0] += 1
        weeks[week][1] += numAdds
        weeks[week][2] += numDels
        weeks[week][3] += lenAdd
        weeks[week][4] += lenAdd*lenAdd
        weeks[week][5] += lenDel
        weeks[week][6] += lenDel*lenDel
        weeks[week][7] += netAdd
        weeks[week][8] += netAdd*netAdd
        weeks[week][9] += revert
         
# Schema defined at : 
#https://github.com/whym/RevDiffSearch/blob/master/README.rst
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4, 'comment':5, 'minor':6, 'user_id':7, 'user_text':8}

editData = []
#firstEdit = float('inf')
lastWeek = -1
weeks = {}
#filename = "C:/Users/Susan/Documents/CS341/WikiEditor/subset_test.txt"
#data = open(filename)
#for line in data.readlines():
for line in sys.stdin :
    line = line.strip('\n').split('\t')

    # gather article statistics and output
    week = line[0]
    if lastWeek != week:
        if lastWeek < 0:
            lastWeek = week
        else:
            collectWeekData(editData, weeks)
            lastWeek = week
            editData=[]
            #firstEdit = float('inf')
            
    # collect data on each revision       
    #weekTimestamp = int(line[get['timestamp']+1])/SECONDS_PER_WEEK
    userText = [ line[i] for i in range(get['user_text']+1, len(line)-1) ]
    revert = isRevert(line[get['comment']])
    editData.append([week] + parseDiffs(userText) + [revert])

collectWeekData(editData, weeks)

""" an entry in weeks is: counts of [articles edited, edits, adds, dels],sum and sumsq of [added words, deleted words, net added]"""

for week in weeks:
    output = [str(week)] + [str(w) for w in weeks[week]]
    print '\t'.join(output), '\n'

#data.close()