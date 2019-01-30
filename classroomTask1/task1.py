from __future__ import print_function
import os,sys
from pathlib import Path
home = str(Path.home())
 
path = home
 
if len(sys.argv) == 2:
    path = sys.argv[1]
 
#print(path) 
files = os.listdir(path)
for name in files:
    print(name)

path2 = os.getcwd()
print("origin path",path2)
print("reverse path",path2
[::-1])
