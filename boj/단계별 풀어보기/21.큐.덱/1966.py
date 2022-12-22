import sys 
from collections import deque
printer = deque()
n = int(sys.stdin.readline())
for i in range(n):
    cnt, target = map(int,sys.stdin.readline().split())
    importance = deque(map(int,sys.stdin.readline().split())) 
    idx = [x for x in range(cnt)]
    indexNum = idx[target]
    order = 0 

    while True:
        if importance[0] == max(importance):
            order += 1 
            if idx[0] == indexNum:
                print(order)
                break
            else: 
                importance.popleft()
                idx.pop(0)
        else: 
            importance.append(importance.popleft())
            idx.append(idx.pop(0))
    
