import sys

space = [[0 for i in range(100)]for j in range(100)] 
n = int(sys.stdin.readline())
for k in range(n):
    n,m  = map(int,sys.stdin.readline().split())
    for i in range(n,n+10):
        for k in range(m,m+10):
            space[i][k] += 1 
blank = 0  
for i in space:
    blank += i.count(0)   
print(10000-blank)