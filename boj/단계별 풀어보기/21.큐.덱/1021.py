import sys 
from collections import deque
n, m = map(int,sys.stdin.readline().split())
ans = 0
now = 1  
deque = deque([x for x in range(1,n+1)])
choose = list(map(int,sys.stdin.readline().split()))

for i in choose: 
    target = deque.index(i)
    if target < len(deque) - target:
        while True:
            if deque[0] == i: 
                deque.popleft()
                break
            else: 
                deque.append(deque.popleft())
                ans += 1 
    else: 
         while True:
            if deque[0] == i: 
                deque.popleft()
                break
            else: 
                deque.appendleft(deque.pop())
                ans += 1 
print(ans)            