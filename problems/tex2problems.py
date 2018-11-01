#!/usr/bin/env python3

"""
usage:

./tex2problems.py -show ~/Documents/CUP-vie-durr/*/*.tex > ../_includes/problems_show.html 
./tex2problems.py -hide ~/Documents/CUP-vie-durr/*/*.tex > ../_includes/problems_hide.html 

l'option -yaml n'est plus d'utilité
"""

from sys import argv
import re


def make_pb(chapter, name, order, links):
	return

CHAPTER = "%chapter="
ORDER= "%difficulty="

# regexp = re.compile(r"\\href\{[^\}]*\}{2}")
regexp = re.compile(r"\\href\{([^\}]*)\}\{([^\}]*)\}")

mode = argv[1][1:]

if mode == "show":
	print('<table class="sortable"><tr><th>chapter</th><th>difficulty</th><th>problem</th><th>judge</th></tr>')
elif mode == "hide":
	print('<table class="sortable"><tr><th>difficulty</th><th>problem</th><th>judge</th></tr>')
else:
	print("---")


def print_problem(chapter, name, order, links):
	judge = ", ".join('<a href="%s">%s</a>' % code for code in links)
	if order is not None:
		diff = "&star;" * order
	else:
		diff = ""
	if mode == "yaml":
		print("- chapter: {}\n  name:  {}".format(chapter, name))
		if order is not None:
			print("  order:  ", order)
		print("  links:")
		for url, code in links:
			print("    - url:", url)
			print("      code:", code)
		print()
	elif mode == "show":
		print('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(chapter, diff, name, judge))
	else:	
		print('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(diff, name, judge))


for filename in argv[2:]:
	f = open(filename, "r")
	chapter = filename.split('/')[-1].split('.')[0]
	for line in f:
		if line.startswith("%chapter:"):
			chapter = line()
		if "\\href" in line:
			i = line.find("\\href")
			name = line[:i].strip()
			links = []
			for link in regexp.finditer(line):
				links.append( (link.group(1), link.group(2)) )
			if ORDER in line:
				i = line.find(ORDER) + len(ORDER)
				diff = int(line[i:].split()[0])
				print_problem(chapter, name, diff, links)
			else:
				print_problem(chapter, name, None, links)



if mode != "yaml":
	print('</table>')
