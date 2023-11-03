import sys 
from collections import deque

n = int(sys.stdin.readline())
temp1 = list(map(int,sys.stdin.readline().rstrip().split()))
temp2 = list(map(int,sys.stdin.readline().rstrip().split()))
cnt = int(sys.stdin.readline())
temp3 = list(map(int,sys.stdin.readline().rstrip().split()))\

queue = deque()

for i in range(n):
    if temp1[i] == 0:
        queue.appendleft(temp2[i])

for j in range(cnt):
    queue.append(temp3[j])
    print(queue.popleft(), end=' ')