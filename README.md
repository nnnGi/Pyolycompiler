# Pyolycompiler

This PolyCompiler is inspired by https://github.com/evanzhoudev/polycompiler written in Node JS.
This project is written in Python, and ultimately, the polyglot method used here is double comment parasite polyglot,
unlike the original, which used a combination of various methods.

<h1>Installation and Use:</h1>
<p>
    1) Install Python 3.13.2 -> Python3<br>
    2) Download Script
</p>

<h3>Running Programme Inside of Directory where Pyolycompiler's main.py is located</h3>

```python3 main.py in.py in.js out.poly```

<hr>

This Project will take in a ```Python (.py)``` and ```Javascript (.js)``` file and output a ```.poly``` file which can be run in both languages using

```node {file name}.poly```
and
```python3 {file name}.poly```
respectively.

<h4>Installation Requirements:</h4>
    - Node JS<br>
    - Python 3

<h3>How PyolyCompiler works</h3>
<p>PyolyCompiler uses a parasite method both ways to let syntactically correct files in both languages run in both. The script used for the parasite is

```
1 // 1; """
/*"""
#*/ {jscontent in one line} /*
{pycontent in multiple lines}
#*/
```
**Syntax Highlighting**
```python
1 // 1; """
/*"""
#*/ console.log("Hello JS"); if (1 == 1) { console.log('1 == 1'); } /*
print("Hello Python")

a = input('Hello: ')

if (1 == 1):
    print(f'1 == 1 and a == {a}')
#*/
```

```javascript
1 // 1; """
/*"""
#*/ console.log("Hello JS"); if (1 == 1) { console.log('1 == 1'); } /*
print("Hello Python")

a = input('Hello: ')

if (1 == 1):
    print(f'1 == 1 and a == {a}')
#*/
```


</p>
   

© Copyright @nnnGi (_nnn_) 2025 - 2025
