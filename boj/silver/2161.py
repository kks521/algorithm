#2161, 실버5, 큐

import sys 
from collections import deque

n = int(sys.stdin.readline())
arr = deque([x for x in range(1,n+1)])

while len(arr) > 1:
    print(arr.popleft())
    arr.append(arr.popleft())
print(arr[0])
