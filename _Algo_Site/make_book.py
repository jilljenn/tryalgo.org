#!/usr/bin/env python
"""
 Cookbook maker. 

 Read the input on stdin as:

 Title
 Author
 First_Algo_Name
 Complexity
 Path_To_Code
    ...
    ...
 #Section Name
 First_Algo_Name
 Complexity
 Path_To_Code
    ...
    ...
#Last Section
"""

import sys, os, traceback
import optparse, subprocess, shlex
import time
import re
#from pexpect import run, spawn

INPUT = r"""


\documentclass[8pt]{extarticle}
\usepackage[a4paper]{geometry}
\usepackage[french]{babel}
\usepackage{amssymb,amsthm,amsmath}
\usepackage{xltxtra}
\usepackage{stmaryrd}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{color}
\lstset{
	extendedchars=true,
	showstringspaces=false,
	escapeinside=``,
	keywordstyle=\color{blue},
	commentstyle=\color[rgb]{0.133,0.545,0.133},
	columns=flexible,
	language=C++,
	tabsize=2,
	basicstyle=\normalsize\selectfont\ttfamily,
	numbers=left,
	frame=lines,
	breaklines=true
}
\geometry{
	left=15mm,
	right=7mm,
	top=7mm,
	bottom=15mm
}
\usepackage{multicol}
\setlength{\columnsep}{1cm}

\title{%(title)s}
\author{%(name)s}
\date\today

\begin{document}
\maketitle
\begin{multicols}{2}
\tableofcontents
\end{multicols}
\begin{multicols}{2}
"""


def main ():

    global options, args
    
    content = {} 
    header = {'name': raw_input(), 'title': raw_input()}
    current_section =[] 
    while True:
        try:
            cur = raw_input()
            if cur[0] == '#': 
                content[cur[1:]] = current_section
                current_section = [] 
                name = raw_input()
            else:
                name = cur

            complexity  = raw_input()
            path        = raw_input()
            current_section.append((name, complexity, path)) 
        except: break
    
    g = generate_main(header, content)

    if options.verbose: print "Compiling."
    with open('book.tex','w') as f: f.write(g)
    proc = subprocess.Popen(shlex.split('xelatex book.tex'))
    proc.communicate()
    proc = subprocess.Popen(shlex.split('xelatex book.tex'))
    proc.communicate()
    if options.verbose: print "Compiled, removing temporary files."
    os.unlink('book.tex')
    os.unlink('book.toc')
    os.unlink('book.log')
    os.unlink('book.aux')


def generate_main(args, content):

    global INPUT
    main = INPUT%args # Generate customized header

    # Fillin the categories
    for section, algos in content.items():
        main += '\n\section{{{}}}\n'.format(section)
        main += "\n".join(\
            [ """
\subsection{{{}}}
Complexity : ${}$
{{\scriptsize\lstinputlisting{{{}}}}}\n\n"""\
                .format(name, compl, path) for name, compl, path in algos])
            
    main += "\end{multicols}\n\end{document}"
    return main

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(),\
                                     usage=globals()['__doc__'], version='$0.1$')
        parser.add_option ('-v', '--verbose', \
                           action='store_true', \
                           default=False, \
                           help='verbose output')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print time.asctime()
        main()
        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME IN MINUTES:',
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)

    except KeyboardInterrupt, e: # Ctrl-C
        raise e

    except SystemExit, e: # sys.exit()
        raise e

    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
