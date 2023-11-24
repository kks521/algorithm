#1158, 실버4, 큐

import sys 
from collections import deque

n,k = map(int,sys.stdin.readline().split())
temp = deque([x for x in range(1,n+1)])
ans = []

while temp:
    temp.rotate(-(k-1))
    ans.append(temp.popleft())

print(f'<{", ".join(map(str,ans))}>')