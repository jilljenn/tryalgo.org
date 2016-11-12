#!/usr/bin/env python3

import yaml

# tuples:
#   - nice
#   - chapter
#   - name
#   - links
L = []

def code(url):
    for c in ":/.":
        url = url.replace(c, " ")
    for w in url.split():
        if w not in ["http", "www", "acm", "https", "code", "google", "com", "uva", "informatik", "cs"]:
            return w
    return "?"

for item in yaml.load(open("problems.yaml").read()):
    if 'broken' in item:
        continue
    if 'order' in item:
        order = item['order']
    else:
        order = 4
    chapter = item['chapter'].replace("_"," ")
    name = item['name']
    links = item['links']
    L.append((order, chapter, name, links))

L.sort(key = lambda t: (t[1].lower(),t[2].lower()))

print('<table class="sortable"><tr><th>chapitre</th><th>difficulté</th><th>problème</th><th>énoncé</th>')
for order, chapter, name, links in L:
    hearts = "&star;" * order
    print("<tr><td>%s</td><td>%s</td><td>%s</td><td>" % (chapter, hearts, name))
    for a in links:
        print('<a href="%s">[%s]</a> ' % (a, code(a)))
    print("</td></tr>")
print("</table>")
