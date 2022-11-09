import sys
n, x = map(int,sys.stdin.readline().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    b.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(x):
        print(a[i][j]+b[i][j],end=' ')
    print()