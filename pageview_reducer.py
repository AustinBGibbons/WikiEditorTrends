import gzip, os, sys, urllib2

'''
	@author gibbons4, dvetrano
	May 11, 2012
	Finds the month, year an article was created
	Counts pageviews per month.
	prints hash screen in ugly format
'''

languages = []
total_counts = {}

for line in sys.stdin:
	parts = line.rstrip('\n').split('\t')

	lang = parts[0]
	date = parts[1]
	views = int(parts[2])

	if lang not in total_counts:
		languages.append(lang)
		total_counts[lang] = {}

	if date not in total_counts[lang]:
		total_counts[lang][date] = 0

	total_count[lang][date] += views	

for lang in languages:
	if lang not in total_counts:
		continue

	for date in total_counts[lang]:
		print lang+'\t'+str(date)+'\t'+str(total_counts[lang][date])+'\n'
	
