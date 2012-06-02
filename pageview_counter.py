import gzip, os, sys, urllib2

'''
	@author gibbons4, dvetrano
	May 11, 2012
	Finds the month, year an article was created
	Counts pageviews per month.
	prints hash screen in ugly format
'''

# load creation dates
languages = []
creation_dates = {}
for lang_dir in os.listdir('./MetaHistoryCreationDates/'):
	lang = lang_dir.split('_')[0]
	languages.append(lang)
	print "process language "+lang
        for line in open('./MetaHistoryCreationDates/'+lang+'_creation', 'r'):
		parts = line.rstrip('\n').split(' ')
		name = ' '.join(parts[0:-1])
		creation_dates[(lang, name)] = parts[-1]

def parsePageviewLine(line):
	parts = line.split()

	lang = parts[0].split('.')[0]
	name = urllib2.unquote(parts[1])
	views = int(parts[2])

	return lang, name, views

total_counts = {}
found = 0
missed = 0
for fd in os.listdir('./pageviews'):
	print 'started: ', fd
	views_file = gzip.open('./pageviews/' + fd)
	for line in views_file:
		lang, name, views = parsePageviewLine(line)
		if lang not in total_counts:
			total_counts[lang] = {}
		if (lang, name) not in creation_dates:
			missed += views
			continue
		creation_date = creation_dates[(lang, name)]
		if creation_date not in total_counts[lang]:
			total_counts[lang][creation_date] = 0
		
		total_counts[lang][creation_date] += views
		found += views
	print 'finished: ' , fd

print 'Found: ', found, 'Missed: ', missed
print 'Write output files'

for lang in languages:
	if lang not in total_counts:
		continue

	f = open('./views-by-lang/'+lang, 'w')
	for date in total_counts[lang]:
		f.write(date+'\t'+str(total_counts[lang][date])+'\n')
	f.close()
	
