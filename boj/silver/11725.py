#11725, silver2, tree
import sys 
sys.setrecursionlimit(10**6)

cnt = int(sys.stdin.readline())
graph = [[] for i in range(cnt+1)]

for _ in range(cnt-1):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(cnt+1)
ans = []

def solve(n):
    for i in graph[n]:
        if visited[i] == 0:
            visited[i] = n
            solve(i)
solve(1)
for j in range(2,cnt+1):
    print(visited[j])


