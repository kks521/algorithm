#11724, 실버2, 그래프
import sys 
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:    
        curr = queue.popleft()
        for a in graph[curr]:
            if not visited[a]:
                queue.append(a)
                visited[a] = True

node, edge = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]

for i in range(edge):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0 
visited = [False] * (node+1)
for j in range(1,node+1):
    if not visited[j]:
        bfs(graph,j,visited)
        ans += 1

print(ans)