# 1 2 3 4 5 
import sys
n = int(sys.stdin.readline())
total = 0 
line = 0
while n > total:
    line += 1 
    total += line 
    
u = line - (total - n)
d = line - u  
print(f"{u} / {d}") 