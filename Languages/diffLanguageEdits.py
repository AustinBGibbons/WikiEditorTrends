import gzip, sys

if len(sys.argv) != 2 :
	print 'python diffLanguages.py input_file'

x = gzip.open(sys.argv[1], 'r')
ctr = 0
for y in x :
	if '<timestamp>' in y or '<logtitle>' in y: 
		print y.rstrip()
