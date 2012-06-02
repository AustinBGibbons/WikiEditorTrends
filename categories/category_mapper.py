#!/usr/bin/python

import sys

cat_file = open(sys.argv[1], 'r')
links_file = open(sys.argv[2], 'r')

categoryMap = {}
num_cats_success = 0
num_cats_cycle = 0
num_cats_no_path = 0

rootCats = set([
	'Category:Agriculture',
	'Category:Arts',
	'Category:Belief',
	'Category:Business',
	'Category:Chronology',
	'Category:Communication',
	'Category:Concepts',
	'Category:Culture',
	'Category:Education',
	'Category:Engineering',
	'Category:Environment',
	'Category:Geography',
	'Category:Health',
	'Category:Humanities',
	'Category:Language',
	'Category:Law',
	'Category:Life',
	'Category:Literature',
	'Category:Mathematics',
	'Category:Nature',
	'Category:Natural_sciences',
	'Category:People',
	'Category:Philosophy',
	'Category:Politics',
	'Category:Science',
	'Category:Society',
	'Category:Team_sports',
	'Category:Technology',
	'Category:Wikipedia_administration',
	'Category:Wikipedia_images'	
])

def categoryToTopCategory(category):
	global num_cats_success, num_cats_cycle, num_cats_no_path

	visitedSet = set()
	curr = category
	prev = None

	while curr in categoryMap:
		if curr in rootCats:
			num_cats_success += 1
			return curr

		if curr in visitedSet:
			num_cats_cycle += 1
			return None

		visitedSet.add(curr)
		prev = curr
		curr = categoryMap[curr]
		#print "\tMove to "+curr
	
	num_cats_no_path += 1
	#print "\tGive up at "+curr
	return None

for line in cat_file:
	cats = line.split(' ')
	
	firstCat = cats[0][29:-1]
	secondCat = cats[2][29:-1]
	relation = cats[1][1:-1]

	if relation == 'http://www.w3.org/2004/02/skos/core#broader' and firstCat != secondCat:
		categoryMap[firstCat] = secondCat

cat_file.close()

for line in links_file:
	if line[0:11] != 'INSERT INTO': continue

	cls = line[35:].split('),(')
	for cl in cls:
		if len(cl) == 0: continue
		if cl[0] == '(':
			cl = cl[1:]
		if cl[-1] == ')':
			cl = cl[0:-1]

		curr_field = 0
		from_page = ''
		to_cat = ''
		in_quotes = False
		for i in range(0, len(cl)):
			if cl[i] == ',' and not in_quotes and curr_field < 2:
				curr_field += 1
				continue

			if cl[i] == '\'':
				in_quotes = not in_quotes
				continue

			if curr_field == 0:
				from_page += cl[i]

			if curr_field == 1:
				to_cat += cl[i]

		#print "Category: "+to_cat
		topCat = categoryToTopCategory('Category:'+to_cat)
		if topCat is not None:
			print from_page + '\t' + topCat

links_file.close()

#print "Success!"
#print "\tLoaded "+str(len(categoryMap))+" category relations."
#print "\t"+str(num_cats_success)+" page categories normalized"
#print "\t"+str(num_cats_cycle)+" page categories failed due to cycle check"
#print "\t"+str(num_cats_no_path)+" page categories failed due to lack of path"

