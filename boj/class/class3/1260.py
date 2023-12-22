#1260, 실버2, 그래프
import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visited2[start] = True
    while queue:    
        curr = queue.popleft()
        print(curr, end=' ')
        for i in range(1,n+1):
            if not visited2[i] and graph[curr][i] == 1:
                queue.append(i)
                visited2[i] = True

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in range(1,n+1):
        if not visited[i] and graph[start][i] == 1:
          dfs(i)      

n, m, start = map(int,sys.stdin.readline().split())
graph =[[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
visited2 = [False] * (n+1)
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1

dfs(start)
print()
bfs(start)