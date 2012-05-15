#!/usr/bin/python

import sys

cat_file = open(sys.argv[1], 'r')
links_file = open(sys.argv[2], 'r')

categoryMap = {}
bad_cls = 0

for line in cat_file:
	cats = line.split(' ')
	
	firstCat = cats[0][29:-1]
	secondCat = cats[2][29:-1]
	relation = cats[1][1:-1]

	if relation == 'http://www.w3.org/2004/02/skos/core#broader' and firstCat != secondCat:
		categoryMap[firstCat] = secondCat

cat_file.close()

rootCats = set([
	'Category:Agriculture',
	'Category:Arts',
	'Category:Belief',
	'Category:Business',
	'Category:Chronology',
	'Category:Culture',
	'Category:Education',
	'Category:Environment',
	'Category:Geography',
	'Category:Health',
	'Category:Humanities',
	'Category:Language',
	'Category:Law',
	'Category:Life',
	'Category:Mathematics',
	'Category:Nature',
	'Category:Politics',
	'Category:Science',
	'Category:Society',
	'Category;Technology'	
])

def categoryToTopCategory(category):
	visitedSet = set()
	curr = category
	prev = None

	while curr in categoryMap:
		if curr in rootCats:
			return prev

		if curr in visitedSet:
			return None

		visitedSet.add(curr)
		prev = curr
		curr = categoryMap[curr]
	
	return None

#print "Success! Loaded "+str(len(categoryMap))+" category relations."
#exit(0)

for line in links_file:
	if line[0:11] != 'INSERT INTO': continue

	cls = line[35:].split('),(')
	for cl in cls:
		if len(cl) == 0: continue
		if cl[0] == '(':
			cl = cl[1:]
		if cl[-1] == ')':
			cl = cl[0:-1]
		cl = cl.split(',')
		if len(cl) != 7:
			bad_cls = bad_cls + 1
			continue
		
		from_page = cl[0]
		topCat = categoryToTopCategory('Category:'+cl[1][1:])
		if topCat is not None:
			print from_page + '\t' + topCat

links_file.close()

