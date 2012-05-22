import sys

'''
	Written by Ausitn at 3:40 am
	Some lessons are never learned

	x is input, read the function name
'''

#what gets returned here doesnt matter so long as it is the same for each page
def getTitle(x) :
	#start = x.find('>') + 1
	#end = x[start:].find('<') - 1
	#title = int(x[start:end])
	#return title	
	return x

#using the number of months since Dec. 1999 as a hacky time solution
def getTime(x) :
	start = x.find('>') + 1
	year = int(x[start:start+4])
	start = x.find('-') + 1
	month = int(x[start:start+2])
	#hardcoded for portugal!
	if (year == 2000) : return -10
	return 12*(year - 2000) + (month - 1)

histo = {}

def histogram(timeArr) :
	global histo
	for t in timeArr :
		# this if statement limits the scope to 2011
		if t >= 11*12 and t < 12*12 :
			#changing diff froma ges to time
			# so inefficient, so overdue
			diff = timeArr[0]
			#diff = t - timeArr[0]
			if diff not in histo : histo[diff] = 0
			histo[diff] += 1

if len(sys.argv) < 2 :
	print >>sys.stderr, 'python time_title_parser.py time_title_file'

base = open(sys.argv[1], 'r')
times = {}
time = 0
skipped = 0
skiplist = []
for x in base :
	if 'timestamp' in x and 'logtitle' in x :
		if x not in skiplist :
			skipped += 1
			skiplist.append(x)
		continue
	if 'timestamp' in x :
		time = getTime(x)
	if 'logtitle' in x :
		title = getTitle(x)
		if title not in times : times[title] = []
		times[title].append(time)

for t in times :
	histogram(times[t])

print >>sys.stderr, 'Number of pages: ', len(times)

for key in histo :
	print '(',key, ',', histo[key], ')'

print >>sys.stderr, skipped
