import sys, os

fileName = 'dataset-all-timesplitters2.tsv'
if len(sys.argv) > 1 :
	fileName = sys.argv[1] 
orig = open(fileName, 'r')

directory = fileName.split('.')[0] + '/'
if os.path.isdir(directory) :
	print 'Looks like the data already exists!'
	sys.exit(0)

os.mkdir(directory)

fileList = {}
bad = 0
for line in orig :
	line.rstrip('\n')
	(user, tab, data) = line.partition('\t')
	if '-' not in user :
		bad = bad +1
		continue
	(user, date) = user.split('-')
	date = directory + date + '.tsv'
	if date not in fileList :
		dateFile = open(date, 'w+')
		fileList[date] = dateFile
	fileList[date].write(user+'\t'+data)

print 'bad values: ', bad
