import gzip, os, sys
#from datetime import datetime

#20011011201847
def getDate(ts) :
	ym = int(ts) / 100000000
	return ym/100, ym %100

view_counts = open('../en_created_cats.tab', 'r')
#Title -> Creation_Dates
creation_dates = {}
flag = 1
for line in view_counts :
	if flag is 1 :
		flag = 0
		continue
	line = line.strip('\n')
	line = line.split('\t')
	year, month = getDate(line[1])
	creation_dates[line[0]] = str(year) + str(month)

all_gzipped_files = os.listdir('../pageviews')

def getName() :

total_counts = {}
for fd in all_gzipped_files :
	views = gzip.open('../pageviews/' + fd)
	for line in views :
		name = getName(line)
