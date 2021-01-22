# The Python Multiprocess Debugger mPdb based on Pdb
This Debugger can be used in both Python2 and Python3. 

To use the debugger in its simplest form:
```python
 1 import numpy
 2 import flask
 3 import tensorflow
 4
 5 a = 2
 6 b = 3
 7 c = 7
 8 import mpdb
 9 mpdb.set_trace()
10 for i in range(9): # set breakpoint here, just like pdb.set_trace()
11     a += i
10     b += 2*i
11     c = a + b
```
running mpdb_cmd.py in another terminal after running the multiprocess code
you want to debug, just like below:
```bash
python mpdb_cmd.py
```
or 
```bash
python3 mpdb_cmd.py
```
or
```bash
python2 mpdb_cmd.py
```
depend on your own system setting.

Other operations the same as Pdb.

Note: the running order doesn't matter, running mpdb_cmd.py first is also ok, but
mpdb_cmd.py must be in the directory where the main program Python file
which you want to debug is, so recommend use 'mv' command to move mpdb_cmd.py
if you need change main program which you want to debug.

# Installation:
Running install.py like below:
```bash
python3 install.py
```
or
```bash
python install.py
```
or
```bash
python2 install.py
```
depend on your own system setting.
Actually, running install.py is finding in which sys.path pdb.py is, and then copy mpdb.py to the path.

# Example
There is a test directory in current directory, a test_code.py is in test directory.
1. copy mpdb_cmd.py to test directory.
2. run test_code.py or mpdb_cmd.py in current terminal, which one doesn't matter, just choose one.
3. open another terminal, change to test directory and run the mpdb_cmd.py if you run the test_code.py 
in previous step, vice versa.
4. if succeed, you will see (Pdb) prompt in the terminal you run the mpdb_cmd.py.     





 



