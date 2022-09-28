import sys

word = sys.stdin.readline().strip()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
total = 0
for i in croatia: 
    word = word.replace(i,'a')
print(len(word))