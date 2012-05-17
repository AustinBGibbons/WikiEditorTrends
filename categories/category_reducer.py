#!/usr/bin/python
import sys

article_id = None
article_cats = set()
for line in sys.stdin:
	line  = line.rstrip('\n').split('\t')
	if len(line) != 2:
		print "here"
		continue

	prev_article_id = article_id	
	article_id = line[0]
	if prev_article_id == article_id:
		article_cats.add(line[1])
	else:
		if prev_article_id is not None and len(article_cats) > 0:
			output = [ article_id ]
			for cat in article_cats:
				output.append(cat)
			print '\t'.join(output)

		article_cats.clear()
		article_cats.add(line[1])

