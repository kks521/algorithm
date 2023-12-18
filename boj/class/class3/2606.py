#2606, 실버3, 그래프 
import sys
from collections import deque

n = int(sys.stdin.readline())
cnt = int(sys.stdin.readline())
unvisted = [x for x in range(2,n+1)]
visted = [] 
queue = deque([1])
graph = []
for _ in range(cnt):
    graph.append(list(map(int,sys.stdin.readline().split())))

while queue:
    curr = queue.popleft()
    visted.append(curr)
    for a, b in graph:
        if a == curr and b not in visted:
            queue.append(b)
        elif b == curr and a not in visted:
            queue.append(a) 

            

print(len(set(visted))-1)