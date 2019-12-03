#!/usr/bin/env python3

"""
usage:

grep href  ~/Documents/CUP-vie-durr/*/*.tex | ./grep2problems.py > ../_includes/problems_show.html 
similar for -hide

l'option -yaml n'est plus d'utilité
"""

from sys import argv, stderr, stdin
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

test_urls = len(argv) == 3 

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
        print('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(chapter, name, judge))
    else:   
        # print('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(diff, name, judge))
        print('<tr><td>{}</td><td>{}</td></tr>'.format(name, judge))


# pattern = re.compile("([^\\]*)\\.*:([^\\]*)\\\\href\{([^\}]*)\}\{([^\}]*)\}.*")
pattern = re.compile(r"([^\\]*)\\[^:]*:([^\\]*)\\href{([^}]*)}{([^}]*)}")
for line in stdin:
    tab = pattern.match(line)
    if tab is not None:
        # print(tab[1], tab[2], tab[3], tab[4])
        chapter = tab[1]
        name = tab[2]
        links = [(tab[3], tab[4])]
        print_problem(chapter, name, None, links)
        if tab[2][0] == "%":
            # ignore commented out problems
            continue
        if test_urls:
            for url, code in links:
                dt = time.time()
                try:
                    r = urlopen(url)
                    if r.getcode() != 200:
                        print('=>', r.getcode(), '{:.3f}s'.format(time.time() - dt), url, code, file=stderr)
                except urllib.error.HTTPError:
                    print('=> 404', url, code, file=stderr)
                except urllib.error.URLError as e:
                    print('=> error', e, file=stderr)
                except ConnectionResetError:
                    print('=> server hung up', file=stderr)
    else:
        print("does not match", line, file=stderr)



if mode != "yaml":
    print('</table>')

