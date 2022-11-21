import sys 
a,b = map(int,sys.stdin.readline().split())
set1 = set(map(int,sys.stdin.readline().split()))
set2 = set(map(int,sys.stdin.readline().split()))
ans = (set1 - set2) | (set2 - set1)
print(len(ans))