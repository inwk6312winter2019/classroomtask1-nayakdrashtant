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
print("\n origin path",path2)
print("\nreverse path",path2[::-1])
path2 = path2.replace('/',' ')
path2 = path2.split()
print("\n Reverse file names:")
for pat in path2:
    print(pat[::-1])


