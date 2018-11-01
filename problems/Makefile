# problems_show.html: problems.yaml
# 	./yaml2html.py > ../_includes/problems_show.html
# 	./yaml2html.py --hide > ../_includes/problems_hide.html

# index.md: problems.yaml
# 	./yaml2md.py > body.md
# 	cat head.md body.md > index.md

all::
	./tex2problems.py -show ~/Documents/CUP-vie-durr/*/*.tex > ../_includes/problems_show.html 
	./tex2problems.py -hide ~/Documents/CUP-vie-durr/*/*.tex > ../_includes/problems_hide.html 
