'''
This PolyCompiler is inspired by https://github.com/evanzhoudev/polycompiler written in Node JS.
This project is written in Python, and ultimately the polyglot method used here is double comment parasite polyglot,
unlike the original which used a combination of various methods.

Input:
polycompiler in.py in.js out.poly

This Project will take in a Python (.py) and Javascript (.js) file and output a .poly file which can be run in both languages using

node {file name}.poly
and
python3 {file name}.poly
respectively.

© Copyright @_nnn_ 2025 - 2025
'''
import sys

def polycompile(in_py, in_js, out_poly):
    ###########################
    # File Reading
    ###########################
    with open(in_py, 'r') as pyfile:
       pycontent = pyfile.read()

    with open(in_js, 'r') as jsfile:
        jscontent = jsfile.read()
        jscontent = list(jscontent)
        for i in range(len(jscontent)):
            if jscontent[i] == '\n':
                jscontent[i] = ' '
        jscontent = ''.join(jscontent)

    ###########################
    # Files -> Polyglot File
    ###########################
    with open(out_poly, 'w') as result:
        base = f'''1 // 1; """
/*"""
#*/ {jscontent} /*
{pycontent}
#*/
'''
        result.write(base)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        py = sys.argv[1]
        js = sys.argv[2]
        poly = sys.argv[3]
        polycompile(py, js, poly)