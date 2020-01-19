#!/usr/bin/env python3

"""
usage:

./tex2problems.py -show ~/Documents/CUP-vie-durr/*/*.tex > ../_includes/problems_show.html 
./tex2problems.py -hide ~/Documents/CUP-vie-durr/*/*.tex > ../_includes/problems_hide.html 

l'option -yaml n'est plus d'utilité
"""

from sys import argv, stderr
import re
from collections import Counter
from urllib.parse import urlsplit
import urllib.error
from urllib.request import urlopen
import time


def make_pb(chapter, name, order, links):
    return

CHAPTER = "%chapter="
ORDER= "%difficulty="

# regexp = re.compile(r"\\href\{[^\}]*\}{2}")
regexp = re.compile(r"\\href\{([^\}]*)\}\{([^\}]*)\}")

mode = argv[1][1:]

if mode == "show":
        # print('<table class="sortable"><tr><th>chapter</th><th>difficulty</th><th>problem</th><th>judge</th></tr>')
        print('<table class="sortable"><tr><th>chapter</th><th>problem</th><th>judge</th></tr>')
elif mode == "hide":
    # print('<table class="sortable"><tr><th>difficulty</th><th>problem</th><th>judge</th></tr>')
    print('<table class="sortable"><tr><th>problem</th><th>judge</th></tr>')
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
        # print('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(chapter, diff, name, judge))
        print("<table>")
        print('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(chapter, name, judge))
    else:   
        # print('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(diff, name, judge))
        print("<table>")
        print('<tr><td>{}</td><td>{}</td></tr>'.format(name, judge))


c = Counter()
for filename in argv[2:]:
    f = open(filename, "r")
    chapter = filename.split('/')[-1].split('.')[0]
    for line in f:
        if line.startswith("%chapter:"):
            chapter = line()
        if "\\href" in line: # and line[0] != '%': # ignore references commented out 
            print(line)
            i = line.find("\\href")
            name = line[:i].strip()
            links = []
            for link in regexp.finditer(line):
                url = link.group(1)
                domain = urlsplit(url).netloc
                c[domain] += 1
                links.append( (url, link.group(2)) )
                print(name, "\t", url, file=stderr)
                dt = time.time()
                try:
                    r = urlopen(url)
                    print('=>', r.getcode(), '{:.3f}s'.format(time.time() - dt), file=stderr)
                except urllib.error.HTTPError:
                    print('=> 404', file=stderr)
                except urllib.error.URLError as e:
                    print('=> error', e, file=stderr)
                except ConnectionResetError:
                    print('=> server hung up', file=stderr)
            if ORDER in line:
                i = line.find(ORDER) + len(ORDER)
                diff = int(line[i:].split()[0])
                print_problem(chapter, name, diff, links)
            else:
                print_problem(chapter, name, None, links)



if mode != "yaml":
    print('</table>')


for k, v in c.most_common():
    print(k, v)
