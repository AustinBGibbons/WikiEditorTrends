#!/usr/bin/env python
import sys

SECONDS_PER_WEEK = 60*60*24*7

'''
    @author : susan_biancani
    outputs tab delimited text: age of article, counts of [articles edited, adds, dels],sum and sumsq of [added words, deleted words, net added]
    (Using count, sum, sumsq, you can calculate mean, st dev)
'''
def parseDiffs(diffs):
    numAdds = numDels = lenAdd = lenDel = 0
    for diff in diffs:
        diffParts = diff.split(':',2) # Don't split into more than 3 parts
        if len(diffParts) != 3: 
            continue
        text = diffParts[2][2:-1]
        #text = diffParts[2][2:-1].decode('string_escape').translate(None, '\n*').split(' ')
        #text = filter (lambda a: a is not ' ' and a is not '', text)
        #st = text.index("'") + 1
        #en = text.index("'", st)
        #text = text[st, en].translate(None, '\n*').split(' ')
        if diffParts[1] == '1':
            numAdds += 1
            lenAdd += len(text)
        elif diffParts[1] == '-1':
            numDels += 1
            lenDel += len(text)
    return [numAdds, numDels, lenAdd, lenDel]

def isRevert(comment):
    comment = comment.lower()
    if comment.find('revert') > -1 or comment.find('revers') >-1:
        return 1
    else: return 0
    

def collectWeekData(firstEdit, editData, weeks, ages):
    """ an entry in weeks is: counts of [articles edited, adds, dels],sum and sumsq of [added words, deleted words, net added]"""
    assert len(editData) > 0 
    assert firstEdit != float('inf')
        
    for edit in editData:
        week, numAdds, numDels, lenAdd, lenDel, revert = edit
        age = week - firstEdit
        netAdd = lenAdd - lenDel
        if not ages.has_key(age):
            ages[age] = [0.0]*10
        ages[age][0] += 1
        ages[age][1] += numAdds
        ages[age][2] += numDels
        ages[age][3] += lenAdd
        ages[age][4] += lenAdd*lenAdd
        ages[age][5] += lenDel
        ages[age][6] += lenDel*lenDel
        ages[age][7] += netAdd
        ages[age][8] += netAdd*netAdd
        ages[age][9] += revert
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
get = {'rev_id':0, 'page_id':1, 'namespace':2, 'title':3, 'timestamp':4,
'comment':5, 'minor':6, 'user_id':7, 'user_text':8}

"""This script runs after map_article.py"""
editData = []
firstEdit = float('inf')
lastPage = -1
weeks = {}
ages = {}
#filename = "C:/Users/Susan/Documents/CS341/WikiEditor/subset_test.txt"
#data = open(filename)
#for line in data.readlines():
for line in sys.stdin :
    line = line.strip('\n').split('\t')

    # gather article statistics and output
    page = line[get['page_id']+1]
    if lastPage != page:
        if lastPage < 0:
            lastPage = page
        else:
            collectWeekData(firstEdit, editData, weeks, ages)
            lastPage = page
            editData=[]
            firstEdit = float('inf')
            
    # collect data on each revision       
    weekTimestamp = int(line[get['timestamp']+1])/SECONDS_PER_WEEK
    if weekTimestamp < firstEdit:
        firstEdit = weekTimestamp
    userText = [ line[i] for i in range(get['user_text']+1, len(line)-1) ]
    revert = isRevert(line[get['comment']+1])
    editData.append([weekTimestamp] + parseDiffs(userText) + [revert])

collectWeekData(firstEdit, editData, weeks, ages)

""" an entry in weeks is: counts of [articles edited, edits, adds, dels],sum and sumsq of [added words, deleted words, net added]"""
#out = open("test_results2.txt", 'w')
for week in weeks:
    output = ['w' + str(week)] + [str(w) for w in weeks[week]]
    print '\t'.join(output), '\n'
    #out.write('\t'.join(output) + '\n')
#out.close()
for age in ages:
    output = ['a' + str(age)] + [str(a) for a in ages[age]]
    print '\t'.join(output), '\n'


#data.close()