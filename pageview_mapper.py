import sys, urllib2

# load creation dates
languages = []
creation_dates = {}
for line in open('./revision-tuples/co', 'r'):
	parts = line.rstrip('\n').split(' ')
	lang = parts[0]
	name = urllib2.unquote(parts[1]).strip()
	t0 = int(parts[2])
	tEdit = int(parts[3])
	isUser = int(parts[4])
	if isUser == 0:
		continue
	if (lang, name) not in creation_dates:
		creation_dates[(lang, name)] = tEdit / 604800

def parsePageviewLine(line):
	parts = line.split()

	lang = None
	name = ''
	views = 0

	if '.' not in parts[0]:
		lang = parts[0].split('.')[0]
		name = urllib2.unquote(parts[1]).strip()
		views = int(parts[2])

	return lang, name, views

total_counts = {}
found = 0
missed = 0
for line in sys.stdin:
	lang, name, views = parsePageviewLine(line)
	if lang is None:
		continue
	if lang not in languages:
		languages.append(lang)
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

for lang in languages:
	if lang not in total_counts:
		continue
	for date in total_counts[lang]:
		print lang+'\t'+str(date)+'\t'+str(total_counts[lang][date])

