import sys
from collections import deque 
n, k = map(int,sys.stdin.readline().split())
que = deque([i for i in range(1,n+1)])
ans = []
while len(que) > 0:
    for j in range(k - 1):
        que.append(que.popleft())
    ans.append(que.popleft())

print('<' + ', '.join(list(map(str,ans))) + '>')