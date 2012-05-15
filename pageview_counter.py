import gzip, os, sys

'''
	@author gibbons4
	May 11, 2012
	Finds the month, year an article was created
	Counts pageviews per month.
	prints hash screen in ugly format
'''

#20011011201847
def getDate(ts) :
	ym = int(ts) / 100000000
	return ym/100, ym %100

view_counts = open('../en_created_cats.tab', 'r')
#Title -> Creation_Dates
creation_dates = {}
creation_counts = {}
flag = 1
for line in view_counts :
	if flag is 1 :
		flag = 0
		continue
	line = line.strip('\n')
	line = line.split('\t')
	year, month = getDate(line[1])
	creation_dates[line[0]] = str(year) + str(month)
	if year not in creation_counts :
		creation_counts[year] = 0
	creation_counts[year] += 1

for k in creation_counts :
	print k, creation_counts[k]
sys.exit()

all_gzipped_files = os.listdir('../pageviews')

def getName(line) :
	line = line.strip('\n')
	line = line.split()
	index = line[1].rfind('/')
	#print line[1], index
	if index != -1 : return line[1][index:], line[2]
	return line[1], int(line[2])

total_counts = {}
found = 0
missed = 0
for fd in all_gzipped_files :
	print 'started: ' , fd
	views_file = gzip.open('../pageviews/' + fd)
	for line in views_file :
		#print line.rstrip('\n')
		name, views = getName(line)
		if name in creation_dates : 
			if creation_dates[name] not in total_counts : total_counts[creation_dates[name]] = 0
			total_counts[creation_dates[name]] += int(views)
			found += int(views)
		else :
			missed += int(views)
	print 'finished: ' , fd

print found, missed
print total_counts
