#!/usr/bin/python3
import py_compile
import os

filename = os.environ.get('PYFILE', 'test.py')
print(f"Compiling {filename} ...")
py_compile.compile(filename, cfile=f"{filename}c")
